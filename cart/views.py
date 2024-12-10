from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .funciones import funcionCarrito
from .models import CartProduct
from django.db.models import F





# Create your views here.
def carrito(request):    
    cart = funcionCarrito(request)
    
    print(cart.products.all())
    
    
    return render(request, 'cart/cart.html',{
        'cart': cart
    })

def add(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    product_cart = CartProduct.objects.crearActualizar(cart=cart, product=product, quantity=quantity)
    
    
    
    
    # Verificar si el producto ya está en el carrito
    # cart_product = cart.cartproduct_set.filter(product=product).first()

    # if cart_product:
    #     # Incrementar la cantidad existente
    #     cart_product.quantity = F('quantity') + quantity
    #     cart_product.save()
    # else:
    #     # Agregar el producto si no existe en el carrito
    
    # cart.products.add(product, through_defaults={
    #     'quantity': quantity
    # })

    return render(request, 'cart/add.html', {
        'product': product,
    })
    
def remove(request):
    cart = funcionCarrito(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    
    cart.products.remove(product)
    
    return redirect('cart')
    