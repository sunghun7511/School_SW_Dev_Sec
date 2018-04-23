# count
a = "programming"
res = a.count("m")

print(res)

'''
2

count 함수가 메소드로 지정된 변수의 문자열에서
count 함수 인자(문자)의 개수를 반환한다.
'''


# find
a = "programming"
res = a.find("m")

print(res)

# index
a = "programming"
res = a.index("m")

print(res)

'''
6
6

find 함수가 메소드로 지정된 변수의 문자열에서
find 함수의 인자(문자)의 인덱스를 반환한다.

만약 찾는 문자가 없다면? => -1 을 출력
반환되는 -1이 정수이기 때문에 연산이 가능하다

ex) if res == -1 또는 res + 1

index 함수는 만약 찾는 문자가 없다면 에러 출력
'''


# join
a = "_m-_-m_"
res = a.join("ABC")

print(res)

'''
A_m-_-m_B_m-_-m_C

join 함수가 메소드로 지정돼 변수의 문자를
join 함수의 인자(문자) 사이에 삽입한다.
숫자도 될까? => 당연히 안된다.
가능하게 하는 방법은? => 숫자를 문자려 지정해준다.

한 줄씩 띄우게 하고 싶을 땐?
"\n".join(a)
'''


a = [1, "asdf", 123, "asdfasdf"]
print(a[0], a[2:4])
print(str(a[2:4])[1:-1])

'''
1 [123, 'asdfasdf']
123, 'asdfasdf'
'''


# upper

a = "programming"
res = a.upper()

print(res)

# lower

a = "PROGRAMMING"
res = a.lower()

print(res)

'''
PROGRAMMING
programming

lower는 소문자로, upper는 대문자로 반환한다.
특수문자에 대해서는 작동하지 않는다.
'''


# replace
a = "programming"
res = a.replace("gramming", "gaming")

print(res)

'''
progaming

문자열을 치환한 결과를 반환한다.

공백으로부터 치환이 가능할까? replace("", "1") -> 가능하다.
programming -> 1p1r1o1g1r1a1m1m1i1n1g1

공백으로 치환도 가능하다.

띄어쓰기로부터 치환이 가능하다.

없는 문자열은 치환이 불가능하다 => 원본 그대로 출력
'''


# split

a = "pro gramm ing"
res = a.split()

print(res)

'''
['pro', 'gramm', 'ing']

문자열을 나눈 결과를 리스트로 반환한다.
'''


# lstrip

a = "     programming     "
res = a.lstrip()

print("\"" + res + "\"")

'''
"programming     "

왼쪽 공백을 제거
'''


# rstrip

a = "     programming     "
res = a.rstrip()

print("\"" + res + "\"")

'''
"     programming"

오른쪽 공백을 제거
'''


# strip

a = "     programming     "
res = a.strip()

print("\"" + res + "\"")

'''
"programming"

앞뒤의 공백을 제거
'''


# type
a = "programming"
res = a.split()

print(type(res))

'''
<class 'list'>

해당 변수의 타입을 반환한다.
'''


# str

a = 123
res = str(a)

print(res)

'''
123

숫자를 문자열로 바꿈
문자열인지 판단하는 방법 => *10
문자를 문자열로 바꾸는 것
'''


# int

a = "123"
res = int(a) # 실수는 float

print(res)

'''
123

문자로 표현된 숫자를 정수형으로 바꿈
숫자가 아닌 값은 불가능
'''


# ord

a = "A"
res = ord(a)

print(res)

'''
65

문자를 아스키로 바꿈
'''


# chr

a = 65
res = chr(a)

print(res)

'''
A

정수에 해당하는 아스키 문자를 반환한다.

res = chr(a/2)
와 같이 썼을 때, a/2는 float이므로 안됨.
'''


# append

res = [1, 2, 3]
res.append(4)

print(res)

'''
[1, 2, 3, 4]

append의 인자를 리스트의 맨 뒤에 추가한다.

이 때 반환값은 None
'''


# sort
res1 = ["e", "a", "h"]
res2 = [1, 6, 2]

res1.sort()
res2.sort(reverse = True)

print(res1)
print(res2)

print(sorted(res1, reverse=True))
print(sorted(res2))


a = {"2": "a", "1": "c", "3": "b"}
print(sorted(a))


'''
['a', 'e', 'h']
[6, 2, 1]
['h', 'e', 'a']
[1, 2, 6]
['1', '2', '3']

리스트 안의 값들을 정렬한다.
res1.sort() 는 반환값 없음
sorted는 반환만 한다.

딕셔너리는 키값들이 정렬되서 나온다.
'''


# reverse

res = ["e", "a", "h"]
res.reverse()

print(res)

'''
['h', 'a', 'e']

리스트 내부의 값을 거꾸로 넣는다.
'''


# insert

res = [100, 123, 523]
res.insert(1, 2)

print(res)

'''
[100, 2, 123, 523]

특정 인덱스의 값이 되도록 요소를 추가한다.
'''


# remove

res = [10, 20, 30, 40, 10]
res.remove(10)

print(res)

'''
[20, 30, 40, 10]

함수의 인자값을 찾아서 삭제한다.

값이 여러개라면 맨 첫 번째 요소만 삭제한다.
'''


# pop

res = [10, 20, 30, 40]
a = res.pop()

print(a)
print(res)

'''
40
[10, 20, 30]

맨 마지막의 요소를 제거한 이후 그 값을 반환한다.
'''


# count

a = [10, 10, 101, 102, 10, "abasf"]
res = a.count(10)

print(res)

'''
3

함수의 인자값을 찾아서 개수를 샌다.
'''


# keys

a = {"a": 123, "b": 456}
res = a.keys()
res2 = list(a.items())

print(res)
print(res2)

'''
dict_keys(['a', 'b'])
[('a', 123), ('b', 456)]

딕셔너리의 key 들을 반환한다.
'''


# get

a = {"q": 123, "w": 456}
res = a.get("q")
res2 = a.get("a", 100)

print(res)
print(a["q"])
print(res2)

'''
123
123
100

딕셔너리의 값을 반환한다.
단, 존재하지 않는 키일 때, get 함수는 None를, [, ] 를 사용했을 때는 오류가 난다.
'''


# in

a = {"q": 123, "w": 456}

print("q" in a)
print("a" in a)

'''
True
False


값이 딕셔너리의 키(또는 리스트의 값들)에 있을 경우 True, 없으면 False
'''