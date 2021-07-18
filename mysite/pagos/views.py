from datetime import datetime
from datetime import date
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Pago, EliminacionPagos
from usuarios.models import LlevaCurso
from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from .forms import PaymentRegisterForm
from django.core.serializers import serialize
import json

# Create your views here.
def control_view(request):
    return render(request, 'pagos/control.html')

def saldo_view(request):
    return render(request, 'pagos/saldo_consulta.html')

def pagos(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.get('params')
        if action == 'listaPagos':
            pagos = Pago.objects.filter(status=1)
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

def solicitarEliminacionPago(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        id_pago = json.loads(request.POST.get('pagos_data')).get('pago_id')
        if action == 'pagoEliminacion':
            pago = Pago.objects.filter(id=id_pago)
            pago = pago.first()
            pago.status = 2
            pago.save()
            pagosExistentes = EliminacionPagos.objects.filter(pago=id_pago)
            if not pagosExistentes:
                EliminacionPagos.objects.create(pago=pago, solicitadoPor=request.user, respuesta=None)
            else:
                pagosExistentes.delete()
                EliminacionPagos.objects.create(pago=pago, solicitadoPor=request.user, respuesta=None)
            response_data = {}
            response_data['result'] = 'CONFIRMADO'
            return JsonResponse(response_data)

def pagos_solicitados_eliminar_view(request):
    return render(request, 'pagos/pagos_solicitados_eliminar.html')

def solicitud_eliminacion_pago(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        id_pago = json.loads(request.POST.get('pagos_data')).get('pago_id')
        if action == 'aceptarSolicitudEliminacionPago':
            # pago = Pago.objects.filter(id=id_pago)
            # pago.update(status=0)
            pago = Pago.objects.filter(id=id_pago)
            pago = pago.first()
            pago.status = 0
            pago.save()
            eliminacionPago = EliminacionPagos.objects.filter(pago=id_pago)

            eliminacionPago = eliminacionPago.first()
            print(eliminacionPago)
            eliminacionPago.procesadoPor = request.user
            eliminacionPago.respuesta = 0
            eliminacionPago.save()
            response_data = {}
            response_data['result'] = 'CONFIRMADA SOLICITUD DE ELIMINACION DEL PAGO'
            return JsonResponse(response_data)
        elif action == 'rechazarSolicitudEliminacionPago':
            pago = Pago.objects.filter(id=id_pago)
            pago = pago.first()
            pago.status = 1
            pago.save()
            eliminacionPago = EliminacionPagos.objects.filter(pago=id_pago)
            eliminacionPago = eliminacionPago.first()
            eliminacionPago.procesadoPor = request.user
            eliminacionPago.respuesta = 1
            eliminacionPago.save()
            response_data = {}
            response_data['result'] = 'RECHAZADA SOLICITUD DE ELIMINACION DEL PAGO'
            return JsonResponse(response_data)
    else:
        response_data = {}
        response_data['result'] = 'ERROR'
        response_data['message'] = 'AUTH OR REQUEST METHOD ERROR'
        return HttpResponse(serialize('json', response_data), content_type='application/json')  

def pagos_eliminados(request):
    return render(request, 'pagos/pagos_eliminados.html')

def pagos_eliminados_list(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.get('params')
        if action == 'listaPagos':
            pagos = Pago.objects.filter(status=0)
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

def pagos_pendientes(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.get('params')
        if action == 'listaPagos':
            pagos = Pago.objects.filter(status=2)
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


def saldos(request):
    if request.is_ajax() and request.method == 'POST':
        action = request.POST.get('action')
        params = request.POST.get('params')
        if action == 'listaSaldos':
            cursosLlevados = LlevaCurso.objects.all()
            pagos = Pago.objects.all()
            hoy = date.today()
            for cursoLlevado in cursosLlevados:
                lista = []
                pagos_usuario = pagos.filter(user__username=cursoLlevado.user.username)
                pagos_usuario = pagos_usuario.filter(codigo_curso__codigo=cursoLlevado.curso.codigo)
                total_inscripcion = pagos_usuario.filter(tipo_pago__nombre='Inscripcion').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
                pagos_inscripcion = cursoLlevado.curso.inscripcion- total_inscripcion
                if pagos_inscripcion != 0:
                    fecha_inscripcion = cursoLlevado.fecha_llevado + relativedelta(months=1)
                    if  hoy > fecha_inscripcion:
                        lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                        , 'desc_pag': 'Mora de Inscripcion', 'fecha_pago': fecha_inscripcion, 'tipo_pago': 'Vencido (Pagar lo antes posible)','cantidad': 50
                        , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
                        lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                        , 'desc_pag': 'Inscripcion', 'fecha_pago': fecha_inscripcion, 'tipo_pago': 'Vencido (Pagar lo antes posible)'
                        ,'cantidad': cursoLlevado.curso.inscripcion
                        , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
                    else: 
                        lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                        , 'desc_pag': 'Inscripcion', 'fecha_pago': fecha_inscripcion, 'tipo_pago': 'Por Vencer'
                        ,'cantidad': cursoLlevado.curso.inscripcion
                        , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
                total_cuota = pagos_usuario.filter(tipo_pago__nombre='Cuota').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
                pagos_cuota = cursoLlevado.curso.cuota*cursoLlevado.curso.duracion - total_cuota
                if pagos_cuota != 0:
                    faltan = pagos_cuota/cursoLlevado.curso.cuota
                    llevados = cursoLlevado.curso.duracion - faltan
                    fecha_cuota = hoy
                    for i in range(int(faltan)):
                        fecha_cuota = cursoLlevado.fecha_llevado + relativedelta(months=llevados+i+1)
                        if  hoy > fecha_cuota:
                            lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                            , 'desc_pag': 'Mora de Cuota', 'fecha_pago': fecha_cuota, 'tipo_pago': 'Vencido (Pagar lo antes posible)','cantidad': 50
                            , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
                            lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                            , 'desc_pag': 'Cuota', 'fecha_pago': fecha_cuota, 'tipo_pago': 'Vencido (Pagar lo antes posible)'
                            ,'cantidad': cursoLlevado.curso.cuota
                            , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
                        else: 
                            lista.append({'desc_est': 'codigo: ' + cursoLlevado.user.username + ', curso: ' + cursoLlevado.curso.codigo 
                            , 'desc_pag': 'Cuota', 'fecha_pago': fecha_cuota, 'tipo_pago': 'Por Vencer'
                            ,'cantidad': cursoLlevado.curso.cuota
                            , 'codigo': cursoLlevado.user.username, 'curso': cursoLlevado.curso.codigo})
            return JsonResponse({"data":lista}, safe=False)
        else:
            response_data = {}
            response_data['result'] = 'ERROR'
            response_data['message'] = 'AUTH OR REQUEST METHOD ERROR'
            return HttpResponse(serialize('json', response_data), content_type='application/json')
            
def control_pagos(request):
    pagos = Pago.objects.all()
    context = {
        'pagos': pagos
    }
    return render(request, 'pagos/control_excel.html', context)

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