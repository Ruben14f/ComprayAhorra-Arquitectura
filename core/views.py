from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth import logout as lgout

# Create your views here.
def home(request):
    productos = Product.objects.all()
    return render(request, 'core/inicio.html', {
        'productos' : productos
    })
    
def logout(request):
    lgout(request)
    return redirect('inicio')


