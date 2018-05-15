import pyautogui as py
import cv2
import numpy as np


def locateCenterImage(img_file):
    tmp_screen = py.screenshot('.tmp_screen.png')
    cv_screen = cv2.imread(".tmp_screen.png")
    cv_img = cv2.imread(img_file)
    i_width, i_height, _ = cv_img.shape

    result = cv2.matchTemplate(cv_screen, cv_img, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(result.argmax(), result.shape)

    return (x + int(i_width / 2), y + int(i_height / 2))
