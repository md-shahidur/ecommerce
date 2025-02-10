from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/category/')
    description = models.CharField(max_length=100, null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='img/item/')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return str(self.name)
