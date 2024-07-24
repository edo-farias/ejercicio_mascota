from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_adopciones, name='lista_adopciones'),
]