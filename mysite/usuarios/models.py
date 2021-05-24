from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NivelAcademico(models.Model):
    nombre = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    codigo = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=False, max_length=50)
    
    def __str__(self):
        return self.codigo

class Sexo(models.Model):
    nombre = models.CharField(unique=True, max_length=25)
    
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    codigo = models.CharField(unique=True, max_length=50)
    nombre = models.CharField(unique=True, max_length=25)
    
    def __str__(self):
        return self.nombre

class ImparteCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_impartido = models.DateField()

class LlevaCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_llevado = models.DateField()

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

    def __str__(self):
        return self.user.username
