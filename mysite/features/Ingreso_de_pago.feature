Feature: Ingreso de registros de pagos
	Scenario: Ingreso de pago de una cuota mensual de un estudiante 
		Given: La página de ingreso de registros de pagos 
		When: El usuario solicita ingresar un pago de cuota mensual de un estudiante
		Then: Se solicita al usuario ingresar “ID de estudiante” , “Nombre del estudiante”, “apellido del estudiante”, “monto”, “fecha de pago”, “forma de pago”, “tipo de pago”
		And: Se guarda el registro en la base de datos
	Scenario: Visualizar los pagos de los estudiantes
		Given: La página de visualización de pagos
		When: El usuario administrador solicita visualizar la lista de pagos de los estudiantes
		Then: Se solicita al usuario filtrar de acuerdo a sus intereses (fecha, nombre de estudiante, tipo de pago, etc.)
		And: Se muestra la lista de pagos en base a los filtros establecidos.
	Scenario: Realizar un pago con atraso
		Given:  La página de ingreso de registros de pagos
		When: El usuario falló en cumplir con su pago mensual y ahora quiere pagar.
		Then: Se solicita la misma información de cuando se hace un pago normal pero se aplica una mora o la penalización que se decida por el administrador.
		And: Se guarda el registro en la base de datos
	Scenario: Un estudiante falla en cumplir con múltiples pagos.
		Given: La página de visualización de pagos
		When: El usuario lleva repetidas veces sin pagar su mensualidad debida.
		Then: Se suspende el ID del estudiante, se le notifica y se le restringe acceso a ciertos privilegios como clases o a exámenes. (Puede variar la penalización a elección del administrador.)
		And: Si el problema persiste, se puede llegar a dar de baja al estudiante.
	Scenario: Se quiere realizar un pago de un libro de un estudiante
		Given: La página de ingreso de registros de pagos 
		When: El usuario solicita ingresar un pago de un libro 
		Then: Se solicita al usuario ingresar “ID de estudiante” , “Nombre del estudiante”, “apellido del estudiante”, “monto”, “fecha de pago”, “forma de pago”, “tipo de pago”
		And: Se guarda el registro en la base de datos
	Scenario: Se desea cambiar la informacion de un pago debido a una equivocación
		Given: La página de visualización de pagos
		When: El usuario que administra los pagos se equivocó al ingresar un pago al estudiante equivocado.
		Then: Se da la opción de modificar la fecha del campo, el código del estudiante, la cantidad, etc. En otra instancia se puede eliminar el pago
		And: Se modifica el registro y se visualiza con los nuevos valores en la tabla
	Scenario: Se desea visualizar los pagos por estudiante de forma más específica
		Given: La página de visualización de pagos por estudiante
		When: Se requiere ver la información acerca de pagos de un estudiante de forma más detallada
		Then: Se consulta por medio de código los pagos de un estudiante donde la información se puede visualizar de forma más detallada con moras, cantidad, etc.
		And: Se visualiza de forma resumida los datos de los estudiantes con detalles e información importante.
