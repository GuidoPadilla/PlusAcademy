from django.contrib import admin
from .models import Sexo, Rol, NivelAcademico, UserExtra
# Register your models here.

admin.site.register(Sexo)
admin.site.register(Rol)
admin.site.register(NivelAcademico)
admin.site.register(UserExtra)