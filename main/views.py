from django.shortcuts import render, HttpResponse

# Create your views here.
def bienvenida(request):
    return render(request, 'main/bienvenida.html')

def mascotas (request):
    
    mascotas = ["Simba", "Dalila", "Negrita", "Chica"]
    
    return render (request, 'mascotas/mascotas.html', {'mascotas': mascotas})

def saludo(request, nombre):
    return HttpResponse(f"¡Hola, {nombre}")

def detalle_mascota (request, nombre):
    detalles = {
        'Simba': 'Es una perrita marron',
        'Dalila': 'Es muy juguetona',
        'Negrita': 'No hace caso, es muy loca',
        'Chica': 'Es una gatita dormilona',
        'Fido': 'Es muy curioso',
    }
    
    descripcion = detalles.get(nombre, "Mascota no encontrada")
    
    return render(request,'mascotas/detalle_mascota.html', {'nombre': nombre, 'descripcion': descripcion})
