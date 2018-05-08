# -*- coding: utf-8 -*-

from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet["A1"] = "Number"
sheet["B1"] = "Name"

sheet["A2"] = 1
sheet["B2"] = "AAA"
sheet["A3"] = 2
sheet["B3"] = "BBB"

# test02라는 파일이 있으면 덮어쓰기 됨
# 없으면 새로운 엑셀파일 생성z
wb.save("test02.xlsx")
