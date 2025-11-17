import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistica.settings')
django.setup()

from transporte.models import Cliente, Conductor, Piloto, Vehiculo, Aeronave, Ruta, Carga, Despacho

def cargar_datos():
    # Clientes
    cliente1 = Cliente.objects.create(
        nombre="Empresa Retail SpA",
        rut="76.123.456-7",
        email="contacto@retailspa.cl",
        telefono="+56912345678",
        direccion="Av. Libertador 1234, Santiago"
    )
    
    cliente2 = Cliente.objects.create(
        nombre="Minera del Norte Ltda",
        rut="85.987.654-3",
        email="info@mineranorte.cl",
        telefono="+56987654321",
        direccion="Ruta 5 Norte Km 1500, Antofagasta"
    )
    
    cliente3 = Cliente.objects.create(
        nombre="Agrícola del Sur",
        rut="77.456.789-0",
        email="ventas@agricolasur.cl",
        telefono="+56956781234",
        direccion="Camino Rural s/n, Temuco"
    )
    
    # Conductores
    conductor1 = Conductor.objects.create(
        nombre="Juan Pérez González",
        rut="12.345.678-9",
        licencia="A3",
        fecha_vencimiento_licencia=date.today() + timedelta(days=365),
        telefono="+56912341111"
    )
    
    conductor2 = Conductor.objects.create(
        nombre="María Rodríguez Silva",
        rut="13.456.789-0",
        licencia="A5",
        fecha_vencimiento_licencia=date.today() + timedelta(days=730),
        telefono="+56912342222"
    )
    
    conductor3 = Conductor.objects.create(
        nombre="Carlos Muñoz Torres",
        rut="14.567.890-1",
        licencia="A3",
        fecha_vencimiento_licencia=date.today() + timedelta(days=500),
        telefono="+56912343333"
    )
    
    # Pilotos
    piloto1 = Piloto.objects.create(
        nombre="Alberto Fernández Rojas",
        rut="15.678.901-2",
        licencia="CPL",
        horas_vuelo=5000,
        certificaciones="Vuelo Instrumental, Multimotor"
    )
    
    piloto2 = Piloto.objects.create(
        nombre="Patricia Soto Vargas",
        rut="16.789.012-3",
        licencia="ATPL",
        horas_vuelo=8000,
        certificaciones="Vuelo Instrumental, Multimotor, Instructor"
    )
    
    # Vehículos
    vehiculo1 = Vehiculo.objects.create(
        patente="ABCD12",
        marca="Mercedes-Benz",
        modelo="Actros 2042",
        año=2020,
        tipo="CAMION",
        capacidad_carga=20.5
    )
    
    vehiculo2 = Vehiculo.objects.create(
        patente="EFGH34",
        marca="Volvo",
        modelo="FH16",
        año=2021,
        tipo="CAMION",
        capacidad_carga=25.0
    )
    
    vehiculo3 = Vehiculo.objects.create(
        patente="IJKL56",
        marca="Ford",
        modelo="Transit",
        año=2019,
        tipo="FURGON",
        capacidad_carga=3.5
    )
    
    # Aeronaves
    aeronave1 = Aeronave.objects.create(
        matricula="CC-AAA",
        marca="Cessna",
        modelo="208 Caravan",
        año=2018,
        tipo="AVION",
        capacidad_carga=1.5
    )
    
    aeronave2 = Aeronave.objects.create(
        matricula="CC-BBB",
        marca="Bell",
        modelo="407",
        año=2020,
        tipo="HELICOPTERO",
        capacidad_carga=0.8
    )
    
    # Rutas
    ruta1 = Ruta.objects.create(
        origen="Santiago",
        destino="Valparaíso",
        distancia=120.0,
        tipo_transporte="TERRESTRE",
        tiempo_estimado=timedelta(hours=1, minutes=30)
    )
    
    ruta2 = Ruta.objects.create(
        origen="Santiago",
        destino="Antofagasta",
        distancia=1366.0,
        tipo_transporte="TERRESTRE",
        tiempo_estimado=timedelta(hours=16)
    )
    
    ruta3 = Ruta.objects.create(
        origen="Santiago",
        destino="Punta Arenas",
        distancia=2500.0,
        tipo_transporte="AEREO",
        tiempo_estimado=timedelta(hours=3, minutes=30)
    )
    
    ruta4 = Ruta.objects.create(
        origen="Concepción",
        destino="Temuco",
        distancia=300.0,
        tipo_transporte="TERRESTRE",
        tiempo_estimado=timedelta(hours=4)
    )
    
    # Cargas
    carga1 = Carga.objects.create(
        descripcion="Electrodomésticos varios",
        peso=1500.0,
        tipo="GENERAL",
        valor_declarado=5000000.0,
        cliente=cliente1
    )
    
    carga2 = Carga.objects.create(
        descripcion="Equipos de minería",
        peso=8000.0,
        tipo="GENERAL",
        valor_declarado=25000000.0,
        cliente=cliente2
    )
    
    carga3 = Carga.objects.create(
        descripcion="Frutas y verduras frescas",
        peso=2000.0,
        tipo="PERECEDERA",
        valor_declarado=1500000.0,
        cliente=cliente3
    )
    
    carga4 = Carga.objects.create(
        descripcion="Material frágil - Cristalería",
        peso=500.0,
        tipo="FRAGIL",
        valor_declarado=3000000.0,
        cliente=cliente1
    )
    
    # Despachos
    despacho1 = Despacho.objects.create(
        estado="ENTREGADO",
        ruta=ruta1,
        carga=carga1,
        vehiculo=vehiculo3,
        conductor=conductor1,
        observaciones="Entrega exitosa"
    )
    
    despacho2 = Despacho.objects.create(
        estado="EN_RUTA",
        ruta=ruta2,
        carga=carga2,
        vehiculo=vehiculo1,
        conductor=conductor2,
        observaciones="En tránsito hacia el norte"
    )
    
    despacho3 = Despacho.objects.create(
        estado="PENDIENTE",
        ruta=ruta3,
        carga=carga3,
        aeronave=aeronave1,
        piloto=piloto1,
        observaciones="Esperando condiciones climáticas"
    )
    
    despacho4 = Despacho.objects.create(
        estado="EN_RUTA",
        ruta=ruta4,
        carga=carga4,
        vehiculo=vehiculo2,
        conductor=conductor3,
        observaciones="Carga frágil - manejo especial"
    )
    
    print("✅ Datos cargados exitosamente!")
    print(f"- {Cliente.objects.count()} clientes")
    print(f"- {Conductor.objects.count()} conductores")
    print(f"- {Piloto.objects.count()} pilotos")
    print(f"- {Vehiculo.objects.count()} vehículos")
    print(f"- {Aeronave.objects.count()} aeronaves")
    print(f"- {Ruta.objects.count()} rutas")
    print(f"- {Carga.objects.count()} cargas")
    print(f"- {Despacho.objects.count()} despachos")

if __name__ == "__main__":
    cargar_datos()
