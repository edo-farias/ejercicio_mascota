from django.shortcuts import render, HttpResponse

# Create your views here.
def bienvenida(request):
    return HttpResponse("¡Bienvenido a Mascotas!!!")


def saludo(request, nombre):
    return HttpResponse(f"¡Hola, {nombre}")
