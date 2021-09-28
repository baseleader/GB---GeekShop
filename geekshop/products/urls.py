from django.contrib import admin
from django.urls import path

app_name = 'products'

from products.views import products, ProductDetail

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:id>', products, name='category'),
    path('page/<int:page>', products, name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]
