from django.urls import path
from .views import home, category,profile 


urlpatterns = [
    path('',home,name="home"),
    path('Petshop/category/',category,name="category"),
      path('Petshop/profile/',category,name="profile"),
]

