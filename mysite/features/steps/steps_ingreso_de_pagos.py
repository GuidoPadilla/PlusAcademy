from behave import *
import models


@given('Los campos requeridos para un registro de pago')
def step_impl(context, fecha_pago, user, codigo_curso, tipo_pago, forma_pago, cantidad, moneda,status):
	context.Pago.fecha_pago = fecha_pago
	context.Pago.user = user
	context.Pago.codigo_curso = codigo_curso
	context.Pago.tipo_pago = tipo_pago
	context.Pago.forma_pago = forma_pago
	context.Pago.cantidad = cantidad
	context.Pago.moneda = moneda
	context.Pago.status = 1

@when('El usuario solicita ingresar el pago')
def step_impl(context,Pago):
    context.Pago.toDict()

@then('Se registra el nuevo pago en la base de datos')
def step_impl(context):
	context.ingreso_view()