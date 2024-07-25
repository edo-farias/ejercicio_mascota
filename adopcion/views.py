from django.shortcuts import render, HttpResponse


# Create your views here.
def lista_adopciones(request):
    return render(request, 'adopcion/lista_adopciones.html')