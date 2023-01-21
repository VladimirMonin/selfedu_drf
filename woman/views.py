from django.http import JsonResponse
from requests import Response
from rest_framework import generics
from rest_framework.views import APIView

from woman.models import Woman, Category
from woman.serializers import WomanSerializer, CategorySerializer


# class WomanAPIView(APIView):
#     def get(self, request):
#         data = Woman.objects.all().values()
#         return JsonResponse({'posts': list(data)})
#
#     def post(self, request):
#         return JsonResponse({'status': 200})


class WomanAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

