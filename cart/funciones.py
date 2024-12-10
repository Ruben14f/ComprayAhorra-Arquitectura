from .models import Cart

def funcionCarrito(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id=cart_id).first()
    
    if cart is None:
        cart = Cart.objects.create(user=user)

    # Asignar el usuario al carrito si es necesario
    if user and cart.user is None:
        cart.user = user
        cart.save()

    # Almacenar el UUID del carrito en la sesión
    request.session['cart_id'] = str(cart.cart_id)

    return cart
