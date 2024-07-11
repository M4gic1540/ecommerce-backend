# Ecommerce Backend

Este es el backend del proyecto Ecommerce, desarrollado con Django y Django REST Framework. Este repositorio contiene todo el código necesario para configurar y ejecutar el backend localmente.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.8 o superior
- Pip (el gestor de paquetes de Python)
- MySQL
- Git


## Instalación

Sigue los siguientes pasos para configurar y ejecutar el proyecto localmente.

1. Clona el repositorio

git clone https://github.com/M4gic1540/deploy-django-railway.git

luego hay que dirigirse a la carpeta del proyecto

cd deploy-django-railway

2. Crea y activa un entorno virtual

python -m venv venv

source venv/bin/activate # para Linux

`venv\Scripts\activate` # para Windows

3. Instala las dependencias

- pip install -r requirements.txt

4. Configura la base de datos

Asegúrate de tener una base de datos MySQL configurada de  lo contrario Utiliza SQlite3 para desplegar localmente

Configuracion para Base de datos Predeterminada (Sqlite3)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

de lo contrario si tienes una base de datos lista, crea un archivo .env en el directorio raíz del proyecto y agrega las siguientes variables de entorno:

DATABASE_NAME=tu_nombre_de_base_de_datos
DATABASE_USER=tu_usuario
DATABASE_PASSWORD=tu_contraseña
DATABASE_HOST=localhost
DATABASE_PORT=3306
SECRET_KEY=tu_clave_secreta
DEBUG=True

5. Realiza las migraciones de la base de datos

- python manage.py makemigrations

- python manage.py migrate

6. Crea un superusuario

- python manage.py createsuperuser

7. Ejecuta el servidor de desarrollo

- python manage.py runserver


si esta todo correctamente Configurado Deberia aparecer el siguiente mensaje:

![alt text](image.png)


### Endpoints de la API

(para poder ingresar a las vistas de DRF  debes estar logueado con el user creado anteriormente)

- /api/usuario/ - Endpoint para gestionar usuarios. 

![alt text](image-1.png)

- /api/productos/ - Endpoint para gestionar productos. 
![alt text](image-2.png)


- /api/carrito/ - Endpoint para gestionar el carrito de compras.
- /api/carrito/items/ Endpoint para gestionar items del carro de compras

![alt text](image-3.png)

