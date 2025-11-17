from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'pilotos', views.PilotoViewSet)
router.register(r'vehiculos', views.VehiculoViewSet)
router.register(r'aeronaves', views.AeronaveViewSet)
router.register(r'rutas', views.RutaViewSet)
router.register(r'cargas', views.CargaViewSet)
router.register(r'despachos', views.DespachoViewSet)

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Autenticación
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('informes/', views.informes, name='informes'),
    # Clientes
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    
    # Conductores
    path('conductores/', views.conductores_list, name='conductores_list'),
    path('conductores/crear/', views.conductor_create, name='conductor_create'),
    path('conductores/editar/<int:pk>/', views.conductor_edit, name='conductor_edit'),
    path('conductores/eliminar/<int:pk>/', views.conductor_delete, name='conductor_delete'),
    
    # Pilotos
    path('pilotos/', views.pilotos_list, name='pilotos_list'),
    path('pilotos/crear/', views.piloto_create, name='piloto_create'),
    path('pilotos/editar/<int:pk>/', views.piloto_edit, name='piloto_edit'),
    path('pilotos/eliminar/<int:pk>/', views.piloto_delete, name='piloto_delete'),
    
    # Vehículos
    path('vehiculos/', views.vehiculos_list, name='vehiculos_list'),
    path('vehiculos/crear/', views.vehiculo_create, name='vehiculo_create'),
    path('vehiculos/editar/<int:pk>/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculos/eliminar/<int:pk>/', views.vehiculo_delete, name='vehiculo_delete'),
    
    # Aeronaves
    path('aeronaves/', views.aeronaves_list, name='aeronaves_list'),
    path('aeronaves/crear/', views.aeronave_create, name='aeronave_create'),
    path('aeronaves/editar/<int:pk>/', views.aeronave_edit, name='aeronave_edit'),
    path('aeronaves/eliminar/<int:pk>/', views.aeronave_delete, name='aeronave_delete'),
    
    # Rutas
    path('rutas/', views.rutas_list, name='rutas_list'),
    path('rutas/crear/', views.ruta_create, name='ruta_create'),
    path('rutas/editar/<int:pk>/', views.ruta_edit, name='ruta_edit'),
    path('rutas/eliminar/<int:pk>/', views.ruta_delete, name='ruta_delete'),
    
    # Cargas
    path('cargas/', views.cargas_list, name='cargas_list'),
    path('cargas/crear/', views.carga_create, name='carga_create'),
    path('cargas/editar/<int:pk>/', views.carga_edit, name='carga_edit'),
    path('cargas/eliminar/<int:pk>/', views.carga_delete, name='carga_delete'),
    
    # Despachos
    path('despachos/', views.despachos_list, name='despachos_list'),
    path('despachos/crear/', views.despacho_create, name='despacho_create'),
    path('despachos/editar/<int:pk>/', views.despacho_edit, name='despacho_edit'),
    path('despachos/eliminar/<int:pk>/', views.despacho_delete, name='despacho_delete'),
    
    # API REST
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
