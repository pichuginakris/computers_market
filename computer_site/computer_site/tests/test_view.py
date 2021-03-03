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



