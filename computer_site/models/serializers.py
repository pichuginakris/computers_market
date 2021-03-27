from rest_framework import serializers
from .models import MainCategory, SubCategory, Product


class MainCategorySerializer(serializers.Serializer):
    name_main_category = serializers.CharField(max_length=2000)

    def update(self, instance, validated_data):
        instance.name_main_category = validated_data.get('name_main_category', instance.title)
        instance.save()
        return instance

    def create(self, validated_data):
        return MainCategory.objects.create(**validated_data)


class SubCategorySerializer(serializers.Serializer):
    name_sub_category = serializers.CharField(max_length=2000)
    name_main_category = serializers.CharField(max_length=2000)

    def update(self, instance, validated_data):
        instance.name_sub_category = validated_data.get('name_sub_category', instance.title)
        instance.name_main_category = validated_data.get('name_main_category', instance.title)
        instance.save()
        return instance

    def create(self, validated_data):
        return SubCategory.objects.create(**validated_data)


class ProductSerializer(serializers.Serializer):
    name_main_category = serializers.CharField(max_length=20000)
    name_sub_category = serializers.CharField(max_length=20000)
    product_name = serializers.CharField(max_length=20000)
    price = serializers.CharField(max_length=20000)
    article = serializers.CharField(max_length=20000)
    picture_url = serializers.CharField(max_length=20000)
    characteristic = serializers.CharField(max_length=20000)
    description = serializers.CharField(max_length=20000)
    goods_url = serializers.CharField(max_length=20000)

    def update(self, instance, validated_data):
        instance.name_sub_category = validated_data.get('name_sub_category', instance.title)
        instance.name_main_category = validated_data.get('name_main_category', instance.title)
        instance.product_name = validated_data.get('product_name', instance.title)
        instance.price = validated_data.get('price', instance.title)
        instance.article = validated_data.get('article', instance.title)
        instance.picture_url = validated_data.get('picture_url', instance.title)
        instance.characteristic = validated_data.get('characteristic', instance.title)
        instance.description = validated_data.get('description', instance.title)
        instance.goods_url = validated_data.get('goods_url', instance.title)
        instance.save()
        return instance

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

