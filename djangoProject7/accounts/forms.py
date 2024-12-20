from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['description', 'email', 'latitude', 'longitude', 'name', 'phone_number', 'photo']  # Ensure 'created_at' is not listed here if it is not editable
