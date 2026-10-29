import time
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
