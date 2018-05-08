# -*- coding: utf-8 -*-

class SimpleTest():
    my_data = 0

    def __init__(self):
        self.my_data += 100
        print("Call init!")


simple = SimpleTest()
print(simple.my_data)
