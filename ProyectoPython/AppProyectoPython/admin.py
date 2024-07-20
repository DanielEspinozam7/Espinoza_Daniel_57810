from django.contrib import admin

# Register your models here.
from .models import *

#Con esta clase podemos hacer que aparezcan los atributos como campo en la app admin
class CotizacionAdmin (admin.ModelAdmin):
    list_display = ("detalle", "mayorista")
    #Agregamos filtros con la siguiente instruccion
    list_filter = ("detalle",)

admin.site.register(Cliente)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(Producto)

