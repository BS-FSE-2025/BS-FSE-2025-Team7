from django import forms
from .models import Compliment

class ComplimentForm(forms.ModelForm):
    class Meta:
        model = Compliment
        fields = ['name', 'email', 'phone_number', 'description', 'latitude', 'longitude']

    # Custom fields for location can be added if necessary
    latitude = forms.DecimalField(widget=forms.HiddenInput())
    longitude = forms.DecimalField(widget=forms.HiddenInput())
