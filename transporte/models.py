from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'cliente'

class Conductor(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    licencia = models.CharField(max_length=20)
    fecha_vencimiento_licencia = models.DateField()
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'conductor'

class Piloto(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)
    licencia = models.CharField(max_length=20)
    horas_vuelo = models.IntegerField()
    certificaciones = models.TextField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'piloto'

class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('CAMION', 'Camión'),
        ('FURGON', 'Furgón'),
        ('BUS', 'Bus'),
    ]
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    capacidad_carga = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"
    
    class Meta:
        db_table = 'vehiculo'

class Aeronave(models.Model):
    TIPO_CHOICES = [
        ('AVION', 'Avión'),
        ('HELICOPTERO', 'Helicóptero'),
    ]
    matricula = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    capacidad_carga = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.modelo}"
    
    class Meta:
        db_table = 'aeronave'

class Ruta(models.Model):
    TIPO_TRANSPORTE_CHOICES = [
        ('TERRESTRE', 'Terrestre'),
        ('AEREO', 'Aéreo'),
    ]
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transporte = models.CharField(max_length=15, choices=TIPO_TRANSPORTE_CHOICES)
    tiempo_estimado = models.DurationField()
    
    def __str__(self):
        return f"{self.origen} - {self.destino} ({self.tipo_transporte})"
    
    class Meta:
        db_table = 'ruta'

class Carga(models.Model):
    TIPO_CHOICES = [
        ('FRAGIL', 'Frágil'),
        ('PERECEDERA', 'Perecedera'),
        ('GENERAL', 'General'),
        ('PELIGROSA', 'Peligrosa'),
    ]
    descripcion = models.TextField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    valor_declarado = models.DecimalField(max_digits=12, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cargas')
    
    def __str__(self):
        return f"{self.descripcion} - {self.peso}kg"
    
    class Meta:
        db_table = 'carga'

class Despacho(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_RUTA', 'En Ruta'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]
    fecha_despacho = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='PENDIENTE')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    aeronave = models.ForeignKey(Aeronave, on_delete=models.SET_NULL, null=True, blank=True)
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, null=True, blank=True)
    piloto = models.ForeignKey(Piloto, on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Despacho #{self.id} - {self.estado}"
    
    class Meta:
        db_table = 'despacho'
