from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class AuthenticationAddForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)