from ast import Delete
from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    imagen = models.ImageField(upload_to='imagen/', verbose_name='Portada', blank=True, null=True)
    fecha_publicacion = models.DateField(null=True, verbose_name='Fecha de publicación')
    isbn = models.CharField(max_length=15, null=True, verbose_name='ISBN')
    anio = models.IntegerField(null=True, verbose_name='Año')

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)
        super().delete()
