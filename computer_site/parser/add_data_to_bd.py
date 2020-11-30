import psycopg2
import csv
import logging


def creating_bd(product, data):
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='product' user='postgres' password='qwerty%' host='localhost'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()

        conn.commit()

        try:
            print(data)
            cursor.execute("INSERT INTO tables_" + product + "(name, price, article, picture_url, " +
                                                      "characteristic, description, goods) values (" +
                           "'" + (data['name']).replace("'", "") + "','" + (data['price']).replace("'", "")
                           + "','" + (data['article']).replace("'", "") + "','" + (data['picture_url']).replace("'", "")
                           + "','" + (data['characteristic']).replace("'", "") + "','" +
                           (data['description']).replace("'", "") + "','" + (data['goods']).replace("'", "") + "')")
            conn.commit()
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in creating_bd(product, data): {!s}'.format(type(ex).__name__,
                                                                                             str(ex)))
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in creating_bd(product, data): {!s}'.format(type(ex).__name__, str(ex)))


