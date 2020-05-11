from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200, unique=True)
    content = RichTextField(verbose_name="Nombre",max_length=100)
    order = models.SmallIntegerField(verbose_name="Orden",default=0)
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated = models.DateField(auto_now=True,verbose_name="Fecha de Modificacion")
    
    # Esto es para ordenar como van a salir en el menu de footer

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ['order', '-title']

    def __str__(self):
        return self.title    
