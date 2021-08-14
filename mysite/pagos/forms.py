from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from pagos.models import Pago

class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'tipo_pago', 'forma_pago', 'moneda', 'cantidad']

class CobroExtraForm(forms.Form):
    codigo_curso = forms.fields.CharField(label='Código de Curso', max_length=100)
    monto = forms.fields.DecimalField(label='Monto', decimal_places=2, max_digits= 6)
    fecha_limite = forms.fields.DateField(label='Fecha Límite')
