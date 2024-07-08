from django import forms
from .models import ObraDeArte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ObraDeArteForm(forms.ModelForm):
    class Meta:
        model = ObraDeArte
        fields = ['titulo', 'descripcion']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']