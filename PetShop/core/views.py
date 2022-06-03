from django.shortcuts import render
from .models import Producto
from core.forms import ProductoForm

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def category(request):

    productos = Producto.objects.all()

    datosproducto={
        'productos': productos
    }

    return render(request, 'core/categorias.html',datosproducto)


def profile(request):
    return render(request, 'core/Perfil.html')

def registroproductos(request):

    productonuevo ={
        'form':ProductoForm()
    }

    return render(request,'core/RegistroProductos.html',productonuevo)