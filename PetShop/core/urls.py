from django.urls import path
from .views import home, category


urlpatterns = [
    path('',home,name="home"),
    path('Petshop/category/',category,name="category"),
]

