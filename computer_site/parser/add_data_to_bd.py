import psycopg2
import logging


def delete_all_information():
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        conn.commit()
        try:
            cursor.execute("DELETE FROM models_maincategory;")
            conn.commit()
            cursor.execute("DELETE FROM models_subcategory;")
            conn.commit()
            cursor.execute("DELETE FROM models_product;")
            conn.commit()
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in delete_all_information(): {!s}'.format(type(ex).__name__,
                                                                                                  str(ex)))
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in delete_all_information(): {!s}'.format(type(ex).__name__,
                                                                                              str(ex)))


def creating_main_category(nameMainCategory):
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        conn.commit()
        print("INSERT INTO models_maincategory(id, name_main_category) values ('" +
              str(nameMainCategory).replace("'", "") + "')")
        try:
            cursor.execute("INSERT INTO models_maincategory(name_main_category) values ('" +
                           str(nameMainCategory).replace("'", "") + "');")
            print('k')

            conn.commit()
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in creating_main_category(nameMainCategory): {!s}'.format(type(ex).__name__,
                                                                                            str(ex)))
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in creating_main_category(nameMainCategory): {!s}'.format(type(ex).__name__, str(ex)))


def creating_sub_category(nameMainCategory, nameSubCategory):
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        conn.commit()

        try:
            cursor.execute("INSERT INTO models_subcategory(name_sub_category,name_main_category) values ('" +
                           str(nameMainCategory).replace("'", "") + "','" + str(nameSubCategory).replace("'", "") + "');")
            conn.commit()
            print('k')
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in creating_sub_category(nameMainCategory, nameSubCategory): {!s}'.format(type(ex).__name__,
                                                                                            str(ex)))
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in creating_sub_category(nameMainCategory, nameSubCategory): {!s}'.format(type(ex).__name__, str(ex)))


def creating_products(data):
    logging.basicConfig(filename='logging.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='cm' user='postgres' password='qwerty' host='localhost'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        conn.commit()

        try:
            cursor.execute("INSERT INTO models_product(product_name, name_main_category, name_sub_category, "
                           "article, picture_url, characteristic, "
                           "description, goods_url, price) values ('" +
                           str(data['product_name']).replace("'", "") + "','"  + str(data['nameMainCategory']).replace("'", "") + "','"
                           + str(data['nameSubCategory']).replace("'", "") + "','" + str(data['article']).replace("'", "") + "','"+
                           str(data['picture_url']).replace("'", "") + "','" + str(data['characteristic']).replace("'", "") + "','" + str(data['description']).replace("'", "") + "','" +
                           str(data['goods_url']).replace("'", "") + "','" + (data['price']) + "');")
            conn.commit()
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in creating_products(data): {!s}'.format(type(ex).__name__,
                                                                                            str(ex)))
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in creating_products(data): {!s}'.format(type(ex).__name__, str(ex)))

