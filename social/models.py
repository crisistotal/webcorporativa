from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nombre",max_length=100)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated = models.DateField(auto_now=True,verbose_name="Fecha de Modificacion")
    
    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['-name']

    def __str__(self):
        return self.name    


'''
despues de crear el modelo tener que ir a activar la app en las settings del proyeto principal.
Si le cambias el verbose name del archivo admin tenes que meterlo al settigs con el nombre de la clase
'''