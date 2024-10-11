import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Modelo(models.Model):
    anio = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year),
        ]
    )

    def __str__(self):
        return f"modelo {self.anio}"
