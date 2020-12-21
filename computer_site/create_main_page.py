import psycopg2


def main_page_creating():
    connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    conn.commit()
    (cursor.execute("SELECT name_main_category FROM models_maincategory ORDER BY name_main_category"))
    rows = cursor.fetchall()
    print(rows)

    carcas = open('templates/main_page_beginning.html', 'r', encoding='utf8', newline='')
    end = open('templates/main_page_end.html', 'r', encoding='utf8', newline='')
    with open('templates/main_page.html', 'w', encoding='utf8', newline='') as file:
        for line in carcas:
            file.writelines(line)
        for row in rows:
            file.writelines(' <option>' + str(row[0]) + '</option>\n')
        for line in end:
            file.writelines(line)
    conn.commit()
