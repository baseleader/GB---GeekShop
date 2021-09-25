from django.contrib import admin
from baskets.models import Basket


class BasketAdmin(admin.TabularInline):
    fields = ('product', 'created_timestamp', 'quantity')
    readonly_fields = ('created_timestamp',)
    model = Basket
    extra = 0