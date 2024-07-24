from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_product(request):
    return HttpResponse('New Product')

