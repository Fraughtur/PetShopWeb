from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario


class ProductoForm(ModelForm):
    class Meta:
            model = Producto
           # fields =['nombre_producto','descripcion_producto','precio_producto','stock_producto','imagen_producto','categoria']
            fields ='__all__'

class UsuarioForm(ModelForm):
    class Meta:
            model = Usuario
           # fields =['nombre_producto','descripcion_producto','precio_producto','stock_producto','imagen_producto','categoria']
            fields ='__all__'

