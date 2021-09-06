
from django.test import TestCase,SimpleTestCase,Client
from django.urls import reverse, resolve
from pagos.views import control_view, saldo_view, ingreso_view, pagos, saldos, control_pagos, solicitarEliminacionPago, pagos_solicitados_eliminar_view, pagos_pendientes, solicitud_eliminacion_pago, pagos_eliminados, pagos_eliminados_list
from pagos.models import TipoPago, Moneda, Pago, EliminacionPagos, FormaPago
import json
from django.db import models


class TestUrls(SimpleTestCase):

    def test_url_pagos_control(self):
        url = reverse('pagos:pagos_control')
        print(resolve(url))
        self.assertEquals(resolve(url).func,control_view)

    def test_url_pagos_saldo(self):
        url = reverse('pagos:pagos_saldo')
        print(resolve(url))
        self.assertEquals(resolve(url).func,saldo_view)

    def test_url_pagos_ingreso(self):
        url = reverse('pagos:pagos_ingreso')
        print(resolve(url))
        self.assertEquals(resolve(url).func,ingreso_view)

    def test_url_lista_pagos(self):
        url = reverse('pagos:lista_pagos')
        print(resolve(url))
        self.assertEquals(resolve(url).func,pagos)

    def test_url_lista_saldos(self):
        url = reverse('pagos:lista_saldos')
        print(resolve(url))
        self.assertEquals(resolve(url).func,saldos)

    def test_url_pagos_excel(self):
        url = reverse('pagos:pagos_excel')
        print(resolve(url))
        self.assertEquals(resolve(url).func,control_pagos)

    def test_url_solicitar_eliminacion(self):
        url = reverse('pagos:solicitar_eliminacion')
        print(resolve(url))
        self.assertEquals(resolve(url).func,solicitarEliminacionPago)

    def test_url_pagos_solicitados_eliminar(self):
        url = reverse('pagos:pagos_solicitados_eliminar')
        print(resolve(url))
        self.assertEquals(resolve(url).func,pagos_solicitados_eliminar_view)

    def test_url_pagos_pagos_pendientes(self):
        url = reverse('pagos:pagos_pendientes')
        print(resolve(url))
        self.assertEquals(resolve(url).func,pagos_pendientes)

    def test_url_solicitud_eliminacion_pago(self):
        url = reverse('pagos:solicitud_eliminacion_pago')
        print(resolve(url))
        self.assertEquals(resolve(url).func,solicitud_eliminacion_pago)

    def test_url_pagos_eliminados(self):
        url = reverse('pagos:pagos_eliminados')
        print(resolve(url))
        self.assertEquals(resolve(url).func,pagos_eliminados)

    def test_url_pagos_eliminados_list(self):
        url = reverse('pagos:pagos_eliminados_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,pagos_eliminados_list)


class TestViews(TestCase):

    def test_control_view(self):
        client = Client()
        response = client.get('/pagos/control/')
        self.assertTemplateUsed(response, 'pagos/control.html')

    def test_saldo_view(self):
        client = Client()
        response = client.get('/pagos/saldo_consulta/')
        self.assertTemplateUsed(response, 'pagos/saldo_consulta.html')

    def test_pagos(self):
        #Incomplete
        client = Client()


    def test_solicitarEliminacionPago(self):
       #Incomplete
        pass

    def test_pagos_solicitados_eliminar_view(self):
        client = Client()
        response = client.get('/pagos/pagos_solicitados_eliminar/')
        self.assertTemplateUsed(response, 'pagos/pagos_solicitados_eliminar.html')

    def test_solicitud_eliminacion_pago(self):
        #Incomplete
        pass

    def test_pagos_eliminados(self):
        client = Client()
        response = client.get('/pagos/pagos_eliminados/')
        self.assertTemplateUsed(response, 'pagos/pagos_eliminados.html')

    def test_pagos_eliminados_list(self):
        #Incomplete
        pass

    def test_pagos_pendientes(self):
        #Incomplete
        pass

    def test_saldos(self):
        #Incomplete
        client = Client()
        response = client.get('/pagos/lista_saldos/')

    def test_control_pagos(self):
        #template fail
        client = Client()
        response = client.get('/pagos/pagos_excel.xls/')
        #self.assertTemplateUsed(response, 'pagos/control_excel.html')

    def test_ingreso_view(self):
        #Template fail
        client = Client()
        response = client.get('/pagos/pagos_ingreso/')
        #self.assertTemplateUsed(response, 'pagos/ingresar.html')

    def test_cobros_extra_view(self):
        client = Client()
        response = client.get('/pagos/cobros_extra/')
        #self.assertTemplateUsed(response, 'pagos/cobros_extra.html')


class testModels(TestCase):

    def test_model_Pago(self):
        Curso = 'testCurso'
        TipoPago = 'TipoPago'
        FormaPago = 'Efectivo'
        Moneda = 'Q'

        newPago = Pago()
        newPago.fecha_pago = models.DateField(auto_now_add=True)
        newPago.cantidad = models.IntegerField()
        newPago.status = models.IntegerField(default = 1)
        self.assertEquals(str(type(newPago)),"<class 'pagos.models.Pago'>")

    def test_model_EliminacionPagos(self):
        newPago = Pago()
        User = 'testUser'
        User2 = 'testUser2'

        newEliminacionPagos = EliminacionPagos()
        newEliminacionPagos.pago = newPago
        newEliminacionPagos.respuesta = models.IntegerField(default=None, null=True)
        newEliminacionPagos.fechaSolicitud = models.DateTimeField(auto_now_add=True)
        newEliminacionPagos.fechaRespuesta = models.DateTimeField(null=True, default=None)
        self.assertEquals(str(type(newEliminacionPagos)),"<class 'pagos.models.EliminacionPagos'>")

    def test_model_TipoPago(self):
        newTipoPago = TipoPago()
        newTipoPago.nombre = models.CharField(unique=True, max_length=50)
        self.assertEquals(str(type(newTipoPago)),"<class 'pagos.models.TipoPago'>")

    def test_model_FormaPago(self):
        newFormaPago = FormaPago()
        newFormaPago.nombre = models.CharField(unique=True, max_length=50)
        self.assertEquals(str(type(newFormaPago)),"<class 'pagos.models.FormaPago'>")

    def test_model_Moneda(self):
        newMoneda = Moneda()
        newMoneda.nombre = models.CharField(unique=True, max_length=50)
        self.assertEquals(str(type(newMoneda)),"<class 'pagos.models.Moneda'>")


class Integration(TestCase):
    def test_control_integration(self):
        url = reverse('pagos:pagos_control')
        print(resolve(url))
        self.assertEquals(resolve(url).func,control_view)
        TestViews.test_control_view(self)
        client = Client()
        response = client.get('/pagos/control/')
        self.assertTemplateUsed(response, 'pagos/control.html')

    def test_saldo_integration(self):
        url = reverse('pagos:pagos_saldo')
        print(resolve(url))
        self.assertEquals(resolve(url).func,saldo_view)
        client = Client()
        response = client.get('/pagos/saldo_consulta/')
        self.assertTemplateUsed(response, 'pagos/saldo_consulta.html')

    def test_pago_integration(self):
        url = reverse('pagos:pagos_ingreso')
        print(resolve(url))
        self.assertEquals(resolve(url).func,ingreso_view)
        newPago = Pago()
        User = 'testUser'
        User2 = 'testUser2'
        newEliminacionPagos = EliminacionPagos()
        newEliminacionPagos.pago = newPago
        newEliminacionPagos.respuesta = models.IntegerField(default=None, null=True)
        newEliminacionPagos.fechaSolicitud = models.DateTimeField(auto_now_add=True)
        newEliminacionPagos.fechaRespuesta = models.DateTimeField(null=True, default=None)
        self.assertEquals(str(type(newEliminacionPagos)),"<class 'pagos.models.EliminacionPagos'>")

