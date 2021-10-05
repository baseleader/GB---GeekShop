from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRD'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_CHOICES = (
        (FORMING, 'Формируется'),
        (SENT_TO_PROCEED, 'Отправлено в обработку'),
        (PAID, 'Оплачено'),
        (PROCEEDED, 'Обробатывается'),
        (READY, 'Готов к выдаче'),
        (CANCEL, 'Отмена заказа'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='create', auto_now_add=True)
    update = models.DateTimeField(verbose_name='update', auto_now=True)
    status = models.CharField(verbose_name='status', max_length=3, default=FORMING, choices=ORDER_CHOICES)

    is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.get_total_cost, items)))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)

    def get_product_cost(self):
        return self.products.price * self.quantity

    def __str__(self):
        return f'Текущий заказ {self.pk}'

