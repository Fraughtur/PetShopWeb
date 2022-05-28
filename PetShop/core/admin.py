from django.contrib import admin
from .models import Usuario, Socio, Descuento, Terminos, Producto,Categoria,Region, Comuna

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Socio)
admin.site.register(Descuento)
admin.site.register(Terminos)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Region)
admin.site.register(Comuna)

