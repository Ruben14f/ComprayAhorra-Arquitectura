from django.urls import path
from . import views

urlpatterns = [
   path('', views.carrito, name='cart'),
   path('agregar/', views.add, name='add'),
   path('eliminar/', views.remove, name='remove')
]