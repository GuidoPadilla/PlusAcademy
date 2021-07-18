from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "pagos"

urlpatterns = [
    path('control/', views.control_view, name='pagos_control'),
    path('saldo_consulta/', views.saldo_view, name='pagos_saldo'),
    path('ingreso/', views.ingreso_view, name='pagos_ingreso'),
    path('pagos/', views.pagos, name='lista_pagos'),
    path('saldos/', views.saldos, name='lista_saldos'),
    path('pagos_excel.xls', views.control_pagos, name='pagos_excel'),
    path('solicitar_eliminacion/', views.solicitarEliminacionPago, name='solicitar_eliminacion'),
    path('pagos_solicitados_eliminar/', views.pagos_solicitados_eliminar_view, name='pagos_solicitados_eliminar'),
    path('pagos_pendientes/', views.pagos_pendientes, name='pagos_pendientes'),
    path('solicitud_eliminacion_pago/', views.solicitud_eliminacion_pago, name='solicitud_eliminacion_pago'),
    path('pagos_eliminados/', views.pagos_eliminados, name='pagos_eliminados'),
    path('pagos_eliminados_list/', views.pagos_eliminados_list, name='pagos_eliminados_list'),
]