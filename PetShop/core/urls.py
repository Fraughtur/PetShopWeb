from django.urls import path
from .views import home, category,profile,registroproductos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"),
    path('Petshop/category/',category,name="category"),
      path('Petshop/profile/',profile,name="profile"),
      path('new/',registroproductos,name="registroproductos"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

