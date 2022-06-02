from distutils.command.upload import upload
import email
from pickle import TRUE
from pyexpat import model
from sre_parse import CATEGORIES
from tkinter import CASCADE
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='id categoria')
    nombre_categoria = models.CharField(max_length=50,verbose_name='nombre categoria')

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.TextField(max_length=100, primary_key=True,verbose_name='nombre producto')
    descripcion_producto = models.TextField(max_length=200, verbose_name='descripcion del producto')
    precio = models.IntegerField(verbose_name='precio producto')
    stock = models.IntegerField(verbose_name='cantidad de producto')
    imagen_producto = models.ImageField(upload='img/', verbose_name='imagen producto')
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class Socio(models.Model):
    id_socio = models.IntegerField(primary_key=TRUE, verbose_name='Id Socio')
    tipo_socio = models.CharField(max_length=10, verbose_name='Tipo de Socio')
    donacion_socio = models.IntegerField( verbose_name='Donacion Socio')
    
    def __str__(self):
        return self.tipo_socio

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=TRUE, verbose_name='Id de usuario')
    nombre_usuario = models.CharField(max_length=30, verbose_name='Nombre Usuario')
    contraseña_usuario = models.CharField(max_length=20, verbose_name='Contraseña Usuario')
    email_usuario = models.EmailField(max_length=100, verbose_name='Correo electronico Usuario')
    celular_usuario = models.IntegerField( verbose_name='Celular Usuario')
    direccion_usuario = models.TextField(max_length=200, verbose_name='Direccion Usuario')
    id_socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_usuario

class Terminos(models.Model):
    id_nuevos_productos = models.IntegerField( verbose_name='id nuevos productos')
    id_nov_ofertas = models.IntegerField( verbose_name='id novedades y ofertas')
    si_no = models.CharField(max_length=2, verbose_name='opcion si o no')
    
    def __str__(self):
        return self.si_no

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