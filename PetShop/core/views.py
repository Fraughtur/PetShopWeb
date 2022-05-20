from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/index.html')
def catgory(request):
    return render(request, 'core/categorias.html')

