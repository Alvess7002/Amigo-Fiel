from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("petshop/<int:id>/", views.detalhe, name="detalhe"),
]
