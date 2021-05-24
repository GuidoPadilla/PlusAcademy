from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Pago
from .forms import PaymentRegisterForm

# Create your views here.
def control_view(request):
    pagos = Pago.objects.all()
    context = {
        'pagos': pagos
    }
    return render(request, 'pagos/control.html', context)

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