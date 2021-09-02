from django.forms import ModelForm
from django.contrib.auth.models import User
from pagos.models import Pago, Cobro

class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'cobro', 'forma_pago', 'moneda', 'cantidad']
    def __init__(self, *args, **kwrgs):
        super(PaymentRegisterForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')




class CobroExtraForm(ModelForm):
    class Meta:
        model = Cobro
        fields = ['user', 'fecha_cobro', 'monto', 'tipo_pago', 'tipo_moneda']
        

    def __init__(self, *args, **kwrgs):
        super(CobroExtraForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')
