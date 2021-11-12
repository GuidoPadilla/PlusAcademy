Feature: Login form

  Scenario: Ingresar a la pagina

	Given: Un usuario anonimo
	When: Envio datos inválidos a la página de login
	Then: Soy redireccionado a la pantalla principal

	Given: Un usuario anonimo
	When: Envio datos inválidos a la página de login
	Then: Soy redireccionado a una pantalla de fallo de login