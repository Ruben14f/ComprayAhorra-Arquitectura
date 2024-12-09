from django.shortcuts import render
from products.models import Product
from .funciones import funcionCarrito
from .models import Cart, CartProduct


# Create your views here.
def carrito(request):
    cart = funcionCarrito(request)
    
    print(cart.products.all())
    
    
    return render(request, 'cart/cart.html',{
        'cart': cart
        
    })

def add(request):
    cart = funcionCarrito(request)

    product_id = request.POST.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
    except (ValueError, Product.DoesNotExist):
        return render(request, 'cart/error.html', {'message': 'Producto no encontrado o ID no válido'})

    # Añadir el producto a la tabla intermedia `CartProduct`
    if not CartProduct.objects.filter(cart=cart, product=product).exists():
        CartProduct.objects.create(cart=cart, product=product)

    return render(request, 'cart/add.html', {
        'product': product,
    })