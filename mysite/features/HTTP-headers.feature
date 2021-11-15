Feature: configuración de seguridad en encabezados HTTP
  Verifique que los encabezados HTTP protejan adecuadamente los datos de los atacantes

  Fondo:
    Given un nuevo navegador o instancia de cliente
    When se visitan las siguientes URL y se registran sus respuestas HTTP
      | https://plus-academy.herokuapp.com/ |

  Scenario: Restrinja a otros sitios para que no lo coloquen en un iframe para evitar ataques de ClickJacking
    Then el encabezado X-Frame-Options es SAMEORIGIN o DENY

  Scenario: vuelva a habilitar la protección integrada del navegador Cross Site Scriping
    Then el encabezado HTTP X-XSS-Protection tiene el valor: 1; modo = bloquear

  Scenario: Forzar el uso de HTTPS para la URL segura base
    Then se establece el encabezado Strict-Transport-Security

  Scenario: restringir las solicitudes de dominio cruzado HTML5 solo a hosts de confianza
    Then el encabezado Access-Control-Allow-Origin no debe ser: *

  Scenario: habilitar la prevención de rastreo anti-MIME en los navegadores
    Then el encabezado HTTP X-Content-Type-Options tiene el valor: nosniff

    