#!/usr/local/bin/python3

####################################################################################
# This script will check mce_release in Cadence San Jose server, and send latest
# MCE release name to my email.
# 
# Note: You need to connect to Cadence network before executing this script.
####################################################################################

import ftplib
import smtplib
from ftplib import FTP
from email.mime.text import MIMEText

ftp = FTP('sj-xfliu')
#ftp.login('xfliu','Youneed3m')
ftp.login('xfliu','Jumpoocz!3m')
ftp.cwd('/vols/rspace01/space/users/rock_cad/mce_releases')
#ftp.retrlines('LIST')
#ftp.retrlines('NLST')
list_string=ftp.nlst()
mce_name = list_string[-1]
print (mce_name)
ftp.quit()


#sender  	= "123371309@qq.com"
sender  	= "johnny_cadence@qq.com"
password    	= "wncbtpxcjnrubjdc"
#receiver    	= "xfliu@cadence.com"
receiver    	= "xfliu@cadence.com, yongjie@cadence.com"
content		= 'Latest MCE Release is: '+ mce_name + '\nThis mail is send by script automaticly, do not reply.'
#print (content)

#msg = MIMEText("""Latest MCE Release is: mce_name, This mail is send by script automaticly, do not reply.""")
msg = MIMEText(content)
msg["Subject"] = "Latest MCE Release Name"
msg["From"] = sender
msg["To"] = receiver

try:
	s = smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(sender, password)
	s.sendmail(sender, receiver, msg.as_string())
	s.quit()
	print("Success!")
except smtplib.SMTPException:
	print ("Failed")


