from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from pagos.models import Pago

class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'tipo_pago', 'forma_pago', 'moneda', 'cantidad']