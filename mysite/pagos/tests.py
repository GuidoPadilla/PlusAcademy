
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
			