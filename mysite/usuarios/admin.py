from django.contrib import admin
from .models import Nacionalidad, Sexo, Rol, NivelAcademico, UserExtra, Curso
# Register your models here.

admin.site.register(Sexo)
admin.site.register(Rol)
admin.site.register(NivelAcademico)
admin.site.register(UserExtra)
admin.site.register(Curso)
admin.site.register(Nacionalidad)