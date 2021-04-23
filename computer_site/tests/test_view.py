from django.test import TestCase
from models.models import MainCategory, SubCategory, Product
import json


class ViewsMainTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        MainCategory.objects.create(name_main_category='Computers')

    def test_api_main_category_get_one_valid(self):
        author = MainCategory.objects.get(id=1)
        response = self.client.get('http://127.0.0.1:8000/api/main_category/' + str(author.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'name_main_category': 'Computers'})

    def test_api_main_category_post(self):
        response = self.client.post('http://127.0.0.1:8000/api/main_category/', {'name_main_category': 'Join'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MainCategory.objects.count(), 2)
        self.assertEqual(MainCategory.objects.get(id=2).name_main_category, 'Join')

    def test_api_main_category_get_one_invalid(self):
        response = self.client.get('http://127.0.0.1:8000/api/main_category/' + str(43525))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})

    def test_api_main_category_get_many(self):
        response = self.client.get('http://127.0.0.1:8000/api/main_category/')
        self.assertEqual(response.status_code, 200)

    def test_api_main_category_delete_valid(self):
        pk = 1
        response = self.client.delete('http://127.0.0.1:8000/api/main_category/' + str(pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), ["Main category with pk " + str(pk) + " deleted"])

    def test_api_main_category_delete_invalid(self):
        pk = 153267355
        response = self.client.delete('http://127.0.0.1:8000/api/main_category/' + str(pk))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})


class ViewSubCategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SubCategory.objects.create(name_main_category='Computer', name_sub_category='Market')

    def test_api_sub_category_many(self):
        response = self.client.get('http://127.0.0.1:8000/api/sub_category/')
        self.assertEqual(response.status_code, 200)

    def test_api_sub_category_one_valid(self):
        author = SubCategory.objects.get(id=1)
        response = self.client.get('http://127.0.0.1:8000/api/sub_category/' + str(author.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'name_main_category': 'Computer',
                                                        'name_sub_category': 'Market'})

    def test_api_sub_category_one_invalid(self):
        response = self.client.get('http://127.0.0.1:8000/api/sub_category/' + str(43525))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})

    def test_create_api_sub_loads_properly(self):
        response = self.client.post('http://127.0.0.1:8000/api/sub_category/', {'name_main_category': 'Join',
                                                                            'name_sub_category': 'KNS_Ноутбуки'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(SubCategory.objects.count(), 2)
        self.assertEqual(SubCategory.objects.get(id=2).name_main_category, 'Join')
        self.assertEqual(SubCategory.objects.get(id=2).name_sub_category, 'KNS_Ноутбуки')

    def test_api_sub_category_delete_valid(self):
        pk = 1
        response = self.client.delete('http://127.0.0.1:8000/api/sub_category/' + str(pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), ["Sub category with pk " + str(pk) + " deleted"])

    def test_api_sub_category_delete_invalid(self):
        pk = 153267355
        response = self.client.delete('http://127.0.0.1:8000/api/sub_category/' + str(pk))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})


class ViewProductTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(product_name='ASUS', name_main_category='Computer', name_sub_category='Market',
                                   price='2', article='12441ew', picture_url='/bla.ru', characteristic='SUPER',
                                   description='Nice', goods_url='/tu.ru')

    def test_product_one_valid(self):
        author = Product.objects.get(id=1)
        response = self.client.get('http://127.0.0.1:8000/api/product_category/' + str(author.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'product_name': 'ASUS',
                                                        'name_main_category': 'Computer',
                                                        'name_sub_category': 'Market',
                                                        'price': '2',
                                                        'article': '12441ew',
                                                        'picture_url': '/bla.ru',
                                                        'characteristic': 'SUPER',
                                                        'description': 'Nice',
                                                        'goods_url': '/tu.ru',
                                                        })

    def test_product_one_invalid(self):
        pk = 457577474
        response = self.client.get('http://127.0.0.1:8000/api/product_category/' + str(pk))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})

    def test_api_product_many(self):
        response = self.client.get('http://127.0.0.1:8000/api/product_category/')
        self.assertEqual(response.status_code, 200)

    def test_create_api_product_loads_properly(self):
        integ = 35
        response = self.client.post('http://127.0.0.1:8000/api/product_category/', {'name_main_category': 'Join',
                                                                                'name_sub_category': 'JOIN_Ноутбуки',
                                                                                'product_name': 'Ноутбук ac',
                                                                                'price': integ,
                                                                                'article': '3525',
                                                                                'picture_url': 'sfl.efr',
                                                                                'characteristic': 'Ноутбук хороший',
                                                                                'description': 'desc',
                                                                                'goods_url': 'goods_url'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.get(id=2).name_main_category, 'Join')
        self.assertEqual(Product.objects.get(id=2).name_sub_category, 'JOIN_Ноутбуки')
        self.assertEqual(Product.objects.get(id=2).product_name, 'Ноутбук ac')
        self.assertEqual(Product.objects.get(id=2).price, integ)
        self.assertEqual(Product.objects.get(id=2).article, '3525')
        self.assertEqual(Product.objects.get(id=2).picture_url, 'sfl.efr')
        self.assertEqual(Product.objects.get(id=2).characteristic, 'Ноутбук хороший')
        self.assertEqual(Product.objects.get(id=2).description, 'desc')
        self.assertEqual(Product.objects.get(id=2).goods_url, 'goods_url')

    def test_api_product_delete_valid(self):
        pk = 1
        response = self.client.delete('http://127.0.0.1:8000/api/product_category/' + str(pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), ["Product with pk " + str(pk) + " deleted"])

    def test_api_product_delete_invalid(self):
        pk = 153267355
        response = self.client.delete('http://127.0.0.1:8000/api/product_category/' + str(pk))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'detail': 'Not found.'})


