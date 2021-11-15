Feature: Ingreso de registros de pagos
	Scenario: Ingreso de pago de una cuota mensual de un estudiante 
		Given Los campos requeridos para un registro de pago
		When El usuario solicita ingresar el pago
		Then Se registra el nuevo pago en la base de datos
	Scenario: El administrador quiere poder ver los registros de pagos
		Given Los registros de pagos
		When El administrador selecciona la pestaña de control de pagos
		Then Se solicita al usuario filtrar los registros por el campo que desee
		And Se muestra la lista de pagos en base a los filtros establecidos.
	Scenario: Uno de los estudiantes ha realizado un pago con atraso 
		Given  La página de ingreso de registros de pagos
		When El usuario falló en cumplir con su pago mensual y ahora quiere pagar.
		Then Se solicita la misma información de cuando se hace un pago normal pero se aplica una mora o la penalización que se decida por el administrador.
		And: Se guarda el registro en la base de datos
	Scenario: Un estudiante falla en cumplir con múltiples pagos.
		Given La falta de registro de pagos de un estudiante en las cuotas
		When El usuario tiene cierta cantidad de mora
		Then Se suspende el ID del estudiante, se le notifica y se le restringe acceso a ciertos privilegios como clases o a exámenes
		And Si el problema persiste, se puede llegar a dar de baja al estudiante.
	Scenario: Se quiere realizar un pago de un libro de un estudiante
		Given La página de ingreso de registros de pagos 
		When El usuario solicita ingresar un pago de un libro 
		Then Se solicita al usuario ingresar los campos del registro de pago para el pago de un libro
		And Se guarda el registro en la base de datos
	Scenario: Se desea eliminar la informacion de un pago debido a una equivocación
		Given La página de visualización de pagos
		When El usuario que administra los pagos se equivocó al ingresar un pago al estudiante equivocado.
		Then Se da la opción de modificar los campos. En otra instancia se puede eliminar el pago
		And Se modifica el registro y se visualiza con los nuevos valores en la tabla
	Scenario: Se desea visualizar los pagos por estudiante de forma más específica
		Given La página de visualización de pagos por estudiante
		When Se requiere ver la información acerca de pagos de un estudiante de forma más detallada
		Then Se consulta por medio de código los pagos de un estudiante donde la información se puede visualizar de forma más detallada 
		And Se visualiza de forma resumida los datos de los estudiantes con detalles e información importante.
