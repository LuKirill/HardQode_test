from rest_framework import serializers
from .models import Product, Lesson, LessonAccess

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'owner', 'name')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'products', 'name', 'video_link', 'duration')

class LessonAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAccess
        fields = ('user', 'lesson', 'viewed_time', 'viewed_status')