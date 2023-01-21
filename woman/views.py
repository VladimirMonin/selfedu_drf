from django.http import JsonResponse
from requests import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView

from woman.models import Woman, Category
from woman.serializers import WomanSerializer, CategorySerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
