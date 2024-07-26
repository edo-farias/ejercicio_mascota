from django.shortcuts import render, HttpResponse

# Create your views here.
def bienvenida(request):
    return render(request, 'main/bienvenida.html')

def mascotas (request):
    
    mascotas = ["Simba", "Dalila", "Negrita", "Chica"]
    
    return render (request, 'mascotas/mascotas.html', {'mascotas': mascotas})

def saludo(request, nombre):
    return HttpResponse(f"¡Hola, {nombre}")
