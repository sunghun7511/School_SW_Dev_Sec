# -*- coding: utf-8 -*-

def func1(*a):
    print(a * 3)

print("start")
func1("agagd")

# 함수는 선언하고 호출하는 위치가 중요하다
# C언어처럼 앞에서 프로토프로토타입을 선언할 수 없을까?

# function  that return value
def sum(a, b):
    return a + b

a, b = input("Input number > ").split()
res = sum(int(a), int(b))
print(res)


# 그냥 함수 안에 다 박았따리
def skip():
    while True:
        n = input("Input > ")

        if "skip" in n:
            print("rejected")
        elif n is bytes("quit"):
            break
        else:
            print(n)
        
        print("-"*10)
# 호출
skip()


