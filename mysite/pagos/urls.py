from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "pagos"

urlpatterns = [
    path('control/', views.control_view, name='pagos_control'),
    path('ingreso/', views.ingreso_view, name='pagos_ingreso'),
]