from django.db import models
from django.contrib.auth.models import User
from front.models import Item

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    t_amount = models.DecimalField(max_digits=7, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'

    def save(self, *args, **kwargs):
        if not Order.objects.count():
            self.id = 52564
        else:
            self.id = Order.objects.last().id + 1
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    qty = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f'Order Item - {str(self.id)}'
