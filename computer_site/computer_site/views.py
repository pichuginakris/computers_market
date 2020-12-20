from django.shortcuts import render
import psycopg2
from create_main_page import main_page_creating
from create_sub_page import sub_page_creating
from create_product_page import product_page_creating

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
    return render(request, "product_page.html", {'selectsub': selectsub})


