import uuid
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from enum import Enum
from django.db.models.signals import pre_save



class OrdenStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    
choices = [(tag,tag.value) for tag in OrdenStatus]
    
class Orden(models.Model):
    orderID = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=choices, default=OrdenStatus.CREATED)
    total = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.orderID

def enviarOrden(sender, instance, *args, **kwargs):
    if not instance.orderID:
        instance.orderID = str(uuid.uuid4())

pre_save.connect(enviarOrden, sender=Orden)