#!/usr/local/bin/python3

import smtplib
from email.mime.text import MIMEText

_user = "123371309@qq.com"
_pwd  = "wncbtpxcjnrubjdc"
_to   = "xfliu@cadence.com"

msg = MIMEText("Test")
msg["Subject"] = "Don't Panic"
msg["From"] = _user
msg["To"] = _to

try:
	s = smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(_user, _pwd)
	s.sendmail(_user, _to, msg.as_string())
	s.quit()
	print("Success!")
except smtplib.SMTPException:
	print ("Failed")

