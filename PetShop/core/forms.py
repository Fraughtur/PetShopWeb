from django import forms
from django.forms import ModelForm
from .models import Producto, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductoForm(ModelForm):
    class Meta:
            model = Producto
      
            fields ='__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"email","password1","password2"]


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ["nombre"]

      