# -*- coding: utf-8 -*-
import pyautogui as py
import cv2, time
import numpy as np
from subprocess import run
from opencvloc import locateCenterImage

# locateCenterOnScreen
# 그림과 일치하는 위치의 좌표 반환 함수
# 그림파일을 png로 설정해야 함.

# lx, ly = py.locateCenterOnScreen("image.png")
# py.moveTo(lx, ly)

def locateCenterImage(img_file):
    tmp_screen = py.screenshot('./imgs/.tmp_screen.png')
    cv_screen = cv2.imread("./imgs/.tmp_screen.png")
    cv_img = cv2.imread(img_file)
    i_width, i_height, _ = cv_img.shape

    result = cv2.matchTemplate(cv_screen, cv_img, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(result.argmax(), result.shape)

    return (x + int(i_width / 2), y + int(i_height / 4))

run(["calc"])

time.sleep(1)

x, y = locateCenterImage("./imgs/btn_5.png")
py.click(x, y)

x, y = locateCenterImage("./imgs/btn_mul.png")
py.click(x, y)

x, y = locateCenterImage("./imgs/btn_3.png")
py.click(x, y)

x, y = locateCenterImage("./imgs/btn_eql.png")
py.click(x, y)


