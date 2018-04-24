# 가상의 이메일 전송 함수

def send_mail(from_mail, to_mail, subject, contents):
    print("From : \t" + from_mail)
    print("To : \t" + to_mail)
    print("Subject : \t" + subject)
    print("*"*20)
    print(contents)
    print("*"*20)
    print("*"*20)

my_email = "sunghun7511@naver.com"

users = []
users.append({"name": "noda", "email": "sunghun7511@naver.com"})
users.append({"name": "hida", "email": "sunghun7511@naver.com"})

'''
            |       user0           |           user1       |
------------|-----------------------|-----------------------|
name        |        noda           | sunghun7511@naver.com |
email       |        hida           | sunghun7511@naver.com |
'''

contents = "Hello Mr.Kim"

for user in users:
    title = "Dear. " + user["name"]
    send_mail(my_email, user["email"], title, contents)