from django import forms
from .models import Database, DatabaseUser

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ['name', 'db_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'wp_site'}),
            'db_type': forms.Select(attrs={'class': 'form-control'}),
        }

class DatabaseUserForm(forms.ModelForm):
    class Meta:
        model = DatabaseUser
        fields = ['username', 'password', 'databases']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'wp_user'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'databases': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
