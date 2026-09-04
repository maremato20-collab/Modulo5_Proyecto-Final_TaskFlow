from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, TareaViewSet, TareasPendientesAPIView

# Configuración del Router para los ViewSets
router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    # Rutas del CRUD del Router
    path('', include(router.urls)),
    
    # Endpoint explícito con APIView
    path('tareas/pendientes/', TareasPendientesAPIView.as_view(), name='tareas-pendientes'),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ProyectoViewSet, TareaViewSet, TareasPendientesAPIView, RegistroAPIView

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    # Endpoints de Autenticación
    path('auth/registro/', RegistroAPIView.as_view(), name='registro'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # POST /api/token/ (Retorna Access & Refresh Token)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # POST /api/token/refresh/ (Renueva el Access Token)
    
    # Endpoints de la API REST
    path('', include(router.urls)),
    path('tareas/pendientes/', TareasPendientesAPIView.as_view(), name='tareas-pendientes'),
]