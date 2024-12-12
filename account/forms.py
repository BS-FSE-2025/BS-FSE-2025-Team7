from django import forms
from django.core.exceptions import ValidationError
from account.models import Register ,Register2 # Adjust based on your structure
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register  # Your Register model
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")  # Attach the error to the second password field

        return cleaned_data


from django import forms
from .models import Register2

class RegisterForm2(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register2  # Your Register2 model
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")  # Attach the error to the second password field

        return cleaned_data
