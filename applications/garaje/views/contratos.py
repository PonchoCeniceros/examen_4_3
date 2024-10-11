from django.shortcuts import render
from ..models import Contrato


def contratos_view(request):
    # Obtener todos los contratos, junto con los clientes y automóviles asociados
    contratos = Contrato.objects.select_related("cliente", "automovil").all()

    for contrato in contratos:
        # Calcular el costo total: precio del automóvil + sumatoria de los costos de características
        costo_caracteristicas = sum(
            caracteristica.costo
            for caracteristica in contrato.automovil.caracteristicas.all()
        )
        contrato.costo_total = contrato.automovil.precio + costo_caracteristicas

    context = {
        "contratos": contratos,
    }
    return render(request, "contratos.html", context)
