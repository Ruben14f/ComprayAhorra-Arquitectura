from django.shortcuts import render
from products.models import Product
from .funciones import funcionCarrito

# Create your views here.
def carrito(request):
    cart = funcionCarrito(request)
    
    return render(request, 'cart/cart.html',{
        
    })

def add(request):
    cart = funcionCarrito(request)

    # Asegúrate de que el product_id se obtenga como un UUID
    product_id = request.POST.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # Maneja el caso de producto no encontrado
        return render(request, 'cart/error.html', {'message': 'Producto no encontrado'})

    cart.products.add(product)

    return render(request, 'cart/add.html', {'product': product})