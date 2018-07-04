# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome("chromedriver")

try:
    driver.get("http://dsmhs.djsch.kr")

    elem = driver.find_element_by_xpath("//*[@id=\"container\"]/div[2]/div[2]/div[1]/div[1]/a")
    elem.click()

    items = driver.find_element_by_xpath("//*[@id=\"subContent\"]/div[2]/form/div/div[1]/table/tbody")
    items_list = items.find_elements_by_class_name("link")
    
    titles = list()
    for item in items_list:
        post_title = item.find_element_by_tag_name("a")
        titles.append(post_title.get_attribute("title"))
    
    wb = Workbook()
    sheet = wb.active
    
    for i, title in enumerate(titles):
        sheet["A" + str(i+1)] = title
        print(title)
    
    wb.save("20403_자유.xlsx")
except Exception as e:
    print(e)
finally:
    driver.close()
