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


def products(request, id=None, page=1):
    products = Product.objects.filter(category_id=id) if id != None else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'title': 'Каталог', 'category': ProductsCategory.objects.all(), 'products': products_paginator}
    return render(request, 'products/products.html', context)
