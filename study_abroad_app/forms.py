# study_abroad_app/forms.py
from django import forms
from .models import Application , Program
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ApplicationForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), label='Program')
    class Meta:
        model = Application
        fields = [ 'status','first_name', 'last_name', 'passport_number', 'date_of_birth', 'passport_upload', 'certificate_upload', 'signed_form_upload' , 'program']
        widgets = {
            'status': forms.HiddenInput(),  # Optional: Hide the status field in the form
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].required = False

        
    def clean(self):
            cleaned_data = super().clean()
            # Add custom validation logic here
            return cleaned_data


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




