from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('mascotas/<str:nombre>/', views.detalle_mascota, name='detalle_mascota'),
]