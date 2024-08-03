from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import MascotaForm, VeterinarioForm, RegistroForm
from .models import Mascota, Veterinario

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

def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
        
    else:
        form = MascotaForm()
    return render(request,'main/agregar_mascota.html', {'form': form})

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'main/lista_mascotas.html', {'mascotas': mascotas})


def agregar_veterinario(request):
    if request.method == "POST":
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'main/agregar_veterinario.html', {'form': form})

def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'main/lista_veterinarios.html', {'veterinarios': veterinarios})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'¡Cuenta creada para {username}!')
            return redirect('bienvenida')  
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})


@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')