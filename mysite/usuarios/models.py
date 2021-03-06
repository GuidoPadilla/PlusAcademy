from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Moneda(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre
class Nacionalidad(models.Model):
    nombre = models.CharField(unique=True, max_length=50)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ', moneda: ' + self.moneda.nombre
    def natural_key(self):
        return self.nombre

# Create your models here.
class NivelAcademico(models.Model):
    nombre = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=False, max_length=50)
    inscripcion_quetzales = models.FloatField(default = 500.00)
    cuota_quetzales = models.FloatField(default = 1000.00)
    inscripcion_dolares = models.FloatField(default = 500.00)
    cuota_dolares = models.FloatField(default = 1000.00)
    duracion = models.IntegerField(default = 5)
    
    def __str__(self):
        return self.codigo
    def natural_key(self):
        return self.codigo

class Sexo(models.Model):
    nombre = models.CharField(unique=True, max_length=25)
    
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class Rol(models.Model):
    codigo = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=True, max_length=25)
    def __str__(self):
        return self.nombre
    def natural_key(self):
        return self.nombre

class ImparteCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_impartido = models.DateField()

class LlevaCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_llevado = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','curso'], name='llevar el curso una vez')    
        ]

class ConteoAnualEstudiantes(models.Model):
    id = models.AutoField(primary_key=True)

        
class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dpi = models.CharField(unique=True, max_length=13)
    telefono = models.CharField(unique=False, max_length=15)
    direccion = models.CharField(unique=False, max_length=500)
    fecha_nacimiento = models.DateField()
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    def toDict (self):
        return {
            'codigo':self.user.username,
            'nombres': self.user.first_name+' ' +self.user.last_name,
            'correo': self.user.email,
            'dpi': self.dpi,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'edad': str(int(datetime.today().strftime('%Y'))-int(self.fecha_nacimiento.strftime('%Y'))),
            'fecha_nacimiento': self.fecha_nacimiento.strftime('%d/%m/%Y'),
            'sexo': self.sexo.nombre,
            'rol': self.rol.nombre,
            'date_joined': self.user.date_joined.strftime('%d/%m/%Y'),
            'nacionalidad': self.nacionalidad.nombre
        }
