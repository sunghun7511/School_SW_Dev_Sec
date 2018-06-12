# SW Development Secuirty Day 009 Selenium

## 웹 드라이버의 역할

* 웹 문서를 분석하고 이를 활용하여 화면 구성
* 웹 문서에 이벤트를 전달하고 결과값을 받음
* 웹 드라이버가 제공하는 방법으로 서로 주고 받아야 함

## 웹 드라이버를 직접 다루는 것

* 브라우저를 만드는 것
* 역시 라이브러리를 활용하자

## Selenium

* 일종의 서버 프로그램인데 라이브러리로 제공하는
* 다양한 브라우저의 웹 드라이버 컨트롤
* 라이브러리를 통해 웹 드라이버 컨트롤 가능

## 웹 자동화

* selenium 설치
  * `pip install selenium`
  * 안 되면 `python -m pip install --upgrade pip`
* 웹 페이지 분석
  * 일관된 화면을 위헤 이번엔 크롬으로 활용
  * 필요 프로그램 다운로드 [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* 코딩
  * 코드를 짜기 전에
  * `try ~ except ~ finally`
    * `try` 안의 코드를 수행하다가 에러가 발생하면 발생한 시점 이후의 코드는 수행하지 않고 `except` 로 가서 코드를 수행해라 `finally` 는 에러 여부와 상관없이 코드를 수행해라

