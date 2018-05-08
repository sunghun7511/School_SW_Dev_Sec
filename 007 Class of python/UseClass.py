# -*- coding: utf-8 -*-

# 간단한 클래스를 정의


class SimpleTest():
    a = 0
    postfix = "\t DSM"

    def print_with(self, string):
        print(string)
        print(self.a)
        print(str(self.a) + string + self.postfix)


# 클래스 변수를 생성
s1 = SimpleTest()
s2 = SimpleTest()

print(s1.a)
print(s2.a)

s1.a = 10
s2.a = 20

print(s1.a)
print(s2.a)

s1.print_with("KSH")
s2.print_with("UYBY&HGHG")
