from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductsCategory

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request, id=None):
    context = {'title': 'Каталог',
               'category': ProductsCategory.objects.all(),
               }
    if id == 7:
        products_filter = Product.objects.all()
        context['products'] = products_filter
    else:
        context.update({'products': Product.objects.filter(category_id=id) if id != None else Product.objects.all()})
    return render(request, 'products/products.html', context)
