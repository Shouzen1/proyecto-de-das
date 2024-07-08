from django.db import models

# Create your models here.

# modelos en models.py

from django.db import models

class ObraDeArte(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
