from django.urls import path
from . import views #para traer las rutas de views hasta urls.py

urlpatterns = [
    path('inicio/', views.index),
    path('saludo/', views.saludo),
]
