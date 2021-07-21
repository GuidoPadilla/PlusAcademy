
from django.test import TestCase,SimpleTestCase
from django.urls import reverse, resolve
from pagos.views import control_view, saldo_view, ingreso_view, pagos, saldos, control_pagos, solicitarEliminacionPago, pagos_solicitados_eliminar_view, pagos_pendientes, solicitud_eliminacion_pago, pagos_eliminados, pagos_eliminados_list

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