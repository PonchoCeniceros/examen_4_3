from django.db import models


class Caracteristicas(models.Model):
    descripcion = models.TextField(max_length=250)
    costo = models.FloatField()

    def __str__(self):
        return f"{self.descripcion}, con valor de {self.costo}"
