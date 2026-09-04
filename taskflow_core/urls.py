from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración base para la documentación de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="TaskFlow API",
        default_version='v1',
        description="Documentación oficial de la API para gestión de proyectos y tareas.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tu_correo@ejemplo.com"), # Puedes poner tu correo aquí
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Panel de administración nativo
    path('admin/', admin.site.urls),
    
    # Rutas de la API (Usuarios, Proyectos y Tareas)
    path('api/', include('core.urls')),
    
    # Rutas para la documentación de Swagger y Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]