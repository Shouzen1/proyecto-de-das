from django.db import models

# Create your models here.
from usuarios.models import Usuario


class Obra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre 

class Voto(models.Model):
	obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.CharField(max_length=100)
    obras = models.ForeignKey(Obra,related_name='artista_obra', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
