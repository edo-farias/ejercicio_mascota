from django import forms
from .models import Mascota, Veterinario 

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'color', 'descripcion', 'edad']
        
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono', 'correo']