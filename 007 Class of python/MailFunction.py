# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

pwf = open("./password")
password = pwf.read()
pwf.close()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

SMTP_USER = "ksh01034244823@gmail.com"
SMTP_PASSWORD = password

class Email():
    def send_mail(self, name, addr, *, subject="테스트 메일입니다.", content="테스트 메일의 내용입니다!"):
        msg = MIMEMultipart()

        msg["From"] = SMTP_USER
        msg["to"] = addr
        msg["Subject"] = subject

        msg.attach(MIMEText(_text=content, _charset="utf-8"))

        # SMTP로 접속할 서버 정보를 가진 클래스 변수를 생성한다.
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

        # 계정 정보로 로그인
        smtp.login(SMTP_USER, SMTP_PASSWORD)

        # 메일 발송
        smtp.sendmail(SMTP_USER, addr, msg.as_string())

        smtp.close()