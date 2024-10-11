from django.urls import path, include
from . import views

urlpatterns = [
    path("contratos/", views.contratos_view, name="contratos"),
]
