
from django.forms import ModelForm, Form
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from pagos.models import Pago, Cobro, TipoPago, TipoGasto, Gasto
from usuarios.models import Moneda, Curso


class PaymentRegisterForm(ModelForm):

    class Meta:
        model = Pago
        fields = ['codigo_curso',  'user', 'cobro', 'forma_pago', 'moneda', 'cantidad']
    def __init__(self, *args, **kwrgs):
        super(PaymentRegisterForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')

class TipoGastoForm(ModelForm):
    class Meta:
        model = TipoGasto
        fields = ['nombre']

class GastoForm(Form):
    fecha_gasto = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    tipo_gasto = forms.ModelChoiceField(queryset=TipoGasto.objects.all())
    cantidad = forms.FloatField()

    class Meta:
        model = Gasto

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CobroExtraForm(Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    fecha_cobro = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    monto = forms.FloatField()
    tipo_pago = forms.ModelChoiceField(queryset=TipoPago.objects.all())
    tipo_moneda = forms.ModelChoiceField(queryset=Moneda.objects.all())
    class Meta:
        model = Cobro
        

    def __init__(self, *args, **kwrgs):
        super(CobroExtraForm, self).__init__(*args, **kwrgs)
        self.fields['user'].queryset = User.objects.filter(userextra__rol__nombre='estudiante')

class CobroExtraCursoForm(Form):
    Curso = forms.ModelChoiceField(queryset= Curso.objects.all())
    fecha_cobro = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    monto = forms.FloatField()
    tipo_pago = forms.ModelChoiceField(queryset=TipoPago.objects.all())
    tipo_moneda = forms.ModelChoiceField(queryset=Moneda.objects.all())

        

    def __init__(self, *args, **kwrgs):
        super(CobroExtraCursoForm, self).__init__(*args, **kwrgs)
