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
        # Create an article from the above data
        serializer = MainCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Main category '{}' created successfully".format(article_saved.title)})


class SubCategoryView(APIView):
    @staticmethod
    def get(request):
        articles = SubCategory.objects.all()
        serializer = SubCategorySerializer(articles, many=True)
        return Response({"Sub category": serializer.data})

    @staticmethod
    def post(request):
        # Create an article from the above data
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Sub category '{}' created successfully".format(article_saved.title)})


class ProductView(APIView):
    @staticmethod
    def get(request):
        articles = Product.objects.all()
        serializer = ProductSerializer(articles, many=True)
        return Response({"Product ": serializer.data})

    @staticmethod
    def post(request):

        # Create an article from the above data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(article_saved.title)})


