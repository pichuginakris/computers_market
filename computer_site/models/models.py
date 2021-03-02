from django.db import models


class MainCategory(models.Model):
    name_main_category = models.CharField(max_length=2000, default="", editable=False)
    title = 'Main category'

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    name_sub_category = models.CharField(max_length=2000, default="", editable=False)
    name_main_category = models.CharField(max_length=20000)
    title = 'Sub category'

    def __str__(self):
        return self.title


class Product(models.Model):

    title = 'Products'
    product_name = models.CharField(max_length=2000, default="", editable=False)
    name_main_category = models.CharField(max_length=20000, default="")
    name_sub_category = models.CharField(max_length=20000)
    price = models.IntegerField(default="2")
    article = models.CharField(max_length=20000)
    picture_url = models.CharField(max_length=20000)
    characteristic = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    goods_url = models.CharField(max_length=20000)

    def __str__(self):
        return self.title
