from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, related_name="direcciones" ,on_delete=models.CASCADE)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

