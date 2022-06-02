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