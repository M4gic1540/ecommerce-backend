# Dockerfile

# Utiliza una imagen base oficial de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y gcc libpq-dev

# Configura y activa el entorno virtual
RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate

# Instala las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Exponer el puerto en el que la aplicación estará ejecutándose
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ecommerce.wsgi:application"]
