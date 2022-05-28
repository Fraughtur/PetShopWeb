import email
from pickle import TRUE
from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=TRUE)
    nombre_usuario = models.CharField(max_length=30)
    contraseña_usuario = models.CharField(max_length=20)
    email_usuario = models.EmailField(max_length=100)
    celular_usuario = models.IntegerField(max_length=8)
    direccion_usuario = models.TextField(max_length=200)

class Socio(models.Model):
    id_socio = models.IntegerField(primary_key=TRUE)
    tipo_socio = ('socio', 'no socio')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    donacion_socio = models.IntegerField(max_length=8)
    

class Descuento(models.Model):
    id_descuento = models.IntegerField(primary_key=TRUE)
    porc_descuento = ('0', '5')
    
class Terminos(models.Model):
    id_nuevos_productos = models.IntegerField(max_length=2)
    id_nov_ofertas = models.IntegerField(max_length=2)
    si_no = models.CharField(max_length=2)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=TRUE)
    nombre_producto = models.CharField(max_length=50)
    precio_producto = models.IntegerField(max_length=7)
    stock = models.IntegerField(max_length=4)
    descripcion_producto = models.TextField(max_length=200)

    
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=TRUE)
    nombre_categoria = models.CharField(max_length=30)
    
class Region(models.Model):
    id_region = models.IntegerField(primary_key=TRUE)
    nombre_region = models.CharField(max_length=20)

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=TRUE)
    nombre_comuna = models.CharField(max_length=25)
