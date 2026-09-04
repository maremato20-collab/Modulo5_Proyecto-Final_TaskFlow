from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Proyecto

class ProyectoAPITests(APITestCase):
    
    def setUp(self):
      
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword123'
        )
      
        self.url = '/api/proyectos/' 

    def test_crear_proyecto_sin_autenticacion_falla(self):
        """Verifica que el sistema rechace la petición si no hay token (401 Unauthorized)"""
        data = {'nombre': 'Proyecto Hacker', 'descripcion': 'Intento de intrusión'}
        response = self.client.post(self.url, data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Proyecto.objects.count(), 0)

    def test_crear_proyecto_con_autenticacion_es_exitoso(self):
        """Verifica que un usuario autenticado pueda crear un proyecto (201 Created)"""
      
        self.client.force_authenticate(user=self.user)
        
        data = {'nombre': 'Proyecto Seguro', 'descripcion': 'Creado por testuser'}
        response = self.client.post(self.url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Proyecto.objects.count(), 1)
        self.assertEqual(Proyecto.objects.get().nombre, 'Proyecto Seguro')