from django.contrib import admin
from .models import Pago, TipoPago, Moneda
# Register your models here.
admin.site.register(Pago)
admin.site.register(TipoPago)
admin.site.register(Moneda)