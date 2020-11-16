import requests
from bs4 import BeautifulSoup


# Get product data
def find_product_data(reference):
    response = requests.get(reference)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # Find a name and delete from a name blank lines with strip()
    product_name_parts = soup.find('h1').text.strip()
    print(product_name_parts)
    price = soup.find('div', class_='cnt-price add-tovar cf').text.strip()
    print(price)
    image = 'https://www.computermarket.ru' + soup.find('div', class_='product product-view__card').find('img').get('src')
    print(image)
    # Find all characteristics and divides into parts
    characteristics = soup.find('div', class_='product-in').text.split()
    info = ''
    # Joins parts together without padding
    for characteristic in characteristics:
        info = info + ' ' + characteristic
    # Delete first space
    product_characteristic = (info.strip())
    article = soup.find('div', class_='articul-cont').text.strip()
    print(article)
    try:
        # Separates description from characteristics
        description = soup.find('div', class_='box visible').text.strip().split('Описание')
        product_description = (description[1])
        print(product_description)
    except:
        product_description = ''


# Collects all products from all pages
def find_all_products(subcategory_name, subcategory_href):
    pattern = subcategory_href + '/pagenum/{}'
    p = 0
    while True:
        # Substitutes the page number in the template
        subcategory_href = pattern.format(p)
        response = requests.get(subcategory_href)
        print(subcategory_href)
        p = p + 1
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        all_tables = soup.find_all('div', class_='inner-cont cf')
        for table in all_tables:
            product_href = 'https://www.computermarket.ru' + table.find('a', class_='title-ineer-cont').get('href')
            find_product_data(product_href)
            print(product_href)


def find_sub_categories(name, href):
    response = requests.get(href)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # Get all tables for a sub category
    all_tables = soup.find_all('div', class_='rnd cat')
    # For each table find name and url of a sub category
    for table in all_tables:
        subcategory_name = table.find('div', class_='cnt-title').text
        subcategory_href = 'https://www.computermarket.ru' + table.find('div', class_='cnt-title').find('a').get('href')
        find_all_products(subcategory_name, subcategory_href)


def find_main_category():
    url = 'https://www.computermarket.ru/'
    # Get response of the page
    response = requests.get(url)
    # Get the html code of the page
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    # Get main category table html code
    find_table = soup.find('div', class_='cnt inln_left-menu')
    # Get all rows from a main category table
    other_categories_html = find_table.find_all('div', class_='menuitem-container')
    # For each row find name and url of a category
    for categories_html in other_categories_html:
        categories_html_a = categories_html.find_all('a')
        for category_html in categories_html_a:
            main_category = category_html
        main_category_href = 'https://www.computermarket.ru' + main_category.get('href')
        main_category_name = main_category.text
        find_sub_categories(main_category_name, main_category_href)


if __name__ == '__main__':
    find_main_category()
