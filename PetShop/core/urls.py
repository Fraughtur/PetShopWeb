from django.urls import path, include
from .views import home,profile,registroproductos,modificarproductos,listarproductos,eliminarproductos,registro,productoxCategoria,viewcart,agregar_producto,eliminar_producto,restar_producto,cleancart,procesar_compra,detalleProducto, ProductoViewset 
from django.conf import settings
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

app_name='core'

urlpatterns = [
    path('',home,name="home"),
      path('Perfil',profile,name="profile"),
      path('Añadir/',registroproductos,name="registroproductos"),
      path('Modificar/<id>/',modificarproductos,name="modificarproductos"),
      path('Listar/',listarproductos,name="listarproductos"),
      path('Eliminar/<id>/',eliminarproductos,name="eliminarproductos"),
      path('productocategoria/<id>/', productoxCategoria, name='productocategoria'),
      path('registro/', registro, name='registro'),
      path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    path('viewcart/', viewcart, name="viewcart"),
    path('addcart/<producto_id>/', agregar_producto, name="addcart"),
    path('delcart/<producto_id>/', eliminar_producto, name="delcart"),
    path('restarcart/<producto_id>/', restar_producto, name="restarcart"),
    path('cleancart/', cleancart, name="cleancart"),
    path('procesar_compra/', procesar_compra, name="procesar_compra"),
    path('detalleproducto/<id>/', detalleProducto, name='detalleproducto'),
    path('api/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

