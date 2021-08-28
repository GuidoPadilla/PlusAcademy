from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from pagos.models import Pago, Cobro

class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'cobro', 'forma_pago', 'moneda', 'cantidad']
    def __init__(self, *args, **kwrgs):
        super(PaymentRegisterForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')

class CobroExtraForm(forms.Form):
    codigo_curso = forms.fields.CharField(label='Código de Curso', max_length=100)
    #user = forms.fields.CharField(label='Usuario', max_length=100, widget=forms.TextInput(attrs={'placeholder':'Dejar en blanco para aplicar a todo el curso'}))
    monto = forms.fields.DecimalField(label='Monto', decimal_places=2, max_digits= 6)
    fecha_limite = forms.fields.DateField(label='Fecha Límite')
