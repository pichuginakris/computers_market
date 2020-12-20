import requests
import re
from bs4 import BeautifulSoup
import transliterate
from add_data_to_bd import creating_sub_category, creating_products, creating_main_category,  delete_all_information


def find_product_data(reference, nameMainCategory, nameSubCategory):
    try:
        response = requests.get(reference)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        product_name_parts = soup.find('h1').text.strip()
        print(product_name_parts)
        try:
            price = soup.find('span', class_='price-val').text.strip()
        except:
            price = ''
        print(price)
        image = soup.find('div', class_='col-12 col-sm-10').find('img').get('src')
        print(image)
        characteristics = soup.find('div', class_='row no-gutters mb-2').text.split()
        info = ''
        for characteristic in characteristics:
            info = info + ' ' + characteristic
        product_characteristic = (info.strip())
        print(product_characteristic)
        article = soup.find('div', class_='sku').text.strip()
        print(article)
        try:
            product_description = (soup.find('div', id='goodsinfo').find('div', class_='my-3')).text
            print(product_description)
        except:
            product_description = ''
        data = {
                'product_name': product_name_parts.strip(),
                 'nameMainCategory': nameMainCategory.strip(),
                 'nameSubCategory': nameSubCategory.strip(),
                 'price': price.strip(),
                 'article': article.strip(),
                 'picture_url': image.strip(),
                 'characteristic': product_characteristic.strip(),
                 'description': product_description.strip(),
                 'goods_url': reference
        }
        creating_products(data)
    except:
        print('er')


def find_all_products(nameMainCategory, subcategory_name, subcategory_href):
    pattern = subcategory_href + 'page{}/'
    p = 1
    while p<20:
        try:
            subcategory_href = pattern.format(p)
            response = requests.get(subcategory_href)
            print(subcategory_href)
            p = p + 1
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            all_tables = soup.find_all('div', class_='item col-6 col-md-3 col-lg col-xl-3 border bg-white')
            for table in all_tables:
                product_href = 'https://www.kns.ru' + table.find('a', class_='img').get('href')
                find_product_data(product_href, 'KNS_' + str(nameMainCategory), subcategory_name)
                print(product_href)
        except:
            break


def find_sub_categories(name, href):
    response = requests.get(href)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    find_block = soup.find('ul', class_='menu-cat').find(string=re.compile(name))
    find_list_childes = find_block.parent.next_sibling.next_sibling.find_all('a')
    for child in find_list_childes:
        subcategory_name = child.text
        creating_sub_category(subcategory_name, 'KNS_' + str(name))
        print(subcategory_name)
        subcategory_href = 'https://www.kns.ru' + child.get('href')
        find_all_products(name, subcategory_name, subcategory_href)


def find_main_category():
    # Main page
    url = 'https://kns.ru//'
    delete_all_information()
    # Request html main page
    try:
        html = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print('Error with connection!')
        return
    soup = BeautifulSoup(html, 'lxml')
    find_table = soup.find('ul', class_='menu-cat').find('li')
    main_category = find_table.find('a')
    while main_category != -1:
        main_category_name = main_category.text
        main_category_href = 'https://www.kns.ru' + main_category.get('href')
        print(main_category_href)
        creating_main_category('KNS_' + str(main_category_name))
       # print(transliterate.translit(str(main_category_name), reversed=True))
        find_sub_categories(main_category_name, main_category_href)
        find_table = find_table.next_sibling
        main_category = find_table.find('a')


if __name__ == '__main__':
    find_main_category()
