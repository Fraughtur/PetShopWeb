from django.urls import path
from .views import home, category,profile,registroproductos,modificarproductos,eliminarproducto,listarproductos 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"),
    path('Petshop/category/',category,name="category"),
      path('Petshop/profile/',profile,name="profile"),
      path('new/',registroproductos,name="registroproductos"),
      path('modify/<id>/',modificarproductos,name="modificarproductos"),
      path('eliminarproducto/<id>',eliminarproducto,name="eliminarproducto"),
      path('list/',listarproductos,name="listarproductos"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

