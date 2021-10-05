from django.contrib import admin
from django.urls import path

from .views import OrderCreate, OrderItemsCreate, OrderList, OrderRead, OrderDelete, OrderUpdate, order_forming_complete

app_name = 'ordersapp'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderItemsCreate.as_view(), name='create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('forming-complete/<int:pk>/', order_forming_complete, name='forming_complete'),
]
