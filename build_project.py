import os
import shutil
import zipfile

PROJECT_NAME = "international_states_agency"

FILES = {
    # -------------------------------------------------------------
    # requirements.txt
    # -------------------------------------------------------------
    "requirements.txt": """django>=5.0
requests>=2.31.0
python-dotenv>=1.0.0
""",
    # -------------------------------------------------------------
    # .env.example
    # -------------------------------------------------------------
    ".env.example": """SECRET_KEY=django-insecure-international-states-elite-agency-key
DEBUG=True
N8N_LEAD_WEBHOOK_URL=https://n8n.yourdomain.com/webhook/lead-intake-endpoint
N8N_WEBHOOK_SECRET=is_prod_sec_99a81b7e408d24
""",
    # -------------------------------------------------------------
    # manage.py
    # -------------------------------------------------------------
    "manage.py": """#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
""",
    # -------------------------------------------------------------
    # core/__init__.py
    # -------------------------------------------------------------
    "core/__init__.py": "",
    # -------------------------------------------------------------
    # core/settings.py
    # -------------------------------------------------------------
    "core/settings.py": """import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-sample-key-for-development')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agency',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'agency' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'agency' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Webhook configuration
N8N_LEAD_WEBHOOK_URL = os.environ.get('N8N_LEAD_WEBHOOK_URL', '')
N8N_WEBHOOK_SECRET = os.environ.get('N8N_WEBHOOK_SECRET', '')
""",
    # -------------------------------------------------------------
    # core/urls.py
    # -------------------------------------------------------------
    "core/urls.py": """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agency.urls')),
]
""",
    # -------------------------------------------------------------
    # core/wsgi.py
    # -------------------------------------------------------------
    "core/wsgi.py": """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()
""",
    # -------------------------------------------------------------
    # agency/__init__.py
    # -------------------------------------------------------------
    "agency/__init__.py": "",
    # -------------------------------------------------------------
    # agency/apps.py
    # -------------------------------------------------------------
    "agency/apps.py": """from django.apps import AppConfig

class AgencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agency'
""",
    # -------------------------------------------------------------
    # agency/urls.py
    # -------------------------------------------------------------
    "agency/urls.py": """from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.case_studies_list, name='case_studies_list'),
    path('work/<slug:slug>/', views.case_study_detail, name='case_study_detail'),
    path('api/lead/submit/', views.submit_lead_contact, name='submit_lead_contact'),
]
""",
    # -------------------------------------------------------------
    # agency/forms.py
    # -------------------------------------------------------------
    "agency/forms.py": """import time
from django import forms
from django.core.exceptions import ValidationError

class LeadContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True, strip=True)
    email = forms.EmailField(max_length=254, required=True)
    company_name = forms.CharField(max_length=120, required=True, strip=True)
    service = forms.ChoiceField(
        choices=[
            ('ai_agents', 'Autonomous AI Agents'),
            ('workflow_automation', 'Workflow & Process Automation'),
            ('conversational_ai', 'Conversational AI & Knowledge Vaults'),
            ('crm_automation', 'CRM & Pipeline Systems'),
            ('voice_assistants', 'AI Voice Telephony'),
            ('custom_integrations', 'Custom Enterprise AI Architecture'),
        ],
        required=True
    )
    budget = forms.ChoiceField(
        choices=[
            ('', 'Select Budget Range (Optional)'),
            ('5k_10k', '$5,000 – $10,000'),
            ('10k_25k', '$10,000 – $25,000'),
            ('25k_50k', '$25,000 – $50,000'),
            ('50k_plus', '$50,000+'),
        ],
        required=False
    )
    description = forms.CharField(max_length=2500, required=True, strip=True)
    consent = forms.BooleanField(required=True)
    website_url_hp = forms.CharField(required=False)
    form_render_ts = forms.FloatField(required=False)

    def clean_website_url_hp(self):
        if self.cleaned_data.get('website_url_hp'):
            raise ValidationError("Spam trigger detected.")
        return ''

    def clean_form_render_ts(self):
        ts = self.cleaned_data.get('form_render_ts')
        if ts and (time.time() - float(ts)) < 2.0:
            raise ValidationError("Automated submission speed rejected.")
        return ts
""",
    # -------------------------------------------------------------
    # agency/case_data.py
    # -------------------------------------------------------------
    "agency/case_data.py": """CASE_STUDIES = [
    {
        "slug": "autonomous-freight-manifest-reconciliation",
        "title": "Autonomous Multi-Modal Manifest & Customs Reconciliation Engine",
        "client_industry": "Global Freight Logistics & Maritime Shipping",
        "client_classification": "[Confidential Enterprise / EMEA Operations]",
        "summary": "Engineering a deterministic multi-agent pipeline to extract, cross-verify, and audit multilingual customs declarations across 14 European and North American ports.",
        "challenge": "The client processed over 4,500 shipping manifests weekly across 4 languages. An auditing team of 8 analysts spent 42 minutes per document reconciling tariff codes against legacy ERP records.",
        "solution": "We engineered an air-gapped, multi-agent cognitive architecture. Inbound documents are routed to a multimodal vision agent, structured into typed Pydantic models, and verified by deterministic mathematical guardrails.",
        "system_architecture": [
            {"step": "01", "name": "Ingestion Gateway", "desc": "Air-gapped S3 bucket webhook trigger capturing PDFs and EDIFACT feeds."},
            {"step": "02", "name": "Multimodal Extraction", "desc": "Vision LLM parsing 4 languages into strictly typed Pydantic models."},
            {"step": "03", "name": "Mathematical Guardrail", "desc": "Deterministic Python layer verifying weight balance and tariff compliance."},
            {"step": "04", "name": "ERP Mutation & Alerting", "desc": "Synchronous NetSuite API mutation + Slack alert to on-duty customs broker."}
        ],
        "technologies": ["Python 3.12", "LangGraph", "Pydantic V2", "FastAPI", "Docker", "NetSuite SuiteTalk API"],
        "process_steps": [
            {"phase": "Phase 01: Audit", "detail": "14-day analysis of 5,000 legacy manifests to map tariff edge-cases."},
            {"phase": "Phase 02: Architecture", "detail": "Specification of zero-drift validation contracts and human-in-the-loop fallbacks."},
            {"phase": "Phase 03: Sandbox", "detail": "Dual-run processing against live operations for 21 days with 0 production mutations."},
            {"phase": "Phase 04: Production", "detail": "Full cutover across 14 European and North American port terminals."}
        ],
        "verified_outcomes": [
            {"metric": "84%", "label": "Reduction in End-to-End Processing Latency", "note": "[Verified Production Benchmark]"},
            {"metric": "320 hrs", "label": "Reclaimed Analyst Capacity Per Week", "note": "[Audited Operations Metric]"},
            {"metric": "< 0.02%", "label": "Discrepancy Escape Rate", "note": "[Deterministic Guardrail Standard]"}
        ],
        "system_status": "OPERATIONAL // 14 NODES ACTIVE"
    },
    {
        "slug": "air-gapped-sovereign-contract-intelligence",
        "title": "Air-Gapped Sovereign RAG & Deal Diligence Vault",
        "client_industry": "Cross-Border Private Equity & Corporate Law",
        "client_classification": "[Tier-1 Financial Advisory / Zurich]",
        "summary": "Building a private, self-hosted vector intelligence environment to cross-examine 40,000+ proprietary M&A contracts without third-party data leakage.",
        "challenge": "During acquisitions, legal teams faced weeks of manual due diligence. Regulations prohibited uploading proprietary transaction data to commercial public LLMs.",
        "solution": "International States architected an on-premise, air-gapped retrieval-augmented generation (RAG) platform with self-hosted open-weights models and verbatim citation guardrails.",
        "system_architecture": [
            {"step": "01", "name": "Air-Gapped Ingestion", "desc": "Local pipeline parsing encrypted PDF, DOCX, and legacy records."},
            {"step": "02", "name": "Semantic Chunking", "desc": "Hierarchical clause-aware chunking preserving contextual legal relationships."},
            {"step": "03", "name": "Hybrid Vector Search", "desc": "Dense vector + BM25 sparse keyword retrieval with reranking."},
            {"step": "04", "name": "Citation Guard", "desc": "Deterministic post-processor blocking any answer lacking a direct document anchor."}
        ],
        "technologies": ["Qdrant", "Llama-3 70B", "vLLM", "FastAPI", "Tailwind CSS", "CUDA 12"],
        "process_steps": [
            {"phase": "Phase 01: Compliance", "detail": "Information security audit to ensure complete zero-egress hardware isolation."},
            {"phase": "Phase 02: Pipeline", "detail": "Custom legal tokenization and synthetic legal evaluation dataset creation."},
            {"phase": "Phase 03: Reranking", "detail": "Fine-tuning of cross-encoder reranking layer for specialized contract clauses."},
            {"phase": "Phase 04: Rollout", "detail": "Secured deployment to 45 M&A partners with hardware token auth."}
        ],
        "verified_outcomes": [
            {"metric": "480ms", "label": "Average Semantic Clause Retrieval Time", "note": "[Measured on 100K Chunk Corpus]"},
            {"metric": "0.00%", "label": "External Data Egress / Cloud Leakage", "note": "[SOC2 / Hardware Verified]"},
            {"metric": "140 hrs", "label": "Saved Per Transaction Audit Cycle", "note": "[Partner Review Feedback]"}
        ],
        "system_status": "DEPLOYED // AIR-GAPPED PRIVATE CLOUD"
    }
]

def get_all_case_studies():
    return CASE_STUDIES

def get_case_study(slug):
    return next((cs for cs in CASE_STUDIES if cs["slug"] == slug), None)
""",
    # -------------------------------------------------------------
    # agency/views.py
    # -------------------------------------------------------------
    "agency/views.py": """import json
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
""",
    # -------------------------------------------------------------
    # agency/static/css/motion.css
    # -------------------------------------------------------------
    "agency/static/css/motion.css": """:root {
    --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
    --motion-fast: 180ms;
    --motion-medium: 260ms;
}
.editorial-link {
    position: relative;
    display: inline-flex;
    align-items: center;
}
.editorial-link::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: currentColor;
    transform: scaleX(0);
    transform-origin: right center;
    transition: transform var(--motion-medium) var(--ease-out-expo);
}
.editorial-link:hover::after {
    transform: scaleX(1);
    transform-origin: left center;
}
.btn-motion {
    transition: transform var(--motion-fast) ease, background-color var(--motion-fast) ease;
}
.btn-motion:active { transform: scale(0.985); }
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
""",
    # -------------------------------------------------------------
    # agency/static/js/motion.js
    # -------------------------------------------------------------
    "agency/static/js/motion.js": """document.addEventListener("DOMContentLoaded", () => {
    const isReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const navHeader = document.querySelector("header");
    const progressBar = document.getElementById("nav-scroll-progress");

    window.addEventListener("scroll", () => {
        const scrolled = window.scrollY;
        const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
        if (scrolled > 40) {
            navHeader?.classList.add("bg-[#070709]/95", "shadow-xl");
        } else {
            navHeader?.classList.remove("bg-[#070709]/95", "shadow-xl");
        }
        if (progressBar && maxScroll > 0) {
            progressBar.style.width = `${(scrolled / maxScroll) * 100}%`;
        }
    }, { passive: true });
});
""",
    # -------------------------------------------------------------
    # agency/templates/index.html
    # -------------------------------------------------------------
    "agency/templates/index.html": """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>International States | Autonomous AI Systems</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/motion.css' %}">
    <style>
        body { background-color: #070709; color: #E2E8F0; font-family: 'Inter', sans-serif; overflow-x: hidden; }
        .hairline-all { border: 1px solid rgba(255, 255, 255, 0.08); }
        .hairline-b { border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
        .hairline-t { border-top: 1px solid rgba(255, 255, 255, 0.08); }
    </style>
</head>
<body class="selection:bg-purple-500 selection:text-white">

    <!-- Nav -->
    <header class="fixed top-0 left-0 w-full z-50 bg-[#070709]/80 backdrop-blur-xl hairline-b transition-colors">
        <div id="nav-scroll-progress" class="absolute top-0 left-0 h-[1.5px] bg-gradient-to-r from-purple-400 to-indigo-400 w-0 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-6 h-18 flex items-center justify-between">
            <a href="#" class="flex items-center gap-3">
                <div class="w-5 h-5 border border-white/20 rotate-45 flex items-center justify-center">
                    <div class="w-1.5 h-1.5 bg-purple-400"></div>
                </div>
                <span class="font-bold text-xs uppercase tracking-widest text-white">International States</span>
            </a>
            <nav class="hidden md:flex items-center gap-8 text-xs text-zinc-400 font-medium">
                <a href="#services" class="editorial-link hover:text-white py-1">Services</a>
                <a href="#work" class="editorial-link hover:text-white py-1">Case Studies</a>
                <a href="#process" class="editorial-link hover:text-white py-1">Framework</a>
                <a href="#contact" class="editorial-link hover:text-white py-1">Inquiry</a>
            </nav>
            <a href="#contact" class="btn-motion px-4 py-2 bg-white text-black text-xs font-semibold uppercase tracking-wider hover:bg-purple-200">
                Book Consultation
            </a>
        </div>
    </header>

    <!-- Hero -->
    <section class="relative pt-40 pb-24 max-w-7xl mx-auto px-6">
        <div class="max-w-3xl">
            <div class="font-mono text-xs text-purple-400 uppercase tracking-widest mb-4">
                [ ENTERPRISE AI ARCHITECTURE ]
            </div>
            <h1 class="text-4xl sm:text-6xl md:text-7xl font-semibold tracking-tight text-white mb-6 leading-[1.04]">
                We Build AI Systems <br>
                That Work While <br>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-zinc-200 to-purple-300">You Scale.</span>
            </h1>
            <p class="text-base sm:text-lg text-zinc-400 font-light leading-relaxed mb-8 max-w-xl">
                From intelligent AI agents to end-to-end business automation, we design and deploy systems that eliminate repetitive work and help teams move faster.
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
                <a href="#contact" class="btn-motion px-8 py-4 bg-white text-black text-xs font-semibold uppercase tracking-wider hover:bg-purple-200 flex items-center justify-center gap-2">
                    <span>Book a Strategy Call</span>
                    <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="#work" class="px-8 py-4 hairline-all text-white text-xs font-semibold uppercase tracking-wider hover:bg-white/5 flex items-center justify-center">
                    Explore Our Work
                </a>
            </div>
        </div>
    </section>

    <!-- Services Bento -->
    <section id="services" class="py-24 hairline-t bg-[#0D0E12]">
        <div class="max-w-7xl mx-auto px-6">
            <div class="mb-14">
                <span class="font-mono text-xs text-purple-400 uppercase tracking-widest">SYSTEM CAPABILITIES</span>
                <h2 class="text-3xl font-medium text-white mt-2">Architected for Autonomous Leverage</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="hairline-all bg-[#070709] p-8">
                    <span class="font-mono text-xs text-zinc-500 block mb-3">01 // REASONING</span>
                    <h3 class="text-lg font-medium text-white mb-2">Autonomous AI Agents</h3>
                    <p class="text-xs text-zinc-400 font-light leading-relaxed">Multi-agent LangGraph workflows executing deterministic cross-software decisions.</p>
                </div>
                <div class="hairline-all bg-[#070709] p-8">
                    <span class="font-mono text-xs text-zinc-500 block mb-3">02 // INTEGRATION</span>
                    <h3 class="text-lg font-medium text-white mb-2">Workflow &amp; n8n Automation</h3>
                    <p class="text-xs text-zinc-400 font-light leading-relaxed">Private self-hosted orchestration connecting enterprise databases and cloud APIs.</p>
                </div>
                <div class="hairline-all bg-[#070709] p-8">
                    <span class="font-mono text-xs text-zinc-500 block mb-3">03 // KNOWLEDGE</span>
                    <h3 class="text-lg font-medium text-white mb-2">Air-Gapped Sovereign RAG</h3>
                    <p class="text-xs text-zinc-400 font-light leading-relaxed">Grounded vector search with strict citations and zero data leakage to public models.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Selected Work -->
    <section id="work" class="py-24 hairline-t">
        <div class="max-w-7xl mx-auto px-6">
            <div class="flex justify-between items-end mb-14">
                <div>
                    <span class="font-mono text-xs text-purple-400 uppercase tracking-widest">SELECTED WORK</span>
                    <h2 class="text-3xl font-medium text-white mt-2">Production Case Studies</h2>
                </div>
                <a href="{% url 'case_studies_list' %}" class="text-xs font-mono text-zinc-400 hover:text-white uppercase">View All Archive →</a>
            </div>
            <div class="space-y-8">
                {% for item in case_studies %}
                <div class="hairline-all bg-[#0D0E12] p-8 md:p-12 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                    <div>
                        <div class="text-[10px] font-mono text-purple-400 uppercase mb-2">{{ item.client_industry }}</div>
                        <h3 class="text-2xl font-medium text-white mb-3">{{ item.title }}</h3>
                        <p class="text-xs sm:text-sm text-zinc-400 max-w-2xl font-light">{{ item.summary }}</p>
                    </div>
                    <a href="{% url 'case_study_detail' item.slug %}" class="px-6 py-3 bg-white text-black font-semibold text-xs uppercase tracking-wider hover:bg-purple-200 shrink-0">
                        Inspect Blueprint
                    </a>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Contact Lead Section with n8n Integration -->
    <section id="contact" class="py-24 hairline-t bg-[#0D0E12]">
        <div class="max-w-4xl mx-auto px-6">
            <div class="text-center mb-12">
                <span class="font-mono text-xs text-purple-400 uppercase tracking-widest">QUALIFICATION GATEWAY</span>
                <h2 class="text-3xl sm:text-4xl font-medium text-white mt-2">Schedule Architectural Discovery</h2>
            </div>
            <form id="lead-intake-form" action="{% url 'submit_lead_contact' %}" method="POST" class="space-y-4">
                {% csrf_token %}
                <div style="display:none;" aria-hidden="true">
                    <input type="text" name="website_url_hp" tabindex="-1">
                </div>
                <input type="hidden" id="form_render_ts" name="form_render_ts" value="">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <input type="text" name="full_name" required placeholder="Full Name *" class="w-full bg-[#070709] hairline-all px-4 py-3 text-xs text-white">
                    <input type="email" name="email" required placeholder="Work Email *" class="w-full bg-[#070709] hairline-all px-4 py-3 text-xs text-white">
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <input type="text" name="company_name" required placeholder="Company Name *" class="w-full bg-[#070709] hairline-all px-4 py-3 text-xs text-white">
                    <select name="service" required class="w-full bg-[#070709] hairline-all px-4 py-3 text-xs text-zinc-300">
                        <option value="ai_agents">Autonomous AI Agents</option>
                        <option value="workflow_automation">Workflow Automation</option>
                        <option value="conversational_ai">Conversational AI &amp; RAG</option>
                        <option value="crm_automation">CRM &amp; Sales Pipelines</option>
                    </select>
                </div>
                <textarea name="description" rows="3" required placeholder="Describe your operational bottleneck..." class="w-full bg-[#070709] hairline-all px-4 py-3 text-xs text-white"></textarea>
                <label class="flex items-center gap-2 text-xs text-zinc-400">
                    <input type="checkbox" name="consent" required>
                    <span>I agree to confidential enterprise data evaluation.</span>
                </label>
                <button type="submit" id="lead-submit-btn" class="w-full py-4 bg-white hover:bg-purple-200 text-black font-semibold text-xs uppercase tracking-wider">
                    Submit Consultation Request
                </button>
                <div id="form-feedback" class="hidden p-4 hairline-all text-xs font-mono text-center"></div>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="hairline-t py-12 text-center font-mono text-xs text-zinc-600">
        © 2025 INTERNATIONAL STATES AGENCY. ALL RIGHTS RESERVED.
    </footer>

    {% load static %}
    <script src="{% static 'js/motion.js' %}"></script>
    <script>
        lucide.createIcons();
        document.getElementById("form_render_ts").value = (Date.now() / 1000).toFixed(2);
        const form = document.getElementById("lead-intake-form");
        const feedback = document.getElementById("form-feedback");
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            feedback.className = "hidden";
            const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: {"X-Requested-With": "XMLHttpRequest"} });
            const data = await res.json();
            feedback.className = res.ok ? "p-4 hairline-all bg-emerald-500/10 text-emerald-300 text-xs font-mono block" : "p-4 hairline-all bg-red-500/10 text-red-300 text-xs font-mono block";
            feedback.textContent = data.message;
            if(res.ok) form.reset();
        });
    </script>
</body>
</html>
""",
    # -------------------------------------------------------------
    # agency/templates/case_studies_list.html
    # -------------------------------------------------------------
    "agency/templates/case_studies_list.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Production Case Studies | International States</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { background-color: #070709; color: #E2E8F0; font-family: 'Inter', sans-serif; } .hairline-all { border: 1px solid rgba(255,255,255,0.08); }</style>
</head>
<body class="p-8 max-w-5xl mx-auto">
    <a href="{% url 'home' %}" class="text-xs font-mono text-purple-400 uppercase">← Return to Flagship</a>
    <h1 class="text-4xl font-medium text-white my-6">Systems Architecture Archive</h1>
    <div class="space-y-6">
        {% for item in case_studies %}
        <div class="hairline-all bg-[#0D0E12] p-8">
            <span class="text-[10px] font-mono text-zinc-500 uppercase">{{ item.client_industry }}</span>
            <h2 class="text-xl font-medium text-white mt-1 mb-3">{{ item.title }}</h2>
            <p class="text-xs text-zinc-400 mb-6">{{ item.summary }}</p>
            <a href="{% url 'case_study_detail' item.slug %}" class="text-xs font-mono text-purple-300 uppercase">Inspect Blueprint →</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
""",
    # -------------------------------------------------------------
    # agency/templates/case_study_detail.html
    # -------------------------------------------------------------
    "agency/templates/case_study_detail.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ case.title }} | International States</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body { background-color: #070709; color: #E2E8F0; font-family: 'Inter', sans-serif; } .hairline-all { border: 1px solid rgba(255,255,255,0.08); }</style>
</head>
<body class="p-8 max-w-4xl mx-auto">
    <a href="{% url 'case_studies_list' %}" class="text-xs font-mono text-purple-400 uppercase">← Systems Index</a>
    <div class="my-8">
        <span class="text-xs font-mono text-zinc-500 uppercase">{{ case.client_industry }}</span>
        <h1 class="text-3xl sm:text-5xl font-medium text-white my-4">{{ case.title }}</h1>
        <p class="text-base text-zinc-400 leading-relaxed">{{ case.summary }}</p>
    </div>
    <div class="grid grid-cols-3 gap-4 hairline-all bg-[#0D0E12] p-6 mb-8 font-mono">
        {% for o in case.verified_outcomes %}
        <div>
            <div class="text-2xl text-white">{{ o.metric }}</div>
            <div class="text-[10px] text-zinc-400 uppercase">{{ o.label }}</div>
        </div>
        {% endfor %}
    </div>
    <div class="space-y-6 text-sm text-zinc-300 mb-12">
        <h2 class="text-lg font-medium text-white font-mono uppercase">Execution Topology</h2>
        {% for node in case.system_architecture %}
        <div class="hairline-all p-4 bg-[#0D0E12]">
            <span class="text-purple-400 font-mono text-xs">{{ node.step }}</span>
            <div class="text-white font-medium">{{ node.name }}</div>
            <div class="text-xs text-zinc-400">{{ node.desc }}</div>
        </div>
        {% endfor %}
    </div>
    <a href="{% url 'home' %}#contact" class="inline-block px-8 py-4 bg-white text-black text-xs font-semibold uppercase tracking-wider">Schedule Similar Audit</a>
</body>
</html>
""",
}


def build():
    print(f"📦 Generating {PROJECT_NAME} directory structure...")
    base_path = os.path.abspath(PROJECT_NAME)

    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path, exist_ok=True)

    for rel_path, content in FILES.items():
        file_path = os.path.join(base_path, rel_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Created: {rel_path}")

    # Generate ZIP File
    zip_filename = f"{PROJECT_NAME}.zip"
    print(f"\n🗜️  Compressing into {zip_filename}...")
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(base_path):
            for file in files:
                abs_file = os.path.join(root, file)
                arcname = os.path.relpath(abs_file, start=os.path.dirname(base_path))
                zipf.write(abs_file, arcname)

    print(f"\n🎉 SUCCESS!")
    print(f"1. Project folder ready at: ./{PROJECT_NAME}/")
    print(f"2. Complete ZIP file ready at: ./{zip_filename}")
    print("\nNext steps to run:")
    print(f"   cd {PROJECT_NAME}")
    print("   pip install django requests python-dotenv")
    print("   python manage.py migrate")
    print("   python manage.py runserver")


if __name__ == "__main__":
    build()