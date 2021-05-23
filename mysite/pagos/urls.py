from django.contrib import admin
from django.urls import path, include
from . import views
from . import ajax_datatable_views
app_name = "pagos"

urlpatterns = [
    path('control/', views.control_view, name='pagos_control'),
    path('ingreso/', views.ingreso_view, name='pagos_ingreso'),
    path('ajax_datatable/pagos/', ajax_datatable_views.PagosAjaxDatatableView.as_view(), name="ajax_datatable_pagos"),
]