from django.db.models import fields
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
        fields = ['user','curso', 'fecha_llevado']

class CursoRegisterForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'inscripcion', 'cuota', 'otros', 'duracion']


class CobroExtraForm(forms.Form):
    codigo_curso = forms.fields.CharField(label='Código de Curso', max_length=100)
    monto = forms.fields.DecimalField(label='Monto', decimal_places=2, max_digits= 6)
    fecha_limite = forms.fields.DateField(label='Fecha Límite')
#    class Meta:
#        fields = ['codigo de curso', 'monto', 'fecha limite']