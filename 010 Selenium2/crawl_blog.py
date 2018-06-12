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

    blogs = driver.find_element_by_class_name("_blogBase")
    blogs_list = blogs.find_elements_by_tag_name("li")
    
    for post in blogs_list:
        # print(post.text)
        # print("-"*20)

        post_title = post.find_element_by_class_name("sh_blog_title")
        post_title_txt = post_title.get_attribute("title")
        print(post_title_txt)
        # ... 으로 생략되어 있는 것 -> 속성 : title
        print(post_title.get_attribute("href"))
        # url

except Exception as e:
    print(e)
finally:
    driver.close()
