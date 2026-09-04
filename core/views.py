from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Proyecto, Tarea
from .serializers import (
    ProyectoSerializer, 
    TareaSerializer, 
    RegistroSerializer
)


class RegistroAPIView(APIView):
    """Endpoint público para registrar nuevos usuarios."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuario registrado exitosamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProyectoViewSet(viewsets.ModelViewSet):
    """
    CRUD para Proyectos.
    Cada usuario solo gestiona sus propios recursos.
    """
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optimización con prefetch_related para cargar tareas asociadas
        return Proyecto.objects.filter(usuario=self.request.user).prefetch_related('tareas')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class TareaViewSet(viewsets.ModelViewSet):
    """
    CRUD para Tareas.
    """
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optimización con select_related para evitar consultas extra al proyecto
        return Tarea.objects.filter(proyecto__usuario=self.request.user).select_related('proyecto')


class TareasPendientesAPIView(APIView):
    """
    Endpoint con APIView que retorna únicamente las tareas pendientes del usuario.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tareas_pendientes = Tarea.objects.filter(
            proyecto__usuario=request.user,
            estado='pendiente'
        ).select_related('proyecto')
        serializer = TareaSerializer(tareas_pendientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)