from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationAddForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
                    return HttpResponseRedirect('../../usuarios/prueba/')
        else:
            form = AuthenticationAddForm()
        context = {'form': form}
        return render(request, 'usuarios/login.html', context)
    else:
        return HttpResponseRedirect('../../usuarios/prueba/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('../../usuarios/login/')

def prueba_view(request):
    return render(request, 'usuarios/prueba.html')