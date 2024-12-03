from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product

# Create your views here.
def home(request):
    productos = Product.objects.all()
    return render(request, 'core/inicio.html', {
        'productos' : productos
    })


