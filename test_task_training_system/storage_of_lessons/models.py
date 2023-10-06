from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    country = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    allowed_actions = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()