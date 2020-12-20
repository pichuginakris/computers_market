import psycopg2


def sub_page_creating(main_category_name):
    connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    (cursor.execute("SELECT name_sub_category FROM models_subcategory WHERE name_main_category ='" +
                    str(main_category_name) + "'  ORDER BY name_sub_category"))
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/sub_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/sub_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/sub_page.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <option>' + str(row[0]) + '</option>\n')
        for line in end:
            file.writelines(line)
    conn.commit()
