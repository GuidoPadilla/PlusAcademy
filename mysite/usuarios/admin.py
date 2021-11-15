from django.contrib import admin
from .models import User, Nacionalidad, Sexo, Rol, NivelAcademico, UserExtra, Curso
# Register your models here.

# class MyUserAdmin(admin.ModelAdmin):
#     form = UserRegisterForm
#     def get_form(self, request, obj=None, **kwargs):
#         print("GET FORM")
#         self.exclude = []
#         if not request.user.is_staff:
#             self.exclude.append('is_staff') #here!
#         else:
#             pass
#         return super(MyUserAdmin, self).get_form(request, obj, **kwargs)

# admin.site.unregister(User)
# admin.site.register(User, MyUserAdmin)

admin.site.register(Sexo)
admin.site.register(Rol)
admin.site.register(NivelAcademico)
admin.site.register(UserExtra)
admin.site.register(Curso)
admin.site.register(Nacionalidad)