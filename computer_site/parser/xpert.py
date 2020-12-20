import requests
from bs4 import BeautifulSoup
from add_data_to_bd import creating_sub_category, creating_products, creating_main_category,  delete_all_information


def find_product_data(main_category_name, reference):
    response = requests.get(reference)
    print(reference)
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
    try:
        image = 'https://www.xpert.ru' + str((soup.find('table', class_='result').find_all('table'))[1].find('img').get('src'))
        print(image)
    except:
        image = ''
    try:
        price = (soup.find('table', class_='result').find_all('table'))[1].find('span').text
        print(price)
    except:
        price = ''
    article = (soup.find('table', class_='box').find_all('tr'))[1].text.strip()
    print(article)
    data = {
        'product_name': product_name.strip(),
        'nameMainCategory': 'XPERT',
        'nameSubCategory': main_category_name.strip(),
        'price': price.strip(),
        'article': article.strip(),
        'picture_url': image.strip(),
        'characteristic': '',
        'description': description.strip(),
        'goods_url': reference.strip()
    }
    creating_products(data)


def find_all_products(main_category_name, main_category_href):
    pattern = main_category_href + '&page={}'
    p = 1
    while p<10:
        try:
            main_category_href = pattern.format(p)
            response = requests.get(main_category_href)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            find_table = soup.find('table', class_='content_wrapper_table').find_all('table', class_='result')[1].find_all('td')
            for str in find_table:
                try:
                    reference = str.find('a').get('href')
                    reference = 'https://www.xpert.ru' + reference
                    find_product_data(main_category_name, reference)
                except:
                    reference = ''
            p = p + 1
        except:
            break


def find_main_category():
    # Стартовая страница
    url = 'https://www.xpert.ru/'
    # Получает ответ на запрос get к сайту
    response = requests.get(url)
    # Получает html код страницы
    html = response.text
    creating_main_category('XPERT')
    soup = BeautifulSoup(html, 'lxml')
    find_table = soup.find('table', class_='infoBoxContents_table').find_all('li')

    for categories_html in find_table:
        categories_html_a = categories_html.find_all('a', class_='category')
        for category_html in categories_html_a:
            main_category = category_html.get('href')
            main_category_href = 'https://www.xpert.ru/' + main_category
            main_category_name = category_html.text
            creating_sub_category(main_category_name, 'XPERT')
            with open('xpert_data.txt', 'a', encoding='utf8', newline='') as file:
                file.writelines(str(main_category_name) + '\n')
            find_all_products(main_category_name, main_category_href)


if __name__ == '__main__':
    find_main_category()