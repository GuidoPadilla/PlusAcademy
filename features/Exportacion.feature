Feature: Exportación de datos de pago 
        Scenario: Se desean generar archivos de excel que contengan la información de                 los pagos realizados
                Given: La sección de control de pagos
                When: Se requiere generar un archivo de excel con la información presentada en la sección de pagos
                Then: Se seleccionan las fechas de las cuales se quiere obtener el reporte 
                And: Se genera un archivo de excel con la información de pagos de las fechas seleccionadas
        Scenario: Se desea, como administrador,  ver las solicitudes de eliminación de pagos o modificación de información
                Given: La página de visualización de pagos.
                When: El administrador tiene las opciones de aceptar o rechazar la solicitud. Selecciona una de las dos.
                Then: Se realiza el cambio y se guarda en un historial quien lo realizó y un timestamp.
                And: Se notifica al estudiante del estado de su solicitud.
        Scenario: Se desea, como administrador,  agregar la foto de la confirmación de la boleta
                Given :La sección de control de pagos
                When: El administrador desea agregar la foto de confirmación de boleta
                Then: Se agrega la foto en el espacio designado
                And: Se guarda la información del pago junto con la foto de confirmación