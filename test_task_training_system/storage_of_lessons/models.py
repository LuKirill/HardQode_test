from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField()
