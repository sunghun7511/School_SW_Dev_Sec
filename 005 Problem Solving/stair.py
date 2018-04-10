# -*- coding: utf-8 -*-

def stair(n):
    '''
    if n is 1:
        return 1
    elif n is 2:
        return 2
    아래와 같이 줄일 수 있다.
    '''
    if n < 3:
        return n
    else:
        return stair(n-1)+stair(n-2)


n = int(input("Input stair's number : "))
print(stair(n))
