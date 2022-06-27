from django.urls import path
from .views import home, category,profile,registroproductos,modificarproductos,listarproductos,eliminarproductos,registro,productoxCategoria
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
    
     
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

