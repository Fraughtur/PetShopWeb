from django.db import models


# Create your models here.


class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombre_categoria=models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
 
    def __str__(self):
        return self.nombre_categoria
 
 
class Producto(models.Model):
    nombre_producto=models.CharField(max_length=50, primary_key=True, verbose_name='Nombre del Producto')
    descripcion_producto=models.TextField(max_length=200, verbose_name='Descripcion del Producto')
    marca_producto=models.CharField(max_length=50, null=True ,verbose_name='Marca del Producto')
    precio_producto= models.IntegerField(verbose_name='Precio del Producto')
    stock_producto= models.IntegerField( verbose_name='Stock del Producto')
    imagen_producto=models.ImageField(upload_to='images/')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre_producto
        
class Socio(models.Model):
      id_socio=models.IntegerField(primary_key=True, verbose_name='Id del socio')
      pertenece_socio=models.CharField(max_length=3, verbose_name='Pertenece a socio SI/NO')
      
      def __str__(self):
        return self.pertenece_socio

class Usuario(models.Model):
    nombre_usuario=models.CharField(max_length=50, primary_key=True, verbose_name='Nombre del Usuario')
    email_usuario=models.CharField(max_length=100,verbose_name='Correo del Usuario')
    contraseña_usuario=models.CharField(max_length=25,verbose_name='Contraseña del Usuario')
    Socio=models.ForeignKey(Socio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario

