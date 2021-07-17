from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Curso, UserExtra, LlevaCurso

class AuthenticationAddForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)

class UserRegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserExtraRegisterForm(ModelForm):

    class Meta:
        model = UserExtra
        fields = ['dpi', 'telefono', 'direccion', 'fecha_nacimiento', 'sexo', 'nivel_academico', 'rol']

class LlevaCursoRegisterForm(ModelForm):

    class Meta:
        model = LlevaCurso
        fields = ['curso', 'fecha_llevado']

class CursoRegisterForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'inscripcion', 'cuota', 'otros', 'duracion']