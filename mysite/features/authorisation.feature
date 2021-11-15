
Feature: Autorización y control de acceso
   Verificar que se aplique el modelo de control de acceso para que solo los usuarios autorizados tengan acceso a sus propios datos

  Scenario: Los usuarios pueden ver los recursos restringidos para los que están autorizados
    Given un nuevo navegador o instancia de cliente
    And el cliente / navegador está configurado para utilizar un proxy de interceptación
    And la pagina de login
    And un username autorizado es utilizado
    And una contraseña autorizada es utilizada
    When el usuario inicia sesión
    And los logs del proxy estan limpios 
    And los HTTP requests y responses son grabados
    And acceden a un recurso restringido
    Then La data sensible deberia ser presentada en una respuesta HTTP

  Scenario: Los usuarios no deben poder ver los recursos para los que no están autorizados
    Given Se ha completado el mapa de control de acceso para usuarios autorizados
    And un nuevo navegador o instancia de cliente
    And un username autorizado es utilizado
    And una contraseña autorizada es utilizada
    And la pagina de login
    When el usuario inicia sesión
    And las solicitudes HTTP previamente grabadas se reproducen utilizando el ID de sesión actual
    Then la información requerida no debe estar presente en ninguna de las respuestas HTTP

  Scenario Outline: Los usuarios no autenticados no deberían poder ver los recursos restringidos
    Given Se ha completado el mapa de control de acceso para usuarios autorizados
    And un nuevo navegador o instancia de cliente
    And la pagina de login
    When las solicitudes HTTP previamente grabadas se reproducen utilizando el ID de sesión actual
    Then la información requerida no debe estar presente en ninguna de las respuestas HTTP

    