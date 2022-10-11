from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add =True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now =True,verbose_name='Fecha de edicion')

    class Meta:  #Se utiliza para dar detalees extendidos a la clase, ejemplo modificar el nombre project por proyecto, etc.
        verbose_name = "Categoria"
        verbose_name_plural= "Categorias"
        ordering = ["-created"]   # el guion delante hace que sea invertido la ordenacion

    def __str__(self) :
        return self.name


class Post(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="fecha de publicacion", default=now)
    image=models.ImageField(verbose_name="Imagem", upload_to="blog", null=True, blank=True)
    author=models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE) 
    categories=models.ManyToManyField(Category,verbose_name="Categorias",related_name='get_posts')
    created = models.DateTimeField(auto_now_add =True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now =True,verbose_name='Fecha de edicion')

    class Meta:  #Se utiliza para dar detalees extendidos a la clase, ejemplo modificar el nombre project por proyecto, etc.
        verbose_name = "Entrada"
        verbose_name_plural= "Entradas"
        ordering = ["-created"]   # el guion delante hace que sea invertido la ordenacion

    def __str__(self) :
        return self.title
