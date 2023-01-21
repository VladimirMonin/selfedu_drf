from rest_framework import serializers

from woman.models import Woman, Category


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
