from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Usuario 
from core.forms import ProductoForm, UsuarioForm

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

    producto =get_object_or_404(Producto, nombre_producto=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulariomodificarproducto= ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulariomodificarproducto.is_valid():
            formulariomodificarproducto.save()
            return redirect(to="listarproductos")
            data["form"] = formulariomodificarproducto

    return render(request,'core/ModificarProductos.html',data)


def eliminarproductos(request,id):
    producto = get_object_or_404(Producto, nombre_producto=id)
    producto.delete()
    return redirect(to="listarproductos")

def registro(request):

    data = {
        'regis': UsuarioForm()
    }

    return render(request,'core/Registro.html',data) 