from django.urls import path
from . import views

urlpatterns = [
   path('', views.orden, name='orden_formulario'),
   path('procesar/', views.procesar_pago, name='procesar_pago'),
]