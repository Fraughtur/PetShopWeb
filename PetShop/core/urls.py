from django.urls import path
from .views import home, category,profile,registroproductos,modificarproductos,listarproductos,eliminarproductos,registro 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"),
    path('Categorias',category,name="category"),
      path('Perfil',profile,name="profile"),
      path('Añadir/',registroproductos,name="registroproductos"),
      path('Modificar/<id>/',modificarproductos,name="modificarproductos"),
      path('Listar/',listarproductos,name="listarproductos"),
      path('Eliminar/<id>/',eliminarproductos,name="eliminarproductos"),
      path('Registro/',registro,name="registro"),
     
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

