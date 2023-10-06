from django import forms
from .models import Product, Lesson

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('owner', 'name')

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('name', 'video_link', 'duration', 'products')