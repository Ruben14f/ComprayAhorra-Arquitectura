from django.db import models

# Create your models here.
class Register(models.Model):
    nombre = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    
    def __str_(self):
        return self.nombre
    