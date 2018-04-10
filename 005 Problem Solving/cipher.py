# -*- coding: utf-8 -*-
'''
문제
---
중복되지 않은 10개의 코드를 가진 암호코드표가 주어지고,
각의 암호 코드에는 0부터 9까지의 숫자가 매칭된다.
암호문이 주어졌을 때 이 암호코드를 기반으로 암호문을
복호화하는 알고리즘을 작성하시오.

암호문은 공백을 허용한다.
'''

code = "iohcgpdabk"

inp = raw_input("Input your text : ")
print("".join([n if code.find(n) is -1 else str(code.find(n)) for n in inp]))