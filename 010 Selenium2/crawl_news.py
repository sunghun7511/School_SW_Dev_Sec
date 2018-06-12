from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")

try:
    driver.get("https://www.naver.com")
    print(driver.title)

    elem = driver.find_element_by_id("query")
    elem.clear()
    # 간혹 포털마다 검색어가 이미 있는 경우가 있기 때문

    elem.send_keys("대덕소프트웨어마이스터고")
    elem.send_keys(Keys.RETURN)

    news = driver.find_element_by_xpath("//*[@id=\"main_pack\"]/div[4]/ul")
    news_list = news.find_elements_by_class_name("_sp_each_title")
    
    for news in news_list:
        print(news.text)

except Exception as e:
    print(e)
finally:
    driver.close()
