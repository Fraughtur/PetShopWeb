from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from core.forms import ProductoForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib import messages
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

    page=request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 5)
        productos= paginator.page(page)
    except:
        raise Http404

    datosproducto = {
        'entity': productos ,
        'paginator': paginator
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
        messages.success(request,"Producto Registrado")
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
            messages.success(request,"modificado correctamente")
            return redirect(to="listarproductos")
            data["form"] = formulariomodificarproducto

    return render(request,'core/ModificarProductos.html',data)


def eliminarproductos(request,id):
    producto = get_object_or_404(Producto, nombre_producto=id)
    producto.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="listarproductos")

def registro(request):

    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado Correctamente")
            return redirect(to="home")
            data["form"] = formulario

    return render(request,'registration/registro.html',data)