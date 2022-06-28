from django.urls import path
from .views import home, category,profile,registroproductos,modificarproductos,listarproductos,eliminarproductos,registro,productoxCategoria,viewcart,agregar_producto,eliminar_producto,restar_producto,cleancart,procesar_compra,detalleProducto 
from django.conf import settings
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

app_name='core'

urlpatterns = [
    path('',home,name="home"),
    path('Categorias',category,name="category"),
      path('Perfil',profile,name="profile"),
      path('Añadir/',registroproductos,name="registroproductos"),
      path('Modificar/<id>/',modificarproductos,name="modificarproductos"),
      path('Listar/',listarproductos,name="listarproductos"),
      path('Eliminar/<id>/',eliminarproductos,name="eliminarproductos"),
      path('productocategoria/<id>/', views.productoxCategoria, name='productocategoria'),
      path('registro/', views.registro, name='registro'),
      path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    path('viewcart/', views.viewcart, name="viewcart"),
    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),
    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),
    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),
    path('cleancart/', views.cleancart, name="cleancart"),
    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

