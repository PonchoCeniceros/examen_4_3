from django.db import models


class Sexo(models.TextChoices):
    MASCULINO = "M", "Masculino"
    FEMENINO = "F", "Femenino"


class MiInformacion(models.Model):
    nombre = models.TextField(max_length=75)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField(max_length=250)
    telefono = models.TextField(max_length=13)
    email = models.TextField(max_length=35)
    sexo = models.CharField(max_length=1, choices=Sexo.choices, default=Sexo.MASCULINO)

    def __str__(self):
        return f"{self.nombre}"
