from rest_framework import generics
from woman.models import Woman, Category
from woman.serializers import WomanSerializer


class WomanAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = WomanSerializer