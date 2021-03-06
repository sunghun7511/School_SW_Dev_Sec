# SW Development Secuirty Day 002 Study Python

## What I learned

### 1. What is the Python

* 스크립트 언어(인터프리터) : 컴파일 없이 실행 가능한 언어
* 컴파일 : 어떤 언어의 코드를 다른 언어로 변환
* 컴파일러 : 프로그램 단위 번역, 느린 번역 속도, 실행 속도 빠름, 큰 메모리
* 인터프리터 : 명령 줄 단위 번역, 빠른 번역 속도, 실행 속도 느림, 작은 메모리

### 2. Operators & Data types

* `print()` : 표준 출력
* `type()` : 대상의 타입
* `string` + `string` = `stringstring`
* 자료형은 대입을 하는 순간 결정됨.
* `int` / `int` = `float`
* `def function():` : 함수 정의
* 연산자
  * `+` : 더하기
  * `-` : 빼기
  * `*` : 곱하기
  * `/` : 나누기
  * `**` : 거듭제곱
  * `//` : 나머지를 버리는 나누기
  * `%` : 나머지 연산

### 3. Strings & Arrays

* 문자열은 `''`, `" "`, `''' '''`, `""" """`
* 탭 = `ctrl + tab`
* `print("\n" * x)` : 문자열 곱셈이 가능하다.
* 인덱싱 : 특정 문자 배열처럼 0부터 시작
  * `a[0]` : 0부터 시작
  * `a[-1]` : 뒤에서 첫번째
* 슬라이싱 : 특정 문자열 자르기
  * `a[0:3]` : 0부터 3까지
  * `a[0:]` : 0부터 끝까지
  * `a[:]` : 전부다
  * `a[:3]` : 3 까지

### 4. Data Structures

* 리스트 : 여러 개 자료형을 동시에 담을 수 있다.
* 딕셔너리 : 대응 관계를 나타낼 수 있는 자료형
  * 인덱싱은 가능
  * 슬라이싱은 불가능
  * Key값을 통해 value를 얻을 수 있음.
  * `dic = {"가" : "1", "나" : "2", "다" : "3"}`

### 5. Built-in Functions

* `count` : 해당 문자의 개수
* `index` : 해당 문자의 인덱스 ( 없으면 에러 )
* `find` : 해당 문자의 인덱스 ( 없으면 -1 )
* `join` : 두 문자열을 섞음 ( 실행하는 메소드의 주인이 인자의 사이로 들어감 )
* `upper` : 대문자로 변환
* `lower` : 소문자로 변환
* `replace` : 문자열 상에서 첫번째 인자에 해당하는 문자를 전부 두번째 인자로 변환
* `split` : 문자를 인자로 나누어서 배열로 만듬
* `lstrip` : 가장 왼쪽의 공백 지우기
* `rstrip` : 가장 오른쪽의 공백 지우기
* `strip` : 양쪽 공백 지우기
* `type` : 타입 출력
* `int` : 문자를 정수로 반환
* `str` : 문자열로 반환
* `ord` : 문자를 아스키코드로 반환
* `chr` : 아스키를 문자로 반환