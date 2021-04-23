from django.test import TestCase
from pars.xpert import find_main_category, find_all_products
from pars.kns import find_main_category_kns, find_sub_categories_kns, find_all_products_kns
from pars.computermarket import find_main_category_comp, find_sub_categories_comp, find_all_products_comp, find_product_data_comp



class ViewsTestCase(TestCase):

    def test_connecton_to_xpert(self):
        k = 1
        response = find_main_category(k)
        self.assertEqual(response.status_code, 200)

    def test_table_exist_xpert(self):
        k = 2
        response = find_main_category(k)
        assert response > 0

    def test_data_exist_xpert(self):
        k = 3
        main_category_name = 'Услуги по сборке'
        main_category_href = 'https://www.xpert.ru/products.php?category_id=307'
        prodict_name = find_all_products(main_category_name, main_category_href, k)
        assert prodict_name != 'Отсутствует'

    def test_connecton_to_kns(self):
        k = 1
        response = find_main_category_kns(k)
        self.assertEqual(response.status_code, 200)

    def test_table_exist_kns(self):
        k = 2
        response = find_main_category_kns(k)
        assert response > 0

    def test_find_sub_categories_kns(self):
        k = 3
        name = 'Ноутбуки'
        href = 'https://www.kns.ru/catalog/noutbuki/'
        response = find_sub_categories_kns(name, href, k)
        assert len(response) > 0

    def test_find_all_products_kns(self):
        k = 3
        nameMainCategory = 'Ноутбуки'
        subcategory_name = 'Ноутбуки Acer'
        subcategory_href = 'https://www.kns.ru/catalog/noutbuki/acer/'
        response = find_all_products_kns(nameMainCategory, subcategory_name, subcategory_href, k)
        assert response != 'er'

    def test_connecton_to_computermarket(self):
        k = 1
        response = find_main_category_comp(k)
        self.assertEqual(response.status_code, 200)

    def test_table_exist_computermarket(self):
        k = 2
        response = find_main_category_comp(k)
        assert response > 0

    def test_find_sub_categories_computermarket(self):
        k = 3
        name = 'Компьютеры, Ноутбуки, Планшеты'
        href = 'https://www.computermarket.ru/main/catalog/catid/1.aspx'
        response = find_sub_categories_comp(name, href, k)
        assert len(response) > 0

    def test_find_all_products_computermarket(self):
        k = 3
        nameMainCategory = 'COMPUTER_MARKET_Компьютеры, Ноутбуки, Планшеты'
        subcategory_name = 'Планшеты'
        subcategory_href = 'https://www.computermarket.ru/main/catalog/catid/1832688.aspx'
        response = find_product_data_comp(nameMainCategory, subcategory_name, subcategory_href, k)
        assert response != ''