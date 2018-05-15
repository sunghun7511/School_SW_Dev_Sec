from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465

SMTP_USER = 'skyjjw79@gmail.com'
SMTP_PASSWORD = ''

def send_mail(name, addr):
	msg = MIMEMultipart()

 	# 메일 전송을 위한 양식 작성 
	msg['From'] = SMTP_USER
	msg['To'] = addr
	msg['Subject'] = name+ '님에게 메일이 도착하였습니다 ^ㅁ^'

	contents = name + '''님에게 메일이 도착하였습니다.
	안녕하세요^^ 자동화로 니 컴퓨터 해킹할거야 아이조아'''

	# msg['text'] = contents

	text = MIMEText(_text = contents, _charset = 'utf-8')
	msg.attach(text)

	# SMTP로 접속할 서버 정보를 가진 클래스 변수를 생성한다.
	smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
	
	# 계정 정보로 로그인 
	smtp.login(SMTP_USER, SMTP_PASSWORD)

	# 메일 발송
	smtp.sendmail(SMTP_USER, addr, msg.as_string())

	print("\n 메일이 전송되었습니다 \n")

	smtp.close()

send_mail('정재웅','skyjjw79@hanmail.net')