from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .carro import Carro
from core.forms import ProductoForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.

def home(request):
    
   

    busqueda = request.POST.get("buscador")
    product_list = Producto.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    
    return render(request, 'core/index.html',data)


def productoxCategoria(request, id):
    busqueda = request.POST.get("buscador")
    lista_productos = Producto.objects.filter(categoria = id)
    
    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        ).distinct()

    data = {'entity': lista_productos}
    return render(request, 'core/index.html', data)

def detalleProducto(request, id):
    product = get_object_or_404(Producto, id=id)
    otrosProductos = Producto.objects.filter(categoria=product.categoria)
    data = {
        'producto': product,
          'productosRelacionados': otrosProductos
    }
    return render(request, 'producto/detalle.html', data)


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

    producto =get_object_or_404(Producto, nombre=id)

    data ={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulariomodificarproducto= ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulariomodificarproducto.is_valid():
            formulariomodificarproducto.save()
            messages.success(request,"modificado correctamente")
            return redirect(to="core:listarproductos")
            data["form"] = formulariomodificarproducto

    return render(request,'core/ModificarProductos.html',data)


def eliminarproductos(request,id):
    producto = get_object_or_404(Producto, nombre_producto=id)
    producto.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="core:listarproductos")

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
            return redirect(to="core:home")
        else:
            data["form"] = formulario

    return render(request,'registration/registro.html',data)


def viewcart(request):
        return render(request, 'carrito/cart.html', {'carro': request.session['carro']})

def agregar_producto(request,producto_id ):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect(to="/viewcart")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect(to="/viewcart")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect(to="/viewcart")

def cleancart(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="/viewcart")


def procesar_compra(request):
    messages.success(request, 'Gracias por su Compra!!')
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('core:home')



class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer