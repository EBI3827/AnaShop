from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

def home(request):
    context={
    'name':'Ebrahim'
    }
    return render(request, 'index.html', context)

class ProductListView(ListView):
    model=Product
    template_name='category.html'

class ProductDetailView(DetailView):
    model=Product
    template_name='product.html'
