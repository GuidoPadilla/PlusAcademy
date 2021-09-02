from django.forms import ModelForm, Form
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from pagos.models import Pago, Cobro, TipoPago
from usuarios.models import Moneda

class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'cobro', 'forma_pago', 'moneda', 'cantidad']
    def __init__(self, *args, **kwrgs):
        super(PaymentRegisterForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')




class CobroExtraForm(Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    fecha_cobro = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    monto = forms.FloatField()
    tipo_pago = forms.ModelChoiceField(queryset=TipoPago.objects.all())
    tipo_moneda = forms.ModelChoiceField(queryset=Moneda.objects.all())
    class Meta:
        model = Cobro
        # fields = ['user', 'fecha_cobro', 'monto', 'tipo_pago', 'tipo_moneda']
        

    def __init__(self, *args, **kwrgs):
        super(CobroExtraForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')
