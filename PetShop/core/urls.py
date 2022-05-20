from unicodedata import category, name
from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name="home"),
    path('Petshop/category/', category, name="category"),
]
