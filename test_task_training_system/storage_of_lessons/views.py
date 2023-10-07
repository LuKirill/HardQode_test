from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Lesson, LessonAccess
from .serializers import ProductSerializer, LessonSerializer, LessonAccessSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonAccessSet(viewsets.ModelViewSet):
    queryset = LessonAccess.objects.all()
    serializer_class = LessonAccessSerializer
