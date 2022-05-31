import email
from pickle import TRUE
from sre_parse import CATEGORIES
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=TRUE, verbose_name='Id de usuario')
    nombre_usuario = models.CharField(max_length=30, verbose_name='Nombre Usuario')
    contraseña_usuario = models.CharField(max_length=20, verbose_name='Contraseña Usuario')
    email_usuario = models.EmailField(max_length=100, verbose_name='Correo electronico Usuario')
    celular_usuario = models.IntegerField( verbose_name='Celular Usuario')
    direccion_usuario = models.TextField(max_length=200, verbose_name='Direccion Usuario')
    
    
    def __str__(self):
        return self.nombre_usuario

class Socio(models.Model):
    id_socio = models.IntegerField(primary_key=TRUE, verbose_name='Id Socio')
    tipo_socio = models.CharField(max_length=10, verbose_name='Tipo de Socio')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Id Usuario')
    donacion_socio = models.IntegerField( verbose_name='Donacion Socio')
    
    def __str__(self):
        return self.tipo_socio

class Descuento(models.Model):
    id_descuento = models.IntegerField(primary_key=TRUE, verbose_name='Id descuento')
    porc_descuento = models.IntegerField( verbose_name='porcentaje descuento')
    
    def __init__(self):
        return self.porc_descuento
    

class Terminos(models.Model):
    id_nuevos_productos = models.IntegerField( verbose_name='id nuevos productos')
    id_nov_ofertas = models.IntegerField( verbose_name='id novedades y ofertas')
    si_no = models.CharField(max_length=2, verbose_name='opcion si o no')
    
    def __str__(self):
        return self.si_no

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=TRUE, verbose_name='id producto')
    nombre_producto = models.CharField(max_length=50, verbose_name='nombre producto')
    precio_producto = models.IntegerField(verbose_name='precio producto')
    stock = models.IntegerField(verbose_name='stocks producto')
    descripcion_producto = models.TextField(max_length=200, verbose_name='descripcion producto')
    
    def __init__(self):
        return self.id_producto

    
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=TRUE, verbose_name='id categoria')
    nombre_categoria = models.CharField(max_length=30, verbose_name='nombre categoria')
    
    def __str__(self):
        return self.nombre_categoria
    
class Region(models.Model):
    id_region = models.IntegerField(primary_key=TRUE, verbose_name='id region')
    nombre_region = models.CharField(max_length=20, verbose_name='nombre region')
    
    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=TRUE, verbose_name='id comuna')
    nombre_comuna = models.CharField(max_length=25, verbose_name='nombre comuna')
    
    def __str__(self):
        return self.nombre_comuna
