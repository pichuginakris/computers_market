from django.db import models


class MainCategory(models.Model):
    nameMainCategory = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class SubCategory(MainCategory):
    nameSubCategory = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Product(SubCategory):
    objects = None
    name = 'India'
    price = models.CharField(max_length=20000)
    article = models.CharField(max_length=20000)
    picture_url = models.CharField(max_length=20000)
    characteristic = models.CharField(max_length=20000)
    description = models.CharField(max_length=20000)
    goods = models.CharField(max_length=20000)

    def __str__(self):
        return self.title
