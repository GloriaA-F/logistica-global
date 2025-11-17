from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente, Conductor, Piloto, Vehiculo, Aeronave, Ruta, Carga, Despacho
from .serializers import (
    ClienteSerializer, ConductorSerializer, PilotoSerializer,
    VehiculoSerializer, AeronaveSerializer, RutaSerializer,
    CargaSerializer, DespachoSerializer
)
from .forms import (
    ClienteForm, ConductorForm, PilotoForm, VehiculoForm,
    AeronaveForm, RutaForm, CargaForm, DespachoForm
)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Vista Home
def home(request):
    return render(request, 'transporte/home.html')

# ============== CLIENTES ==============
def clientes_list(request):
    clientes = Cliente.objects.all()
    buscar = request.GET.get('buscar')
    if buscar:
        clientes = clientes.filter(
            nombre__icontains=buscar
        ) | clientes.filter(
            rut__icontains=buscar
        ) | clientes.filter(
            email__icontains=buscar
        )
    return render(request, 'transporte/clientes_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    return render(request, 'transporte/cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente')
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'transporte/cliente_form.html', {'form': form, 'titulo': 'Editar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente')
        return redirect('clientes_list')
    return render(request, 'transporte/confirm_delete.html', {'object': cliente, 'tipo': 'Cliente'})

# ============== CONDUCTORES ==============
def conductores_list(request):
    conductores = Conductor.objects.all()
    return render(request, 'transporte/conductores_list.html', {'conductores': conductores})

@login_required
def conductor_create(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor creado exitosamente')
            return redirect('conductores_list')
    else:
        form = ConductorForm()
    return render(request, 'transporte/conductor_form.html', {'form': form, 'titulo': 'Crear Conductor'})

@login_required
def conductor_edit(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conductor actualizado exitosamente')
            return redirect('conductores_list')
    else:
        form = ConductorForm(instance=conductor)
    return render(request, 'transporte/conductor_form.html', {'form': form, 'titulo': 'Editar Conductor'})

@login_required
def conductor_delete(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)
    if request.method == 'POST':
        conductor.delete()
        messages.success(request, 'Conductor eliminado exitosamente')
        return redirect('conductores_list')
    return render(request, 'transporte/confirm_delete.html', {'object': conductor, 'tipo': 'Conductor'})

# ============== PILOTOS ==============
def pilotos_list(request):
    pilotos = Piloto.objects.all()
    return render(request, 'transporte/pilotos_list.html', {'pilotos': pilotos})

@login_required
def piloto_create(request):
    if request.method == 'POST':
        form = PilotoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto creado exitosamente')
            return redirect('pilotos_list')
    else:
        form = PilotoForm()
    return render(request, 'transporte/piloto_form.html', {'form': form, 'titulo': 'Crear Piloto'})

@login_required
def piloto_edit(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    if request.method == 'POST':
        form = PilotoForm(request.POST, instance=piloto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Piloto actualizado exitosamente')
            return redirect('pilotos_list')
    else:
        form = PilotoForm(instance=piloto)
    return render(request, 'transporte/piloto_form.html', {'form': form, 'titulo': 'Editar Piloto'})

@login_required
def piloto_delete(request, pk):
    piloto = get_object_or_404(Piloto, pk=pk)
    if request.method == 'POST':
        piloto.delete()
        messages.success(request, 'Piloto eliminado exitosamente')
        return redirect('pilotos_list')
    return render(request, 'transporte/confirm_delete.html', {'object': piloto, 'tipo': 'Piloto'})

# ============== VEHÍCULOS ==============
def vehiculos_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'transporte/vehiculos_list.html', {'vehiculos': vehiculos})

def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo creado exitosamente')
            return redirect('vehiculos_list')
    else:
        form = VehiculoForm()
    return render(request, 'transporte/vehiculo_form.html', {'form': form, 'titulo': 'Crear Vehículo'})

def vehiculo_edit(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente')
            return redirect('vehiculos_list')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'transporte/vehiculo_form.html', {'form': form, 'titulo': 'Editar Vehículo'})

def vehiculo_delete(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        messages.success(request, 'Vehículo eliminado exitosamente')
        return redirect('vehiculos_list')
    return render(request, 'transporte/confirm_delete.html', {'object': vehiculo, 'tipo': 'Vehículo'})

# ============== AERONAVES ==============
def aeronaves_list(request):
    aeronaves = Aeronave.objects.all()
    return render(request, 'transporte/aeronaves_list.html', {'aeronaves': aeronaves})

def aeronave_create(request):
    if request.method == 'POST':
        form = AeronaveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aeronave creada exitosamente')
            return redirect('aeronaves_list')
    else:
        form = AeronaveForm()
    return render(request, 'transporte/aeronave_form.html', {'form': form, 'titulo': 'Crear Aeronave'})

def aeronave_edit(request, pk):
    aeronave = get_object_or_404(Aeronave, pk=pk)
    if request.method == 'POST':
        form = AeronaveForm(request.POST, instance=aeronave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aeronave actualizada exitosamente')
            return redirect('aeronaves_list')
    else:
        form = AeronaveForm(instance=aeronave)
    return render(request, 'transporte/aeronave_form.html', {'form': form, 'titulo': 'Editar Aeronave'})

def aeronave_delete(request, pk):
    aeronave = get_object_or_404(Aeronave, pk=pk)
    if request.method == 'POST':
        aeronave.delete()
        messages.success(request, 'Aeronave eliminada exitosamente')
        return redirect('aeronaves_list')
    return render(request, 'transporte/confirm_delete.html', {'object': aeronave, 'tipo': 'Aeronave'})

# ============== RUTAS ==============
def rutas_list(request):
    rutas = Ruta.objects.all()
    buscar = request.GET.get('buscar')
    tipo_transporte = request.GET.get('tipo_transporte')
    
    if buscar:
        rutas = rutas.filter(origen__icontains=buscar) | rutas.filter(destino__icontains=buscar)
    if tipo_transporte:
        rutas = rutas.filter(tipo_transporte=tipo_transporte)
    
    return render(request, 'transporte/rutas_list.html', {'rutas': rutas})

def ruta_create(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta creada exitosamente')
            return redirect('rutas_list')
    else:
        form = RutaForm()
    return render(request, 'transporte/ruta_form.html', {'form': form, 'titulo': 'Crear Ruta'})

def ruta_edit(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta actualizada exitosamente')
            return redirect('rutas_list')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'transporte/ruta_form.html', {'form': form, 'titulo': 'Editar Ruta'})

def ruta_delete(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == 'POST':
        ruta.delete()
        messages.success(request, 'Ruta eliminada exitosamente')
        return redirect('rutas_list')
    return render(request, 'transporte/confirm_delete.html', {'object': ruta, 'tipo': 'Ruta'})

# ============== CARGAS ==============
def cargas_list(request):
    cargas = Carga.objects.all()
    tipo = request.GET.get('tipo')
    cliente = request.GET.get('cliente')
    
    if tipo:
        cargas = cargas.filter(tipo=tipo)
    if cliente:
        cargas = cargas.filter(cliente_id=cliente)
    
    clientes = Cliente.objects.all()
    return render(request, 'transporte/cargas_list.html', {'cargas': cargas, 'clientes': clientes})

def carga_create(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carga creada exitosamente')
            return redirect('cargas_list')
    else:
        form = CargaForm()
    return render(request, 'transporte/carga_form.html', {'form': form, 'titulo': 'Crear Carga'})

def carga_edit(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    if request.method == 'POST':
        form = CargaForm(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carga actualizada exitosamente')
            return redirect('cargas_list')
    else:
        form = CargaForm(instance=carga)
    return render(request, 'transporte/carga_form.html', {'form': form, 'titulo': 'Editar Carga'})

def carga_delete(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    if request.method == 'POST':
        carga.delete()
        messages.success(request, 'Carga eliminada exitosamente')
        return redirect('cargas_list')
    return render(request, 'transporte/confirm_delete.html', {'object': carga, 'tipo': 'Carga'})

# ============== DESPACHOS ==============
def despachos_list(request):
    despachos = Despacho.objects.all()
    estado = request.GET.get('estado')
    
    if estado:
        despachos = despachos.filter(estado=estado)
    
    return render(request, 'transporte/despachos_list.html', {'despachos': despachos})

@login_required
def despacho_create(request):
    if request.method == 'POST':
        form = DespachoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Despacho creado exitosamente')
            return redirect('despachos_list')
    else:
        form = DespachoForm()
    return render(request, 'transporte/despacho_form.html', {'form': form, 'titulo': 'Crear Despacho'})

@login_required
def despacho_edit(request, pk):
    despacho = get_object_or_404(Despacho, pk=pk)
    if request.method == 'POST':
        form = DespachoForm(request.POST, instance=despacho)
        if form.is_valid():
            form.save()
            messages.success(request, 'Despacho actualizado exitosamente')
            return redirect('despachos_list')
    else:
        form = DespachoForm(instance=despacho)
    return render(request, 'transporte/despacho_form.html', {'form': form, 'titulo': 'Editar Despacho'})

@login_required
def despacho_delete(request, pk):
    despacho = get_object_or_404(Despacho, pk=pk)
    if request.method == 'POST':
        despacho.delete()
        messages.success(request, 'Despacho eliminado exitosamente')
        return redirect('despachos_list')
    return render(request, 'transporte/confirm_delete.html', {'object': despacho, 'tipo': 'Despacho'})

# ============== AUTENTICACIÓN ==============
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'transporte/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('home')

# ============== INFORMES (PROTEGIDO) ==============
@login_required
def informes(request):
    total_despachos = Despacho.objects.count()
    despachos_pendientes = Despacho.objects.filter(estado='PENDIENTE').count()
    despachos_en_ruta = Despacho.objects.filter(estado='EN_RUTA').count()
    despachos_entregados = Despacho.objects.filter(estado='ENTREGADO').count()
    
    total_cargas = Carga.objects.count()
    total_rutas = Ruta.objects.count()
    rutas_terrestres = Ruta.objects.filter(tipo_transporte='TERRESTRE').count()
    rutas_aereas = Ruta.objects.filter(tipo_transporte='AEREO').count()
    
    context = {
        'total_despachos': total_despachos,
        'despachos_pendientes': despachos_pendientes,
        'despachos_en_ruta': despachos_en_ruta,
        'despachos_entregados': despachos_entregados,
        'total_cargas': total_cargas,
        'total_rutas': total_rutas,
        'rutas_terrestres': rutas_terrestres,
        'rutas_aereas': rutas_aereas,
    }
    return render(request, 'transporte/informes.html', context)

# ============== ViewSets para API REST ==============
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'rut', 'email']
    filterset_fields = ['nombre']

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'rut', 'licencia']

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'rut', 'licencia']

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['patente', 'marca', 'modelo']
    filterset_fields = ['tipo']

class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['matricula', 'marca', 'modelo']
    filterset_fields = ['tipo']

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['origen', 'destino']
    filterset_fields = ['tipo_transporte']

class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descripcion', 'tipo']
    filterset_fields = ['tipo', 'cliente']

class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['estado']
    filterset_fields = ['estado', 'ruta']
