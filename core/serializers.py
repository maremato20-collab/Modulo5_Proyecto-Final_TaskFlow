from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Proyecto, Tarea


class TareaSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Tarea."""
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'proyecto', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProyectoSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Proyecto con sus tareas anidadas."""
   
    tareas = TareaSerializer(many=True, read_only=True)

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'usuario', 'tareas', 'created_at', 'updated_at']
        read_only_fields = ['id', 'usuario', 'created_at', 'updated_at']

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Crea el usuario encriptando su contraseña
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user