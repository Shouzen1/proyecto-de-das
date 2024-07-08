from django.db import models

# Create your models here.
from usuarios.models import Usuario




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