from django.db import models
from .automovil import Automovil
from applications.participante.models import MiInformacion


class Contrato(models.Model):
    cliente = models.OneToOneField(
        MiInformacion, on_delete=models.SET_NULL, null=True, blank=True
    )
    automovil = models.OneToOneField(
        Automovil, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"contrato {self.id}"
