from django.shortcuts import render, HttpResponse


# Create your views here.
def lista_adopciones(request):
    return HttpResponse("Lista de adopciones")