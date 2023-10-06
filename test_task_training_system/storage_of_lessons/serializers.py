from rest_framework import serializers
from .models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'owner', 'name')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'products', 'name', 'video_link', 'duration')