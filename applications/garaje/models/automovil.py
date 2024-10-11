from django.db import models
from .modelo import Modelo
from .caracteristicas import Caracteristicas


class Color(models.TextChoices):
    BLANCO = "BLANCO", "Blanco"
    NEGRO = "NEGRO", "Negro"
    ROJO = "ROJO", "Rojo"


class Motor(models.TextChoices):
    M4CIL = "4CIL", "4 cilindros"
    M8CIL = "8CIL", "8 cilindros"


class Automovil(models.Model):
    nombre = models.TextField(max_length=75)
    color = models.TextField(max_length=10, choices=Color.choices, default=Color.NEGRO)
    peso = models.FloatField()
    motor = models.TextField(max_length=4, choices=Motor.choices, default=Motor.M4CIL)
    precio = models.FloatField()
    modelo = models.OneToOneField(Modelo, on_delete=models.CASCADE)
    caracteristicas = models.ManyToManyField(Caracteristicas)

    def __str__(self):
        return f"{self.nombre}"
