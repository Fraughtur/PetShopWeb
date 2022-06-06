from django.contrib import admin
from .models import Producto,Categoria, Usuario, Socio
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Socio)
