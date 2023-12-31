from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "agent",
            "age",
        )