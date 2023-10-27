from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>HOLA MUNDO</h1>")

def saludar(request):
    return HttpResponse("<h2>nuevo saludo para mi cliente especial</h2>")
