from django.contrib import admin

from pasteleria.models import Pastel

# Register your models here.

class PastelAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'precio']
    ordering =  ['nombre']

admin.site.register(Pastel)