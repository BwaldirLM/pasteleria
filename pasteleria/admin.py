from django.contrib import admin

from pasteleria.models import *

# Register your models here.

class PastelAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion', 'precio']
    ordering =  ['nombre']

admin.site.register(Pastel, PastelAdmin)
admin.site.register(Vendedor)
admin.site.register(Produccion)
admin.site.register(Cliente)
admin.site.register(JefeProduccion)
admin.site.register(Venta)
admin.site.register(VentaDetalle)
admin.site.register(Pago)
