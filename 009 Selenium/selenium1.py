# -*- coding: utf-8 -*-

# 크롬 브라우저를 띄우기 위해 selenium 으로 웹드라이버를 가져옴
from selenium import webdriver

# 크롬 드라이버로 크롬 브라우저를 실행
driver = webdriver.Chrome("chromedriver")

try:
    # 네이버 뉴스 페이지로 이동
    driver.get("http://news.naver.com")

    # 네이버 뉴스임을 알 수 있도록 현재 타이틀 출력
    print(driver.title)

    # 최근 뉴스 목록을 가진 div id 태그를 가져옴
    title_id = driver.find_element_by_id("right.ranking_contents")

    # 위 div_id 안에 li 태그로 구분되어 있는 정보를 가져와 리스트로 저장
    news_list = title_id.find_element_by_tag_name("li")
    
except Exception as e:
    print(e)
