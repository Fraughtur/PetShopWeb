from django.db import models


# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
 
    def __str__(self):
        return self.nombre
   
    class Meta:
        db_table = "categoria"
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'
        ordering = ['id']
 
class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Producto')
    descripcion = models.TextField(max_length=200, verbose_name='Descripcion del Producto')
    marca = models.CharField(max_length=50, null=True ,verbose_name='Marca del Producto')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    stock = models.IntegerField( verbose_name='Stock del Producto')
    imagen = models.ImageField(upload_to='images/')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
 
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Producto'
        ordering = ['id']
