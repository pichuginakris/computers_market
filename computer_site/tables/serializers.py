from rest_framework import serializers
from .models import MainCategory, SubCategory, Product


class MainCategorySerializer(serializers.Serializer):
    nameMainCategory = serializers.CharField(max_length=20000)

    def update(self, instance, validated_data):
        instance.nameMainCategory = validated_data.get('nameMainCategory', instance.title)
        instance.save()
        return instance

    def create(self, validated_data):
        return MainCategory.objects.create(**validated_data)
