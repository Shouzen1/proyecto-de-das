from django import forms
from .models import Obra
from .models import Artista
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Obra(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'descripcion']


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'descripcion', 'fecha']