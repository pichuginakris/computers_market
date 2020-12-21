from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import MainCategory, SubCategory, Product
from .serializers import MainCategorySerializer, SubCategorySerializer, ProductSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


class MainCategoryView(APIView):
    @staticmethod
    def get(request):
        articles = MainCategory.objects.all()
        serializer = MainCategorySerializer(articles, many=True)
        return Response({"Main category": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("name_main_category")
        # Create an article from the above data
        serializer = MainCategorySerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Main category '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(MainCategory.objects.all(), pk=pk)
        data = request.data.get('name_main_category')
        serializer = MainCategorySerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Main category '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(request, pk):
        # Get object with this pk
        data = request.data.get('name_main_category')
        article = MainCategory.objects.get(pk=pk)
        article.delete()
        return Response({
            "message": "Main category with id `{}` has been deleted.".format(pk)
        }, status=204)


class SubCategoryView(APIView):
    @staticmethod
    def get(request):
        articles = SubCategory.objects.all()
        serializer = SubCategorySerializer(articles, many=True)
        return Response({"Sub category": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("name_sub_category")
        # Create an article from the above data
        serializer = SubCategorySerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Sub category '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(SubCategory.objects.all(), pk=pk)
        data = request.data.get('name_sub_category')
        serializer = SubCategorySerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Sub category '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(request, pk):
        # Get object with this pk
        data = request.data.get('name_sub_category')
        article = SubCategory.objects.get(pk=pk)

        article.delete()
        return Response({
            "message": "Sub category with id `{}` has been deleted.".format(pk)
        }, status=204)


class ProductView(APIView):
    @staticmethod
    def get(request):
        articles = Product.objects.all()
        serializer = ProductSerializer(articles, many=True)
        return Response({"Product ": serializer.data})

    @staticmethod
    def post(request):
        article = request.data.get("product_name")
        # Create an article from the above data
        serializer = ProductSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(article_saved.title)})

    @staticmethod
    def put(request, pk):
        saved_article = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data.get('product_name')
        serializer = ProductSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Product '{}' updated successfully".format(article_saved.title)
        })

    @staticmethod
    def delete(request, pk):
        # Get object with this pk
        data = request.data.get('product_name')
        print(pk)
        article=Product.objects.get(pk=pk)

        article.delete()
        return Response({
            "message": "Product with id `{}` has been deleted.".format(pk)
        }, status=204)

