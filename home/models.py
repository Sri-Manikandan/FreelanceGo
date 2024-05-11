from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=12,null=True,unique=True)
    def __str__(self):
        return self.name
