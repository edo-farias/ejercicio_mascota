from django import forms
from .models import Mascota, Veterinario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'color', 'descripcion', 'edad']
        
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono', 'correo']
        
        
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user