from django import forms
from .models import Cliente, Conductor, Piloto, Vehiculo, Aeronave, Ruta, Carga, Despacho

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_vencimiento_licencia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'horas_vuelo': forms.NumberInput(attrs={'class': 'form-control'}),
            'certificaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'capacidad_carga': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class AeronaveForm(forms.ModelForm):
    class Meta:
        model = Aeronave
        fields = '__all__'
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'capacidad_carga': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'
        widgets = {
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'distancia': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo_transporte': forms.Select(attrs={'class': 'form-control'}),
            'tiempo_estimado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}),
        }

class CargaForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'valor_declarado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class DespachoForm(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = '__all__'
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'ruta': forms.Select(attrs={'class': 'form-control'}),
            'carga': forms.Select(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'aeronave': forms.Select(attrs={'class': 'form-control'}),
            'conductor': forms.Select(attrs={'class': 'form-control'}),
            'piloto': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
