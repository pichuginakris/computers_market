import psycopg2
import logging


def create_main_category_table(name):
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')

    connect_str = "dbname='products' user='postgres' password='qwerty' host='localhost'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    print('d')
    cursor.execute(
        "CREATE TABLE computers_kns(id integer, subname char(20000), main_category integer) INHERITS (computers); ")