const peticion = (path) => (
    $.ajax({
        url: path,
        type: "POST",
        dataType: "json",
        data: {
            content: "xxx",
            csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        success: (response) => {
            $('#data_body').html("")
            console.log(response)
            response.forEach(element => {
                let fila = '<tr>'
                for (key in element['fields']) {
                    fila += `<td>${element['fields'][key]}</td>`
                }
                fila += `<td><button>Editar</button><button>Eliminar</button></td>`
                fila += '</tr>'
                $('#data_body').append(fila)
            })
            /* $('data_table').DataTable({
                data: response,
                columns: [
                    {   data: "pagos.fields.user" },
                    {   data: "pagos.fields.fecha_pago" },
                    {   data: "pagos.fields.codigo_curso" },
                    {   data: "pagos.fields.tipo_pago" },
                    {   data: "pagos.fields.moneda" },
                    {   data: "pagos.fields.cantidad" }
                ],
            }) */
        },
        error: (response) => {
            console.log(response)
        }
    })
    /* $('#data_table').DataTable({
        processing: true,
        serverSide: true,
        ajax: {
            url: '/pagos/control/',
            type: 'POST',
            dataType: "json",
            data: {
                content: "xxx",
                csrfmiddlewaretoken: "{{ csrf_token }}",
            },
            
        },
        columns: [
                    {   data: "pagos.fields.user" },
                    {   data: "pagos.fields.fecha_pago" },
                    {   data: "pagos.fields.codigo_curso" },
                    {   data: "pagos.fields.tipo_pago" },
                    {   data: "pagos.fields.moneda" },
                    {   data: "pagos.fields.cantidad" }
                ],
    }) */
)