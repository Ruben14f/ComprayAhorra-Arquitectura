import uuid
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save
# Create your models here.
class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cart_id)
    
    @property
    def products(self):
        # Devuelve todos los productos relacionados a través de la tabla intermedia `CartProduct`
        return self.cartproduct_set.all()
    
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, db_column='cart_id', to_field='cart_id')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('cart', 'product')
        db_table = 'cart_product'  

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())

pre_save.connect(set_cart_id, sender=Cart)