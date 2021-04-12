import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
link = "http://127.0.0.1:8000/"


def test_UI_Find_Lowest_Cost():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        select_mc = Select(browser.find_element_by_tag_name("select"))
        select_mc.select_by_visible_text("KNS_Ноутбуки")
        browser.find_element_by_name("btn").click()

        select_sc = Select(browser.find_element_by_tag_name("select"))
        select_sc.select_by_visible_text("Ноутбуки Acer")
        browser.find_element_by_name("btn").click()

        select_sort = Select(browser.find_element_by_name("sort"))
        select_sort.select_by_visible_text("По возрастанию")
        list_elems = browser.find_elements(By.CLASS_NAME, "new_div")
        assert int(list_elems[0].find_element_by_class_name("price").text.split(" ")[1]) <= \
               int(list_elems[1].find_element_by_class_name("price").text.split(" ")[1])

        url = list_elems[0].find_element_by_class_name("url").text.split(" ")[1]
    except Exception as e:
        print(e)
        assert False, "test_UI_Find_Lowest_Cost failed"
    finally:
        browser.close()
        time.sleep(2)
        browser.quit()


def test_UI_Find_Highest_Cost():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        select_mc = Select(browser.find_element_by_tag_name("select"))
        select_mc.select_by_visible_text("KNS_Ноутбуки")
        browser.find_element_by_name("btn").click()

        select_sc = Select(browser.find_element_by_tag_name("select"))
        select_sc.select_by_visible_text("Ноутбуки Acer")
        browser.find_element_by_name("btn").click()

        select_sort = Select(browser.find_element_by_name("sort"))
        select_sort.select_by_visible_text("По убыванию")
        list_elems = browser.find_elements(By.CLASS_NAME, "new_div")
        assert int(list_elems[0].find_element_by_class_name("price").text.split(" ")[1]) >= \
               int(list_elems[1].find_element_by_class_name("price").text.split(" ")[1])
        url = list_elems[0].find_element_by_class_name("url").text.split(" ")[1]
    except Exception as e:
        print(e)
        assert False, "test_UI_Find_Highest_Cost failed"
    finally:
        browser.close()
        time.sleep(2)
        browser.quit()


def test_UI_Use_Middle_Filter():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        select_mc = Select(browser.find_element_by_tag_name("select"))
        select_mc.select_by_visible_text("KNS_Ноутбуки")
        browser.find_element_by_name("btn").click()

        select_sc = Select(browser.find_element_by_tag_name("select"))
        select_sc.select_by_visible_text("Ноутбуки Acer")
        browser.find_element_by_name("btn").click()

        select_sort = Select(browser.find_element_by_name("filter"))
        select_sort.select_by_visible_text("От 15000 до 55000 рублей")
        list_elems = browser.find_elements(By.CLASS_NAME, "new_div")
        assert (int(list_elems[len(list_elems) - 1].find_element_by_class_name("price").text.split(" ")[1]) <= 55000) &\
               (int(list_elems[0].find_element_by_class_name("price").text.split(" ")[1]) >= 15000), \
            "Middle Filter is broken"
    except Exception as e:
        print(e)
        assert False, "test_UI_Use_Middle_Filter failed"
    finally:
        browser.close()
        time.sleep(2)
        browser.quit()


def test_UI_Use_Big_Filter():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)

        select_mc = Select(browser.find_element_by_tag_name("select"))
        select_mc.select_by_visible_text("KNS_Ноутбуки")
        browser.find_element_by_name("btn").click()

        select_sc = Select(browser.find_element_by_tag_name("select"))
        select_sc.select_by_visible_text("Ноутбуки Acer")
        browser.find_element_by_name("btn").click()

        select_sort = Select(browser.find_element_by_name("filter"))
        select_sort.select_by_visible_text("Более 55000 рублей")
        list_elems = browser.find_elements(By.CLASS_NAME, "new_div")
        assert int(list_elems[0].find_element_by_class_name("price").text.split(" ")[1]) >= 55000,\
            "Big Filter is broken"
    except Exception as e:
        print(e)
        assert False, "test_UI_Use_Big_Filter failed"
    finally:
        browser.close()
        time.sleep(2)
        browser.quit()


def test_UI_csv_Download():
    try:
        prefs = {}
        prefs["profile.default_content_settings.popups"] = 0
        prefs["download.default_directory"] = os.getcwd()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(link)

        select_mc = Select(browser.find_element_by_tag_name("select"))
        select_mc.select_by_visible_text("KNS_Ноутбуки")
        browser.find_element_by_name("btn").click()

        select_sc = Select(browser.find_element_by_tag_name("select"))
        select_sc.select_by_visible_text("Ноутбуки Acer")
        browser.find_element_by_name("btn").click()

        downBtn = browser.find_element_by_link_text("Скачать")
        name = downBtn.get_attribute("download")
        downBtn.click()
        time.sleep(5)
        assert os.path.exists(os.getcwd() + '\\' + name)

        df_test = pd.read_csv("products_test.csv", delimiter=',', encoding="utf8")
        df_down = pd.read_csv(name, delimiter=',', encoding="utf8")
        assert df_down.equals(df_test), "Not equals .csv"
    except Exception as e:
        print(e)
        assert False, "test_UI_csv_Download failed"
    finally:
        if os.path.exists(os.getcwd() + '\\' + name):
            os.remove(os.getcwd() + '\\' + name)
        browser.close()
        time.sleep(2)
        browser.quit()


if __name__ == '__main__':
    test_UI_Find_Lowest_Cost()
    test_UI_Find_Highest_Cost()
    #test_UI_Use_Low_Filter()
    test_UI_Use_Middle_Filter()
    test_UI_Use_Big_Filter()
    test_UI_csv_Download()
