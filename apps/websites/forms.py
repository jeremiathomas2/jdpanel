from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['domain', 'php_version']
        widgets = {
            'domain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example.com'}),
            'php_version': forms.Select(choices=[('8.1', 'PHP 8.1'), ('8.2', 'PHP 8.2'), ('8.3', 'PHP 8.3')], attrs={'class': 'form-control'}),
        }
