from django.db import models

# Create your models here.

from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    # Otros campos relevantes para la marca

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    # Otros campos relevantes para el modelo

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    # Otros campos relevantes para el cliente

    def __str__(self):
        return self.nombre
