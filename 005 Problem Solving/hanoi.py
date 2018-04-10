# -*- coding: utf-8 -*-

'''
def hanoi(n):
    return 1 if n is 1 else hanoi(n-1) + 1 + hanoi(n-1)
    # 유한성 조건

n = int(input("Input hanoi column's number : "))
# 입력(0개 이상)

print(hanoi(n)) # 출력(1개 이상)

'''


n = int(input("Input hanoi column's number : "))
print(2 ** n - 1)