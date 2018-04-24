# -*- coding: utf-8 -*-

def gcd(a, b):
    while b is not 0:
        temp = a % b
        a = b
        b = temp
    return abs(a)

def minimize_div(a, b):
    if b == 0 or a == 0:
        return a, b

    g = gcd(a, b)
    return (a // g, b // g)

def minimize_expr(a, b, *, has_unknown=False, neg_val="-"):
    vals = list(minimize_div(a, b))
    neg = (vals[0] < 0) ^ (vals[1] < 0) is True

    vals[0] = abs(vals[0])
    vals[1] = abs(vals[1])

    final = ""
    final += (neg_val if neg else "")
    final += str(vals[0])
    if abs(vals[1]) is 1:
        if has_unknown:
            final += "x"
    else:
        final += "/" + str(vals[1])
        if has_unknown:
            final = "(" + final + ")x"

    return final

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def run(a_str, b_str, *, print_output=True):
    if not is_digit(a_str) or not is_digit(b_str):
        exit("정수만 입력해주세요.")

    a, b = int(a_str), int(b_str)

    if a is 0:
        exit("미지수의 차수는 0이 아니여야 합니다.")

    origin_expr = a_str + "x"

    if b < 0:
        origin_expr += " - " + b_str[1:]
    elif b > 0:
        origin_expr += " + " + b_str


    first_expr = minimize_expr(1, a, has_unknown=True)
    second_expr = minimize_expr(-b, a, neg_val="- ")

    final_expr = first_expr + (" " if second_expr[0] == "-" else " + ") + second_expr
    
    if print_output:
        print(origin_expr + " 의 역함수 f^-1(x) 는 " + final_expr + "입니다.")

    return final_expr


def test_case():
    tcs = [
        {"input": ("3", "5"), "output": "(1/3)x - 5/3"},
        {"input": ("2", "2"), "output": "(1/2)x - 1"},
        {"input": ("5", "6"), "output": "(1/5)x - 6/5"},
        {"input": ("2", "-3"), "output": "(1/2)x + 3/2"},
        {"input": ("-1", "-2"), "output": "-1x - 2"}
    ]
    
    for i, tc in enumerate(tcs):
        inp = tc["input"]
        out = tc["output"]
        
        value = run(inp[0], inp[1], print_output=False)
        if out == value:
            print(str(i+1) + "'s test case pass!")
        else:
            print(str(i+1) + "'s test case error!")
            print("\nInput : " + str(tc["input"]))
            print("Output : " + str(value))
            print("\nAnswer : " + out)
            print("")

    return


if __name__ == "__main__":
    test_case()
    
    inp = input("ax + b 의 함수에서 a값과 b값을 입력하세요 : ").split()
    a_str, b_str = inp[0], inp[1]

    run(a_str, b_str)

'''
f(x) = ax + b

f^-1(x) = (1/a)x - b/a
'''