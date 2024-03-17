from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField('product.Product', blank=True)
    banner = models.ImageField(upload_to='seller/banner', blank=True, null=True)
    store_name = models.CharField(max_length=255, default='')
    store_description = models.TextField(default='')

    def __str__(self):
        return self.store_name

    def get_products(self):
        return self.products.all()
