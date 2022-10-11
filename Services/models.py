from unittest.util import _MAX_LENGTH
from django.db import models
from tabnanny import verbose
from django.contrib.auth.models import User 

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200,  verbose_name='Titulo')
    subtitle = models.CharField(max_length=200,  verbose_name='Sub-Titulo')
    content = models.TextField( verbose_name='Contenido')
    image = models.ImageField( verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add =True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now =True,verbose_name='Fecha de edicion')

    class Meta:  #Se utiliza para dar detalees extendidos a la clase, ejemplo modificar el nombre project por proyecto, etc.
        verbose_name = "Servicio"
        verbose_name_plural= "Servicios"
        ordering = ["-created"]   # el guion delante hace que sea invertido la ordenacion

    def __str__(self) :
        return self.title