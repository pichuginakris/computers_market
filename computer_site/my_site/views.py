from django.shortcuts import render
import psycopg2
from create_main_page import main_page_creating
from create_sub_page import sub_page_creating
from create_product_page import product_page_creating, product_page_sorted_descending_creating,\
    product_page_sorted_ascending_creating, product_page_filter_55000, product_page_filter_15000, product_page_filter_56000


def beginning(request):
    main_page_creating()
    return render(request, "main_page.html")


def create_sub(request):
    if request.method == "POST":
        selectmain = request.POST.get("selectmain")
        sub_page_creating(selectmain)
    return render(request, "sub_page.html", {'selectmain': selectmain})


def create_products(request):
    if request.method == "POST":
        selectsub = request.POST.get("selectsub")
        product_page_creating(selectsub)
        product_page_sorted_descending_creating(selectsub)
        product_page_sorted_ascending_creating(selectsub)
        product_page_filter_55000(selectsub)
        product_page_filter_56000(selectsub)
        product_page_filter_15000(selectsub)
    return render(request, "product_page.html")


def download_csv(request):
    return render(request, 'products.csv')


def product_page_sorted_descending(request):
    return render(request, 'product_page_sorted_descending.html')


def product_page_sorted_ascending(request):
    return render(request, 'product_page_sorted_ascending.html')


def product_page_end_filter_55000(request):
    return render(request, 'product_page_end_filter_55000.html')


def product_page_end_filter_56000(request):
    return render(request, 'product_page_end_filter_56000.html')


def product_page_end_filter_15000(request):
    return render(request, 'product_page_end_filter_15000.html')


