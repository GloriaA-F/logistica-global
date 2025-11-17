# 🚚 Logística Global - Sistema de Gestión de Transporte

Sistema de gestión de transporte terrestre y aéreo desarrollado con Django REST Framework y desplegado en AWS.

## 📋 Características

- ✅ API REST completa con Django REST Framework
- ✅ Autenticación JWT
- ✅ CRUD completo para todas las entidades
- ✅ Filtros y búsquedas avanzadas
- ✅ Interfaz web con Bootstrap 5
- ✅ Documentación API con Swagger/ReDoc
- ✅ Base de datos PostgreSQL
- ✅ Despliegue en AWS con Nginx + Gunicorn

## 🛠️ Tecnologías

- Python 3.11
- Django 5.x
- Django REST Framework
- PostgreSQL 15
- Nginx
- Gunicorn
- Bootstrap 5
- AWS EC2

## 🚀 Modelos

- **Cliente**: Gestión de clientes
- **Conductor**: Personal de transporte terrestre
- **Piloto**: Personal de transporte aéreo
- **Vehículo**: Flota terrestre (camiones, furgones, buses)
- **Aeronave**: Flota aérea (aviones, helicópteros)
- **Ruta**: Rutas de transporte
- **Carga**: Detalle de mercancías
- **Despacho**: Registro de envíos

## 📦 Instalación Local

1. Clonar el repositorio
```bash
git clone url_detu_repo
cd logistica
```

2. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary gunicorn django-cors-headers drf-yasg django-filter crispy-bootstrap5
```

4. Configurar base de datos en `settings.py`

5. Ejecutar migraciones
```bash
python manage.py migrate
```

6. Crear superusuario
```bash
python manage.py createsuperuser
```

7. Cargar datos de prueba
```bash
python cargar_datos.py
```

8. Ejecutar servidor
```bash
python manage.py runserver
```

## 🔐 Autenticación

El sistema utiliza JWT para proteger:
- Gestión de conductores y pilotos
- Registro de despachos
- Informes de carga y rutas

## 📚 API Endpoints

- `/api/clientes/` - CRUD Clientes
- `/api/conductores/` - CRUD Conductores (requiere auth)
- `/api/pilotos/` - CRUD Pilotos (requiere auth)
- `/api/vehiculos/` - CRUD Vehículos
- `/api/aeronaves/` - CRUD Aeronaves
- `/api/rutas/` - CRUD Rutas
- `/api/cargas/` - CRUD Cargas
- `/api/despachos/` - CRUD Despachos (requiere auth)
- `/api/token/` - Obtener token JWT
- `/api/token/refresh/` - Refrescar token

## 📖 Documentación

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

## 🌐 Demo

URL: http://logisticaglobalback.duckdns.org

## 👨‍💻 Autor

gloria antibil  
Sección: IEI-172-N4  
Año: 2025

## 📄 Licencia

Este proyecto fue desarrollado como evaluación académica.
