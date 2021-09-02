from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Curso, Moneda
from django.conf import settings

from datetime import datetime

# Create your models here.
class TipoPago(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class FormaPago(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class Cobro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_cobro = models.DateField(null = False)
    monto = models.FloatField(null = False)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    tipo_moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_pago.nombre + ' ' + self.fecha_cobro.strftime('%d/%m/%Y')
    def toDict(self):
        retDict = {
        'id': self.id,
        'user': self.user.username,
        'fecha_cobro':self.fecha_cobro.strftime('%d/%m/%Y'),
        'monto': self.monto,
        'tipo_pago': self.tipo_pago.nombre,
        'tipo_moneda': self.tipo_moneda.nombre
        }
        return retDict

class Pago(models.Model):
    fecha_pago = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    cobro = models.ForeignKey(Cobro, on_delete=models.CASCADE)
    #1 = Activo
    #0 = Eliminado
    #2 = En proceso de revision
    status = models.IntegerField(default = 1)

    def __str__(self):
        return 'Pago ' + self.user.username + ' Para Curso ' + self.codigo_curso.codigo + ' Tipo de Pago ' + self.cobro.tipo_pago.nombre + ' Cantidad Q' + str(self.cantidad) + ' Fecha ' + str(self.fecha_pago)
    def toDict (self):
        retDict ={
        'fecha_pago': self.fecha_pago.strftime('%d/%m/%Y'),
        'user': self.user.username,
        'userInfo': 'Nombre: ' + self.user.first_name + ' ' + self.user.last_name + ' - Código: ' + self.user.username,
        'id': self.id, 'cantidad': self.cantidad,
        'codigo_curso': self.codigo_curso.codigo,
        'moneda': self.moneda.nombre,
        'tipo_pago': self.cobro.tipo_pago.nombre,
        'forma_pago': self.forma_pago.nombre
        }
        return retDict
    
class EliminacionPagos(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    solicitadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    procesadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name='+')
    respuesta = models.IntegerField(default=None, null=True)
    fechaSolicitud = models.DateTimeField(auto_now_add=True)
    fechaRespuesta = models.DateTimeField(null=True, default=None)

    def toDict(self):
        retDict = {
        'id': self.id,
        'pago_user': self.pago.user.username,
        'userInfo': 'Nombre: ' + self.pago.user.first_name + ' ' + self.pago.user.last_name + ' - Código: ' + self.pago.user.username,
        'pago_codigo_curso': self.pago.codigo_curso.codigo,
        'fecha_pago_procesado': self.pago.fecha_pago.strftime('%d/%m/%Y'),
        'tipo_pago': self.pago.cobro.tipo_pago.nombre,
        'forma_pago': self.pago.forma_pago.nombre,
        'monto': self.pago.cantidad,
        'solicitado_por': self.solicitadoPor.username,
        'procesado_por': self.procesadoPor.username,
        'fecha_solicitud': self.fechaSolicitud.strftime('%d/%m/%Y'),
        'fecha_respuesta': self.fechaRespuesta.strftime('%d/%m/%Y')
        }
        return retDict

