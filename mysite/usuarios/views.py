from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationAddForm, UserRegisterForm, UserExtraRegisterForm, LlevaCursoRegisterForm, CursoRegisterForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Curso, UserExtra, LlevaCurso
from pagos.models import Cobro, Moneda, TipoPago
from django.db import connection
from django.core.serializers import serialize
import datetime
from dateutil.relativedelta import relativedelta

def view_login(request):
    if request.user.is_authenticated != True:
        if request.method == "POST":
            form = AuthenticationAddForm(request.POST)

            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('../../pagos/control/')
        else:
            form = AuthenticationAddForm()
        context = {'form': form}
        return render(request, 'usuarios/login.html', context)
    else:
        return HttpResponseRedirect('../../pagos/control/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('../../usuarios/login/')

def lista_usuarios(request):
    if request.is_ajax() and request.method == 'POST':
        users = UserExtra.objects.all()
        users = users.filter(rol__nombre='estudiante')
        return JsonResponse({"data":[x.toDict() for x in users]}, safe=False) 

def view_createuser(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form1 = UserRegisterForm(request.POST)
            form2 = UserExtraRegisterForm(request.POST)
            if form1.is_valid():
                if form2.is_valid():
                    """ form1.cleaned_data['username'] = codigo """
                    new_user = User.objects.create_user(**form1.cleaned_data)
                    UserExtra.objects.create(user=new_user, **form2.cleaned_data)
                    return HttpResponseRedirect('../control/')

        else:
            form1 = UserRegisterForm()
            form2 = UserExtraRegisterForm()
        context = {'form1': form1, 'form2': form2}
        return render(request, 'usuarios/create_user.html', context)
    else:
        return HttpResponseRedirect('../usuarios/login/')

def view_creatcurso(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form1 = CursoRegisterForm(request.POST)
            if form1.is_valid():
                new_curso = Curso.objects.create(**form1.cleaned_data)
                return HttpResponseRedirect('../create_curso/')
        else:
            form1 = CursoRegisterForm()
        context = {'form1': form1}
        return render(request, 'usuarios/create_curso.html', context)
    else:
        return HttpResponseRedirect('../usuarios/login/')

#Arreglar con el nuevo modelo de cobros y curso
def view_createasignacion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form1 = LlevaCursoRegisterForm(request.POST)
            if form1.is_valid():
                user = form1.cleaned_data['user']
                user = User.objects.get(username=user)
                fecha_llevado = form1.cleaned_data['fecha_llevado']
                curso = Curso.objects.get(codigo = form1.cleaned_data['curso'])
                inscripcion_quetzales = curso.inscripcion_quetzales
                inscripcion_dolares = curso.inscripcion_dolares
                cuota_quetzales  = curso.cuota_quetzales
                cuota_dolares  = curso.cuota_dolares
                monto_inscripcion = inscripcion_quetzales if user.userextra.nacionalidad.nombre == 'Guatemala' else inscripcion_dolares
                monto_cuota = cuota_quetzales if user.userextra.nacionalidad.nombre == 'Guatemala' else cuota_dolares
                moneda = Moneda.objects.get(nombre = 'Quetzal') if user.userextra.nacionalidad.moneda.nombre == 'Quetzal' else Moneda.objects.get(nombre = 'Dolar')
                duracion = curso.duracion
                fecha_inscripcion = fecha_llevado + relativedelta(months=1)
                Cobro.objects.create(user=user, fecha_cobro = fecha_inscripcion, monto = monto_inscripcion, tipo_pago = TipoPago.objects.get(nombre = 'Inscripcion'), tipo_moneda = moneda)
                for i in range(duracion):
                    fecha_cuota  = fecha_llevado + relativedelta(months=1+i)
                    Cobro.objects.create(user=user, fecha_cobro = fecha_cuota, monto = monto_cuota, tipo_pago = TipoPago.objects.get(nombre = 'Cuota'), tipo_moneda = moneda)
                LlevaCurso.objects.create(**form1.cleaned_data)
                return HttpResponseRedirect('../asignar_curso/')
        else:
            form1 = LlevaCursoRegisterForm()
        context = {'form1': form1}
        return render(request, 'usuarios/asignar_curso.html', context)
    else:
        return HttpResponseRedirect('../usuarios/login/')

def view_usuarios(request):
    return render(request, 'usuarios/control.html')