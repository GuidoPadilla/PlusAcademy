from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def control_view(request):
    return render(request, 'pagos/control.html')

def ingreso_view(request):
    return render(request, 'pagos/ingresar.html')