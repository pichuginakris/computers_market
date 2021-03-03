import psycopg2
import csv


def write_csv_header():  # обновляет файл, добавляя в него заголовки
    with open('templates/products.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('Имя',  'Главная категория', 'Побочная категория', 'Артикул', 'Ссылка на картинку',
                         'Характеристика', 'Описание', 'Ссылка на товар', 'Цена'))


def write_csv(data):  # записывает данные в файл csv
    with open('templates/products.csv', 'a', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        row = (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
        writer.writerow(row)


def product_page_creating(sub_category_name):
    write_csv_header()
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "')")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            write_csv(row)
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) + '">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()


def product_page_sorted_descending_creating(sub_category_name):
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "') ORDER BY price DESC")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page_sorted_descending.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) + '">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()


def product_page_sorted_ascending_creating(sub_category_name):
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "') ORDER BY price ASC")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page_sorted_ascending.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) + '">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()


def product_page_filter_56000(sub_category_name):
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "') and (price>55000)ORDER BY price ASC")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page_end_filter_56000.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) + '">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()


def product_page_filter_15000(sub_category_name):
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "') and (price<15000)ORDER BY price ASC")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page_end_filter_15000.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) + '">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()


def product_page_filter_55000(sub_category_name):
    connect_str = "dbname='cm' user='project_user' password='+sWes43V%JMv' host='5.181.109.147'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    print(str(sub_category_name))
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + sub_category_name + "')and (price>15000) and (price<55001)ORDER BY price ASC")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page_end_filter_55000.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <div class="new_div"> <div class="article">' + str(row[4]) + '</div>\n')
            file.writelines('    <div class="price">Цена: ' + str(row[9]) + ' </div>\n')
            file.writelines('        <img  class="image" src="' + str(row[5]) +'">\n')

            file.writelines('  <div class="name">Наименование: ' + str(row[1]) + '</div>\n')
            file.writelines('   <div class="description"> Описание: ' + str(row[7]) + '</div>\n')

            file.writelines('  <div class="charact">Характеристики: ' + str(row[6]) + '</div>\n')
            file.writelines('   <div class="url">URL: ' + str(row[8]) + '  </div>\n')

            file.writelines('</div> <div class="border"></div>\n')

        for line in end:
            file.writelines(line)
    conn.commit()
