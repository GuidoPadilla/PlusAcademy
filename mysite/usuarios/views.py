from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationAddForm, UserRegisterForm, UserExtraRegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from usuarios.models import UserExtra
from django.db import connection
import datetime

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

def view_createuser(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form1 = UserRegisterForm(request.POST)
            form2 = UserExtraRegisterForm(request.POST)
            now = datetime.datetime.now()
            currYear = '{:02d}'.format(now.year)
            currYear = currYear[2:4]
            lastname = request.POST['last_name']
            lastname = lastname[0:3].lower()
            
            cursor = connection.cursor() 
            contadorUsuariosAnual = 'Select count(*) from auth_user where strftime(\''+'%Y'+'\', date_joined) = strftime(\''+'%Y'+'\', \''+'now'+'\')'
            print(contadorUsuariosAnual)
            cursor.execute(contadorUsuariosAnual)
            resultado = cursor.fetchall()
            print(resultado)
            resultado = int(list(resultado[0])[0])+1

            # print(resultado)
            # resultado = resultado+1
            resultado = str(resultado).zfill(3)

            codigo = lastname+currYear+resultado
            if form1.is_valid():
                if form2.is_valid():
                    form1.cleaned_data['username'] = codigo
                    print(form2.cleaned_data['fecha_nacimiento'])
                    new_user = User.objects.create_user(**form1.cleaned_data)
                    UserExtra.objects.create(user=new_user, **form2.cleaned_data)
                    return HttpResponseRedirect('')

        else:
            form1 = UserRegisterForm()
            form2 = UserExtraRegisterForm()
        context = {'form1': form1, 'form2': form2}
        return render(request, 'usuarios/create_user.html', context)
    else:
        return HttpResponseRedirect('../usuarios/login/')

def view_usuarios(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/control.html', context)