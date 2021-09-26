from django.contrib import admin
from .models import Pago, TipoPago, FormaPago, Moneda, EliminacionPagos, Gasto, TipoGasto
# Register your models here.
admin.site.register(Pago)
admin.site.register(TipoGasto)
admin.site.register(Gasto)
admin.site.register(EliminacionPagos)
admin.site.register(TipoPago)
admin.site.register(FormaPago)
admin.site.register(Moneda)
