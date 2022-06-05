from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from core.forms import ProductoForm

# Create your views here.

def home(request):
    
    productos = Producto.objects.all()
    datosproducto={
        'productos': productos
    }

    return render(request, 'core/index.html',datosproducto)

def category(request):

    productos = Producto.objects.all()

    datosproducto={
        'productos': productos
    }

    return render(request, 'core/categorias.html',datosproducto)


def profile(request):
    return render(request, 'core/Perfil.html')

def listarproductos(request):

    productos = Producto.objects.all()

    datosproducto = {
        'productos': productos
    }

    return render(request, 'core/lista_productos.html',datosproducto)

def registroproductos(request):

    productonuevo ={
        'form': ProductoForm()
    }

    if request.method== 'POST':
        formularioregistroproducto = ProductoForm(data=request.POST, files=request.FILES)
        if formularioregistroproducto.is_valid(): 
            formularioregistroproducto.save()
        productonuevo['mensajeproducto'] = "Producto agregado exitosamente"
    return render(request,'core/RegistroProductos.html',productonuevo)

def modificarproductos(request, id):
 
    productos = get_object_or_404(Producto, nombre_producto=id)

    datamodify ={
        'form': ProductoForm(instance=productos)
    }

    if request.method== 'POST':
         formulariomodificarproducto = ProductoForm(data=request.POST, instance=productos , files=request.FILES)
         if formulariomodificarproducto.is_valid(): 
            formulariomodificarproducto.save()
    return redirect(to="listarproductos")

    return render(request,'core/ModificarProductos.html', datamodify)

def eliminarproducto(request, id):
    productos = get_object_or_404(Producto,nombre_producto=id)
    productos.delete()
    return redirect(to="listarproductos")

