from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=50, null=True, blank=True, unique=True)
    mobile = models.IntegerField(
        null=True, blank=True, unique=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    pro_pic = models.ImageField(
        null=True, blank=True, upload_to='img/profile/')

    def __str__(self):
        return str(self.user)
