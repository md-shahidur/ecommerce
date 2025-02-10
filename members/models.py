from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=50, null=True, blank=True, unique=True)
    mobile = models.CharField(
        max_length=11,
        validators=[RegexValidator(
            # Example regex for international phone numbers
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '01234567890'. Up to 11 digits allowed."
        )]
    )
    address = models.CharField(max_length=50, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    pro_pic = models.ImageField(
        null=True, blank=True, upload_to='img/profile/')

    def __str__(self):
        return str(self.user)
