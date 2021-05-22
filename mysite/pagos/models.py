from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Curso

# Create your models here.
class TipoPago(models.Model):
    nombre = models.CharField(unique=True, max_length=50)

class Moneda(models.Model):
    nombre = models.CharField(unique=True, max_length=50)

class Pago(models.Model):
    fecha_pago = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo_pago= models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
