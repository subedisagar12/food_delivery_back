from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class FoodView(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer
