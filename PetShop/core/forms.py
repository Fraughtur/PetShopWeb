from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoForm(ModelForm):
    class Meta:
            model = Producto
            fields =['nombre_producto','descripcion_producto','precio_producto','stock_producto','imagen_producto','categoria']
            labels ={
                'nombre': '',
               'descripcion': '',
              'precio': '',
             'stock': '',
             'imagen': '',
             'categoria': '',
            }