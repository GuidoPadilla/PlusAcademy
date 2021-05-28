from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Pago
from .forms import PaymentRegisterForm
from django.core.serializers import serialize
import json

# Create your views here.
def control_view(request):
    return render(request, 'pagos/control.html')

def pagos(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.get('params')
        if action == 'listaPagos':
            pagos = Pago.objects.all()
            if params:
                parametros = params.split(',')
                f_ini = parametros[0]
                f_fin = parametros[1]
                cod_usuario = parametros[2]
                if f_ini != '' and f_fin == '':
                    pagos = pagos.filter(fecha_pago__gte=f_ini)
                if f_fin != '' and f_ini == '':
                    pagos = pagos.filter(fecha_pago__lte=f_fin)
                if f_fin != '' and f_ini != '':
                    pagos = pagos.filter(fecha_pago__range=[f_ini,f_fin])
                if cod_usuario != '':
                    pagos = pagos.filter(user__username__contains=cod_usuario)
            return JsonResponse({"data":[x.toDict() for x in pagos]}, safe=False)
        else:
            response_data = {}
            response_data['result'] = 'ERROR'
            response_data['message'] = 'AUTH OR REQUEST METHOD ERROR'
            return HttpResponse(serialize('json', response_data), content_type='application/json')

def ingreso_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PaymentRegisterForm(request.POST)
            if form.is_valid():
                Pago.objects.create(**form.cleaned_data)
                return HttpResponseRedirect('')
        else:
            form = PaymentRegisterForm()
        context = {'form': form}
        return render(request, 'pagos/ingresar.html', context)
    else:
        return render(request, 'pagos/ingresar.html')