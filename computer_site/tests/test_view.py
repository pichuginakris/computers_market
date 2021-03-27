from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_create_sub_loads_properly(self):
        response = self.client.post('http://127.0.0.1:8000/create_sub/', {'selectmain': 'KNS_Ноутбуки'})
        self.assertEqual(response.status_code, 200)

    def test_create_products_loads_properly(self):
        response = self.client.post('http://127.0.0.1:8000/create_sub/create_products/', {'selectsub': 'Компьютеры Acer'})
        self.assertEqual(response.status_code, 200)

    def test_product_page_sorted_descending_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/product_page_sorted_descending.html/')
        self.assertEqual(response.status_code, 200)

    def test_product_page_sorted_ascending_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/product_page_sorted_ascending.html/')
        self.assertEqual(response.status_code, 200)

    def test_filter_15000_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/product_page_end_filter_15000.html/')
        self.assertEqual(response.status_code, 200)

    def test_filter_56000_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/product_page_end_filter_56000.html/')
        self.assertEqual(response.status_code, 200)

    def test_filter_55000_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/product_page_end_filter_55000.html/')
        self.assertEqual(response.status_code, 200)

    def test_load_csv(self):
        response = self.client.get('http://127.0.0.1:8000/create_sub/create_products/products.csv/')
        self.assertEqual(response.status_code, 200)

    def test_api_sub_category(self):
        response = self.client.get('http://127.0.0.1:8000/api/sub_category/')
        self.assertEqual(response.status_code, 200)

    def test_api_main_category(self):
        response = self.client.get('http://127.0.0.1:8000/api/main_category/')
        self.assertEqual(response.status_code, 200)

    def test_api_product_category(self):
        response = self.client.get('http://127.0.0.1:8000/api/product_category/')
        self.assertEqual(response.status_code, 200)

    def test_create_api_main_loads_properly(self):
        response = self.client.post('http://127.0.0.1:8000/api/main_category/', {'name_main_category': 'Join'})
        self.assertEqual(response.status_code, 200)

    def test_create_api_sub_loads_properly(self):
        response = self.client.post('http://127.0.0.1:8000/api/sub_category/', {'name_main_category': 'Join',
                                                                                'name_sub_category': 'KNS_Ноутбуки'})
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


