from django.forms import ModelForm, Form
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from .models import Curso, UserExtra, LlevaCurso, Sexo, NivelAcademico, Rol, Nacionalidad

class AuthenticationAddForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario", max_length=150)
    password = forms.CharField(label="Contraseña", max_length=150, widget=forms.PasswordInput)

class UserRegisterForm(ModelForm):

    class Meta:
        model = User
        fields= ('username', 'password', 'first_name', 'last_name', 'email', 'is_staff')
        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput() 
        }

    # def __init__(self, *args, **kwargs):
    #     # user should be popped here
    #     user = kwargs.pop('user', None)
    #     super(UserRegisterForm(), self).__init__(*args, **kwargs)
    #     # just in case your user is empty
    #     if user and not user.is_staff:
    #        del self.fields['is_staff']
class UserExtraRegisterForm(Form):

    dpi = forms.CharField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    sexo = forms.ModelChoiceField(queryset=Sexo.objects.all())
    nivel_academico = forms.ModelChoiceField(queryset=NivelAcademico.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(codigo=2))
    nacionalidad = forms.ModelChoiceField(queryset=Nacionalidad.objects.all())


    class Meta:
        model = UserExtra
        # fields = ['dpi', 'telefono', 'direccion', 'fecha_nacimiento', 'sexo', 'nivel_academico', 'rol', 'nacionalidad']

class StudentRegisterForm(ModelForm):

    class Meta:
        model = User
        fields= ('username', 'first_name', 'last_name', 'email')


class StudentExtraRegisterForm(Form):

    dpi = forms.CharField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    sexo = forms.ModelChoiceField(queryset=Sexo.objects.all())
    nivel_academico = forms.ModelChoiceField(queryset=NivelAcademico.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(codigo=1))
    nacionalidad = forms.ModelChoiceField(queryset=Nacionalidad.objects.all())


    class Meta:
        model = UserExtra
        # fields = ['dpi', 'telefono', 'direccion', 'fecha_nacimiento', 'sexo', 'nivel_academico', 'rol', 'nacionalidad']


class LlevaCursoRegisterForm(Form):

    user = forms.ModelChoiceField(queryset=User.objects.all())
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    fecha_llevado = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = LlevaCurso
        #fields = ['user','curso', 'fecha_llevado']
    def __init__(self, *args, **kwrgs):
        super(LlevaCursoRegisterForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')

class CursoRegisterForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'inscripcion_quetzales', 'cuota_quetzales', 'inscripcion_dolares', 'cuota_dolares', 'duracion']

class DefNivelAcaForm(ModelForm):
    class Meta:
        model = NivelAcademico
        fields= ['nombre']