from rest_framework import serializers
from .models import Cliente, Conductor, Piloto, Vehiculo, Aeronave, Ruta, Carga, Despacho
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    
    class Meta:
        model = Carga
        fields = '__all__'

class DespachoSerializer(serializers.ModelSerializer):
    ruta_detalle = serializers.CharField(source='ruta.__str__', read_only=True)
    carga_detalle = serializers.CharField(source='carga.__str__', read_only=True)
    
    class Meta:
        model = Despacho
        fields = '__all__'
