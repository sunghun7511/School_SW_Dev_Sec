# -*- coding: utf-8 -*-

# pyautogui test

import pyautogui

# size
# 화면의 크기를 반환하는 pyautogui 라이브러리 함수

w, h = pyautogui.size()

print(w, h)

# pyautogui.moveTo(w / 2, h / 2)

# moveRel
#  원하는 위치(상대좌표)로 마우스를 이동
#  이동하지 않으려면 None 값으로 인자를 설정한다.

# pyautogui.moveRel(-150, -150)

'''
pyautogui.moveTo(w/3, h/3)

for i in range(10):
    pyautogui.moveRel(w/3, 0)
    pyautogui.moveRel(0, h/3)
    pyautogui.moveRel(-w/3, 0)
    pyautogui.moveRel(0, -h/3)
'''

# click
# 옵션을 통해 횟수와 버튼 지정 가능
# x, y => 마우스 위치 이동
# clicks => 마우스 클릭 횟수
# interval => 클릭 간격 조정(값 : second)
# button => 마우스 버튼 위치 선택(left, right)

pyautogui.click(x=w/2, y=h/2, button="left")

# typewrite
# 키를 입력하는 함수
# 지금은 영어만 입력할 수 있음.

pyautogui.typewrite('give me icecream')

# press
# 특수키를 입력할 때 사용하는 함수

pyautogui.press("enter")
