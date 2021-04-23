from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import MainCategory, SubCategory, Product
from .serializers import MainCategorySerializer, SubCategorySerializer, ProductSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404


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


class MainCategoryView_v2(APIView):
    @staticmethod
    def get(request, pk):
        try:
            puppy = MainCategory.objects.get(pk=pk)
            serializer = MainCategorySerializer(puppy)
            return Response(serializer.data)
        except MainCategory.DoesNotExist:
            raise Http404("MainCategory does not exist")

    @staticmethod
    def delete(request, pk):
        try:
            puppy = MainCategory.objects.get(pk=pk)
            puppy.delete()
            return Response({"Main category with pk " + str(pk) + " deleted"})
        except MainCategory.DoesNotExist:
            raise Http404("MainCategory does not exist")


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


class SubCategoryView_v2(APIView):
    @staticmethod
    def get(request, pk):
        try:
            puppy = SubCategory.objects.get(pk=pk)
            serializer = SubCategorySerializer(puppy)
            return Response(serializer.data)
        except SubCategory.DoesNotExist:
            raise Http404("Sub category does not exist")

    @staticmethod
    def delete(request, pk):
        try:
            puppy = SubCategory.objects.get(pk=pk)
            puppy.delete()
            return Response({"Sub category with pk " + str(pk) + " deleted"})
        except SubCategory.DoesNotExist:
            raise Http404("SubCategory does not exist")



class ProductView_v2(APIView):
    @staticmethod
    def get(request, pk):
        try:
            puppy = Product.objects.get(pk=pk)
            serializer = ProductSerializer(puppy)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")


    @staticmethod
    def delete(request, pk):
        try:
            puppy = Product.objects.get(pk=pk)
            puppy.delete()
            return Response({"Product with pk " + str(pk) + " deleted"})
        except Product.DoesNotExist:
            raise Http404("Product does not exist")


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


