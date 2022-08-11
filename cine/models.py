from django.conf import settings
from django.db import models
from django.utils import timezone

class Director(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Peliculas(models.Model):
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()

    
    def __str__(self):
        return self.title