from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def category(request):
    return render(request, 'core/categorias.html')
def profile(request):
    return render(request, 'core/Perfil.html')