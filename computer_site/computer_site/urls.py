"""computer_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from computer_site import views

urlpatterns = [
    path('', views.beginning),
    path('create_sub/', views.create_sub),
    path('create_sub/create_products/', views.create_products),
    path('create_sub/create_products/products.csv/', views.download_csv),
    path('create_sub/create_products/product_page_sorted_descending.html/', views.product_page_sorted_descending),
    path('create_sub/create_products/product_page_sorted_ascending.html/', views.product_page_sorted_ascending),
    path('create_sub/create_products/product_page_end_filter_15000.html/', views.product_page_end_filter_15000),
    path('create_sub/create_products/product_page_end_filter_56000.html/', views.product_page_end_filter_56000),
    path('create_sub/create_products/product_page_end_filter_55000.html/', views.product_page_end_filter_55000),

    path('admin/', admin.site.urls),
    path('api/', include('models.urls')),
]
