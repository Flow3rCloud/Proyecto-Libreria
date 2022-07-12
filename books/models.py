from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    portada = models.ImageField(upload_to='portadas/', verbose_name='Portada')
    fecha_publicacion = models.DateField(null=True, verbose_name='Fecha de publicación')
    isbn = models.CharField(max_length=15, null=True, verbose_name='ISBN')
    anio = models.IntegerField(null=True, verbose_name='Año')
