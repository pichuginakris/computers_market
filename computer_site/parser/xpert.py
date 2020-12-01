import requests
from bs4 import BeautifulSoup


def find_product_data(reference):
    response = requests.get(reference)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    try:
        product_name = soup.find('td', class_='productName').text
        print(product_name)
    except:
        product_name = ''
    try:
        description = soup.find('div', id_='tabDesc')
        print(description)
    except:
        description = ''


def find_all_products(subcategory_name, subcategory_href):
    pattern = subcategory_href + '&page={}'
    p = 1
    while True:
        subcategory_href = pattern.format(p)
        response = requests.get(subcategory_href)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        find_table = soup.find('table', class_='content_wrapper_table').find_all('table', class_='result')[1].find_all('td')
        for str in find_table:
            try:
                reference = str.find('a').get('href')
                reference = 'https://www.xpert.ru' + reference
                find_product_data(reference)
            except:
                reference = ''


def find_main_category():
    # Стартовая страница
    url = 'https://www.xpert.ru/'
    # Получает ответ на запрос get к сайту
    response = requests.get(url)
    # Получает html код страницы
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    find_table = soup.find('table', class_='infoBoxContents_table').find_all('li')

    for categories_html in find_table:
        categories_html_a = categories_html.find_all('a', class_='category')
        for category_html in categories_html_a:
            main_category = category_html.get('href')
            main_category_href = 'https://www.xpert.ru/' + main_category
            main_category_name = category_html.text
            find_all_products(main_category_name, main_category_href)

if __name__ == '__main__':
    find_main_category()
