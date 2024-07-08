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

class Carrito_de_Compra(models.Model):
	CARRITO_ESTADO = [
		("pendiente", "Pendiente"),
		("comprado", "Comprado"),
	]
	productos = models.ForeignKey("tienda.Obra", on_delete=models.CASCADE)
	estado = models.CharField(max_length=100, choices=CARRITO_ESTADO)
	total = models.IntegerField(max_length=100)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    direcciones = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    carrito_de_compra = models.ForeignKey(Carrito_de_Compra, on_delete=models.CASCADE, blank=True, null=True)

