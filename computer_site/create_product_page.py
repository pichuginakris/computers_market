import psycopg2


def product_page_creating(sub_category_name):
    connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    cursor.execute("SELECT * FROM models_product WHERE (name_sub_category ='" + str(sub_category_name) + "')")
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/product_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/product_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/product_page.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <option>' + str(row[0]) + '</option>\n')
        for line in end:
            file.writelines(line)
    conn.commit()
