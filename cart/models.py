from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed, post_save
import uuid

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)
    
    def update_totals(self):
        self.update_total()

    def update_total(self):
        self.total = sum([i.quantity * i.product.price for i in self.product_related()])
        self.save()
        

    def product_related(self):
        return self.cartproduct_set.select_related('product')
        
class CartProductManager(models.Manager):
    def crearActualizar(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)
        
        if not created:
            quantity = object.quantity + quantity
        object.update_quantity(quantity)
        return object
            
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)     
    create_at = models.DateTimeField(auto_now_add=True)
    
    objects = CartProductManager()
    
    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()
        
    def get_subtotal(self):
        """Devuelve el subtotal para este producto"""
        return self.quantity * self.product.price
        
# Señal para generar cart_id automáticamente antes de guardar
def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.update_totals()
        
def postActualizar(sender, instance, *args, **kwargs):
        instance.cart.update_totals()
        
        
post_save.connect(postActualizar, sender=CartProduct)
pre_save.connect(set_cart_id, sender=Cart)
m2m_changed.connect(update_totals, sender=Cart.products.through)


