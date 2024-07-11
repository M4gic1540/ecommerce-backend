# models.py
from django.db import models

class Producto(models.Model):
    CATEGORIAS_CHOICES = [
        ('PC', 'PC'),
        ('PLAYSTATION', 'PlayStation'),
        ('XBOX', 'Xbox'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre
