from django.db import models


# Create your models here.


class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombre_categoria=models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
 
    def __str__(self):
        return self.nombre_categoria
 
 
class Producto(models.Model):
    nombre_producto=models.TextField(max_length=50, primary_key=True, verbose_name='Nombre del Producto')
    descripcion_producto=models.TextField(max_length=200, verbose_name="Descripcion del Producto")
    precio_producto= models.IntegerField(verbose_name='Precio del Producto')
    stock_producto= models.IntegerField( verbose_name='Stock del Producto')
    imagen_producto=models.ImageField(upload_to='images/')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre_producto

class Socio(models.Model):
    id_socio= models.IntegerField(primary_key=True, verbose_name='Id de Socio')
    pertenece= models.CharField(max_length=2, verbose_name='Pertenece si o no')
    
    def __str__(self):
        return self.pertenece
    
class Usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True, verbose_name='Id de Usuario')
    nombre_usuario= models.CharField(max_length=30, verbose_name='Nombre Usuario')
    correo= models.EmailField(verbose_name='Email de Usuario')
    contrasena= models.CharField(max_length=16, verbose_name='Contraseña Usuario')
    direccion=models.TextField(max_length=50, verbose_name='Direccion Usuario')
    celular= models.IntegerField( verbose_name='Celular Usuario')
    socio= models.ForeignKey(Socio, on_delete=models.CASCADE)
    
    def __init__(self):
        return self.id_usuario