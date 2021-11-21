"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "usuarios"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.view_login, name='login_view'),
    path('logout/', views.logout_user, name='logout'),
    path('create-operativo/', views.view_createuser, name='createuser_view'),
    path('create-student/', views.view_createstudent, name='createstudent_view'),
    path('control/', views.view_usuarios, name='usuarios_listado'),
    path('usuarios/', views.lista_usuarios, name='lista_estudiante'),
    path('create_curso/', views.view_creatcurso, name='create_curso'),
    path('asignar_curso/', views.view_createasignacion, name='asignar_curso'),
    path('definir_nivel_academico/', views.definicion_nivel_academico_view, name='definir_nivel_academico'),
]
