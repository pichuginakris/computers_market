from django.test import TestCase

from models.models import MainCategory, SubCategory, Product


class MainCategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        MainCategory.objects.create(name_main_category='Computers')

    def test_name_main_category_name_label(self):
        author = MainCategory.objects.get(id=1)
        field_label = author._meta.get_field('name_main_category').verbose_name
        self.assertEquals(field_label, 'name main category')

    def test_name_main_category_name_max_length(self):
        author = MainCategory.objects.get(id=1)
        max_length = author._meta.get_field('name_main_category').max_length
        self.assertEquals(max_length, 2000)


class SubCategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SubCategory.objects.create(name_main_category='Computer', name_sub_category='Market')

    def test_name_main_category_name_label(self):
        author = SubCategory.objects.get(id=1)
        field_label = author._meta.get_field('name_main_category').verbose_name
        self.assertEquals(field_label, 'name main category')

    def test_name_main_category_name_max_length(self):
        author = SubCategory.objects.get(id=1)
        max_length = author._meta.get_field('name_main_category').max_length
        self.assertEquals(max_length, 2000)

    def test_name_sub_category_name_label(self):
        author = SubCategory.objects.get(id=1)
        field_label = author._meta.get_field('name_sub_category').verbose_name
        self.assertEquals(field_label, 'name sub category')

    def test_name_sub_category_name_max_length(self):
        author = SubCategory.objects.get(id=1)
        max_length = author._meta.get_field('name_sub_category').max_length
        self.assertEquals(max_length, 2000)


class ProductCategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(product_name='ASUS', name_main_category='Computer', name_sub_category='Market',
                                   price='2', article='12441ew', picture_url='/bla.ru', characteristic='SUPER',
                                   description='Nice', goods_url='/tu.ru')

    def test_name_main_category_name_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('name_main_category').verbose_name
        self.assertEquals(field_label, 'name main category')

    def test_name_main_category_name_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('name_main_category').max_length
        self.assertEquals(max_length, 2000)

    def test_name_sub_category_name_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('name_sub_category').verbose_name
        self.assertEquals(field_label, 'name sub category')

    def test_name_sub_category_name_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('name_sub_category').max_length
        self.assertEquals(max_length, 2000)

    def test_product_name_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label, 'product name')

    def test_product_name_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('product_name').max_length
        self.assertEquals(max_length, 2000)

    def test_price_name_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_article_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('article').verbose_name
        self.assertEquals(field_label, 'article')

    def test_article_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('article').max_length
        self.assertEquals(max_length, 20000)

    def test_picture_url_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('picture_url').verbose_name
        self.assertEquals(field_label, 'picture url')

    def test_picture_url_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('picture_url').max_length
        self.assertEquals(max_length, 20000)

    def test_characteristic_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('characteristic').verbose_name
        self.assertEquals(field_label, 'characteristic')

    def test_characteristic_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('characteristic').max_length
        self.assertEquals(max_length, 20000)

    def test_description_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('description').max_length
        self.assertEquals(max_length, 20000)

    def test_goods_url_label(self):
        author = Product.objects.get(id=1)
        field_label = author._meta.get_field('goods_url').verbose_name
        self.assertEquals(field_label, 'goods url')

    def test_goods_url_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('goods_url').max_length
        self.assertEquals(max_length, 20000)
