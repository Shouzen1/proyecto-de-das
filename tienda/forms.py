from django import forms
from .models import Obra
from .models import Artista, Direccion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Obra(forms.ModelForm):
    class Meta:
        model = Obra
        fields = fields = ['nombre', 'descripcion', 'fecha', 'precio', 'artista']

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'descripcion', 'fecha']
from .models import Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'comuna', 'ciudad', 'pais', 'telefono']
