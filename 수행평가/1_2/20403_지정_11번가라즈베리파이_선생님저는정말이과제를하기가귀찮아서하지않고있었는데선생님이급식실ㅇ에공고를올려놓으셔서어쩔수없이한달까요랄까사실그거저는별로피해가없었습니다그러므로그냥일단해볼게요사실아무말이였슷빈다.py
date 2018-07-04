# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome("chromedriver")

try:
    driver.get("http://www.11st.co.kr/html/main.html")

    elem = driver.find_element_by_id("AKCKwd")
    elem.clear()

    elem.send_keys("라즈베리파이")
    elem.send_keys(Keys.RETURN)

    items = driver.find_element_by_xpath("//*[@id=\"hotClickPrdArea\"]/div/ul")
    items_list = items.find_elements_by_tag_name("li")
    
    titles = list()
    for item in items_list:
        post_title = item.find_element_by_xpath("./div[2]/div[2]/p/a")
        titles.append(post_title.text)
    
    wb = Workbook()
    sheet = wb.active
    
    for i, title in enumerate(titles):
        sheet["A" + str(i+1)] = title
        print(title)
    
    wb.save("20403_지정.xlsx")
except Exception as e:
    print(e)
finally:
    driver.close()
