from django.shortcuts import render
from .utils import funcionOrden
from cart.funciones import funcionCarrito
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart,CartProduct
from orden.models import Orden


def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)
        
    return render(request, 'orden/orden.html',{
        'cart' : cart
    })

def procesar_pago(request):
    cart = funcionCarrito(request)
    
    CartProduct.objects.filter(cart=cart).delete()
    
    return render(request, 'orden/compra_exitosa.html', {
        'mensaje': '¡Compra Exitosa!'
    })

