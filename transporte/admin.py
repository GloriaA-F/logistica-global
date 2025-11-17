from django.contrib import admin
from .models import Cliente, Conductor, Piloto, Vehiculo, Aeronave, Ruta, Carga, Despacho

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'rut', 'email', 'telefono']
    search_fields = ['nombre', 'rut', 'email']

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'rut', 'licencia', 'fecha_vencimiento_licencia']
    search_fields = ['nombre', 'rut', 'licencia']

@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'rut', 'licencia', 'horas_vuelo']
    search_fields = ['nombre', 'rut', 'licencia']

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['id', 'patente', 'marca', 'modelo', 'año', 'tipo', 'capacidad_carga']
    list_filter = ['tipo']
    search_fields = ['patente', 'marca', 'modelo']

@admin.register(Aeronave)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'matricula', 'marca', 'modelo', 'año', 'tipo', 'capacidad_carga']
    list_filter = ['tipo']
    search_fields = ['matricula', 'marca', 'modelo']

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ['id', 'origen', 'destino', 'distancia', 'tipo_transporte']
    list_filter = ['tipo_transporte']
    search_fields = ['origen', 'destino']

@admin.register(Carga)
class CargaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'peso', 'tipo', 'valor_declarado', 'cliente']
    list_filter = ['tipo']
    search_fields = ['descripcion']

@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_despacho', 'estado', 'ruta', 'carga']
    list_filter = ['estado']
    search_fields = ['observaciones']
