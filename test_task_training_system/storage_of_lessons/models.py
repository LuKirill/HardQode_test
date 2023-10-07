from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration = models.IntegerField("duration (sec)")

class LessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.PositiveIntegerField(default=0)
    viewed_status = models.CharField(max_length=20, default='Не просмотрено')