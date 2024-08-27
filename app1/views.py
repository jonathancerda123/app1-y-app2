from django.shortcuts import render
from django.http import HttpResponse #envia una respuesta de vuelta al cliente, httpresquest es cuando el cliente pide algo

# Create your views here.

def index(request):
    html="""
    <h1>soy el index de la app</h1>
    <h2>Hola!</h2>
    """

    return HttpResponse(html)

 
def saludo(request):
    html="""
    <h1 style="color:turquoise">¿que tal, como esta?</h1>
    <h2 style="color:skyblue">¿como se siente mi vida hermosa?</h2>

    """

    return HttpResponse(html)