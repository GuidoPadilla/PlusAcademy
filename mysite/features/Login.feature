Feature: Login/logout

  Scenario: Ingresar a la pagina

		Given Un usuario anonimo
		When Envio datos inválidos a la página de login
		Then Soy redireccionado a la pantalla principal

		Given Un usuario anonimo
		When Envio datos inválidos a la página de login
		Then Soy redireccionado a una pantalla de fallo de login

	Scenario: Cerrar sesión

		Given Mi sesión como usuario de Plus Academy está iniciada
		When  Quiero cerrar sesión 
		Then  Debería recibir un mensaje de ¨Sesión cerrada exitosamente¨

		Given Mi sesión como usuario de Plus Academy está iniciada
		When  Cierro sesión de mi usuario
		And   Intento ingresar a https://plus-academy.herokuapp.com/pagos/control/ o cualquier otro URL compuesto de la aplicación
		Then	 La aplicación debería de redireccionarme a la página de inicio o presentar un error

