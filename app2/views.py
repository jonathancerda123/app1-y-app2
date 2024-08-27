from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Soy el index de la app2 </h1>") 

def saludo(request):
    html="""
    <h1>hola, muy buenas<h1>
    <a href="/app2/index">volver>/a>
    """
    return HttpResponse(html)