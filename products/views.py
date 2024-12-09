from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.db.models import Q

# Create your views here.
class ProductListView(ListView):
    template_name = 'core/inicio.html'
    queryset = Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for producto in context['object_list']:
            producto.price = '${:,.0f}'.format(producto.price).replace(',', '.')
            
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'].price = '${:,.0f}'.format(context['object'].price).replace(',', '.')
            
        return context
    
    