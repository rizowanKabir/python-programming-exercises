import json
import time
import hashlib
import logging
import requests
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_POST
from django.conf import settings
from .forms import LeadContactForm
from .case_data import get_all_case_studies, get_case_study

logger = logging.getLogger(__name__)

def home(request):
    case_studies = get_all_case_studies()[:2]
    return render(request, "index.html", {"case_studies": case_studies})

def case_studies_list(request):
    case_studies = get_all_case_studies()
    return render(request, "case_studies_list.html", {"case_studies": case_studies})

def case_study_detail(request, slug):
    case = get_case_study(slug)
    if not case:
        raise Http404("Architectural blueprint not found.")
    return render(request, "case_study_detail.html", {"case": case})

@require_POST
def submit_lead_contact(request):
    form = LeadContactForm(request.POST)
    if not form.is_valid():
        errors = {field: err[0] for field, err in form.errors.get_json_data().items()}
        return JsonResponse({"status": "error", "message": "Validation failed.", "errors": errors}, status=400)

    data = form.cleaned_data
    fingerprint = hashlib.sha256(f"{data['email'].lower()}:{data['company_name'].lower()}".encode()).hexdigest()
    
    last_sub = request.session.get("last_lead_fingerprint")
    last_sub_time = request.session.get("last_lead_timestamp", 0)

    if last_sub == fingerprint and (time.time() - last_sub_time) < 180:
        return JsonResponse({"status": "duplicate", "message": "Inquiry already received. We will contact you shortly."}, status=429)

    webhook_url = getattr(settings, "N8N_LEAD_WEBHOOK_URL", "")
    webhook_secret = getattr(settings, "N8N_WEBHOOK_SECRET", "")

    # Local simulation fallback if webhook not configured
    if not webhook_url or "yourdomain" in webhook_url or "demo" in webhook_url:
        request.session["last_lead_fingerprint"] = fingerprint
        request.session["last_lead_timestamp"] = time.time()
        return JsonResponse({
            "status": "simulated",
            "message": "✓ Registered in local dev mode. (Connect your real n8n webhook URL in .env to transmit to Google Sheets)."
        }, status=200)

    payload = {
        "event": "lead.created",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "lead_data": {
            "full_name": data["full_name"],
            "business_email": data["email"],
            "company_name": data["company_name"],
            "service_slug": data["service"],
            "budget_tier": data["budget"] or "unspecified",
            "project_description": data["description"],
            "consent_granted": data["consent"]
        }
    }

    try:
        res = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json", "X-Webhook-Secret": webhook_secret},
            timeout=5.0
        )
        if res.status_code in (200, 201, 204):
            request.session["last_lead_fingerprint"] = fingerprint
            request.session["last_lead_timestamp"] = time.time()
            return JsonResponse({"status": "success", "message": "Inquiry successfully dispatched to systems queue."}, status=200)
        return JsonResponse({"status": "upstream_error", "message": "Upstream service error. Please contact directly via email."}, status=502)
    except Exception as e:
        return JsonResponse({"status": "timeout", "message": "Gateway timed out. Please retry momentarily."}, status=504)
