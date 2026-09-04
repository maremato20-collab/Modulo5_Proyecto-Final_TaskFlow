# TaskFlow API - trabajo final modulo 5

API REST desarrollada con Django y Django REST Framework para la gestión estructurada de proyectos y sus tareas asociadas, protegida mediante autenticación JWT.

## Requisitos Previos:
* Python 3.10 o superior.
* Entorno virtual de Python (`venv`).

## Instalación de dependencias:
1. Abrir una terminal en la carpeta raíz del proyecto.
2. Crea y activa tu entorno virtual con el comando:
   python -m venv venv
   venv\Scripts\activate  # En Windows
3. Instala las librerías del proyecto con el comando:
   pip install -r requirements.txt

## Configuración de variables de entorno
Crear un archivo llamado `.env` en la raíz del proyecto y agregar la siguiente configuración para entornos de desarrollo:
DEBUG=True

## Configuración de la base de datos y migraciones
El proyecto utiliza SQLite de forma predeterminada. Para generar y aplicar las tablas a la base de datos, ejecutar el comando:
python manage.py makemigrations
python manage.py migrate

## Creación del superusuario
Para poder ingresar al panel de administración de Django, crea tu usuario administrador ejecutando el siguiente comando y llenando los datos solicitados:
python manage.py createsuperuser

## Ejecución del servidor de desarrollo
Levanta el servidor local especificando el puerto 8080:
python manage.py runserver 8080

## Acceso a la documentación de la API (Swagger/OpenAPI)
Con el servidor en ejecución, abre tu navegador web y visita la siguiente ruta para probar los endpoints de forma interactiva:
* http://127.0.0.1:8080/swagger/

## Cómo ejecutar las pruebas
Para verificar la integridad de la seguridad y la lógica del negocio mediante pruebas unitarias automatizadas, ejecutar:
python manage.py test
