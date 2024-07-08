from django.db import models

# Create your models here.
from usuarios.models import Usuario
from django.contrib.auth.models import User



class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre 

class Obra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.CharField(max_length=100)
    precio = models.IntegerField()
    artista = models.ForeignKey(Artista,related_name='obras', on_delete=models.CASCADE)



    def __str__(self):
        return self.nombre
    
class Voto(models.Model):
	obra = models.ForeignKey(Obra,related_name='votos', on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario,related_name='votos', on_delete=models.CASCADE)
     
class Carrito_de_Compra(models.Model):
	CARRITO_ESTADO = [
		("pendiente", "Pendiente"),
		("comprado", "Comprado"),
	]
	estado = models.CharField(max_length=100, choices=CARRITO_ESTADO)
	total = models.IntegerField(max_length=100)
	usuario = models.ForeignKey(User,related_name="carritos", on_delete=models.CASCADE, blank=True, null=True)
     
class Producto_Carrito(models.Model):
    productos = models.ForeignKey("tienda.Obra", on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito_de_Compra, related_name="productos" ,on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=100)