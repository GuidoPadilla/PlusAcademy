from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from usuarios.models import Curso, UserExtra

class AuthenticationAddForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)

class UserRegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UserExtraRegisterForm(ModelForm):

    class Meta:
        model = UserExtra
        fields = ['dpi', 'telefono', 'direccion', 'fecha_nacimiento', 'sexo', 'nivel_academico', 'rol']