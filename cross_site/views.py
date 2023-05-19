from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category, Tag, Product

def product1(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product2(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
