from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(ModelForm):
    class Meta:
            model = Producto
           # fields =['nombre_producto','descripcion_producto','precio_producto','stock_producto','imagen_producto','categoria']
            fields ='__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]