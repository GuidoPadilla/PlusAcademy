from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Curso
from django.conf import settings

from datetime import datetime

# Create your models here.
class TipoPago(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class Moneda(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class Pago(models.Model):
    fecha_pago = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    #1 = Activo
    #0 = Eliminado
    #2 = En proceso de revision
    status = models.IntegerField(default = 1)

    def __str__(self):
        return 'Pago ' + self.user.username
    def toDict (self):
        return {'fecha_pago': self.fecha_pago.strftime('%d/%m/%Y'), 'user': self.user.username, 'id': self.id, 'cantidad': self.cantidad, 'codigo_curso': self.codigo_curso.codigo, 'moneda': self.moneda.nombre, 'tipo_pago': self.tipo_pago.nombre}
    
class EliminacionPagos(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    solicitadoPor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    procesadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, related_name='+')
    respuesta = models.IntegerField(default=None, null=True)
    fecha = models.DateTimeField(auto_now_add=True)