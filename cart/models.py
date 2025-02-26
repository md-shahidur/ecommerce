from django.db import models
from front.models import Item
from django.contrib.auth.models import User

# Create your models here.


class CartItem(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='item')
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.name}'
