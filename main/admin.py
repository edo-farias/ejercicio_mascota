from django.contrib import admin
from .models import Mascota, Veterinario

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Veterinario)