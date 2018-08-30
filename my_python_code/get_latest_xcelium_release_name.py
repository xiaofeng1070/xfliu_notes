#!/usr/local/bin/python3

####################################################################################
# This script will check latest INCISIVE1522/Xcelium (including Agile and Stable) verion
# in Cadence San Jose server, and send release name to my email.
# 
# Note: You need to connect to Cadence network before executing this script.
####################################################################################

import string
import ftplib
import smtplib
from ftplib import FTP
from email.mime.text import MIMEText

def get_latest_version(names):
	ftp = FTP('sj-xfliu')
	ftp.login('xfliu','Jumpoocz!3m')
	versions = []

	for tool_name in names:
		if (tool_name == '1522'):
			ftp.cwd('/grid/avs/install/avs1522')
			avs1522_list = ftp.nlst()
			avs1522_latest = avs1522_list[-3]
			print ('Latest INCISIVE1522 Version is {}'.format(avs1522_latest))
			versions.append(avs1522_latest)
		elif (tool_name == "xlm1704"):
			ftp.cwd('/grid/avs/install/xcelium/1704')
			xlm1704_list = ftp.nlst()
			xlm1704_latest = xlm1704_list[-3]
			print ('Latest Xcelium 1704 Stable Version is {}'.format(xlm1704_latest))
			versions.append(xlm1704_latest)
		elif (tool_name == 'xlma'):
			ftp.cwd('/grid/avs/install/xcelium/AGILE')
			xlma_list = ftp.nlst()
			xlma_latest = xlma_list[-3]
			print ('Latest Xcelium Agile Version is {}'.format(xlma_latest))
			versions.append(xlma_latest)
		elif (tool_name == 'mce'):
			ftp.cwd('/vols/rspace01/space/users/rock_cad/mce_releases')
			mce_release_list=ftp.nlst()
			mce_latest = mce_release_list[-1]
			print ('Latest MCE Release Version is {}'.format(mce_latest))
			versions.append(mce_latest)
		else:
			print ('ERROR, invalid tool name!')

	ftp.quit()
	return versions


def generate_mail_message(versions):
	file = open('./mail_message.txt', 'w')
	file.write ('=' * 30)
	file.write ('\n')
	file.write ('Latest Incisive1522  Version is:	{} \n'.format(versions[0]))
	file.write ('Latest Xcelium 1704  Version is:	{} \n'.format(versions[1]))
	file.write ('Latest Xcelium Agile Version is:	{} \n'.format(versions[2]))
	file.write ('Latest MCE Release   Version is:	{} \n'.format(versions[3]))
	file.write ('=' * 30)
	file.write ('\n')
	file.write ('\n')
	file.write ('This mail is send by script automaticly, do not replay')
	file.close()


def send_mail():
	#sender  	= "123371309@qq.com"
	sender  	= "johnny_cadence@qq.com"
	password   	= "wncbtpxcjnrubjdc"
	receiver   	= "xfliu@cadence.com"
	#receiver  	= "xfliu@cadence.com, yongjie@cadence.com, shaonan@cadence.com, kechang@cadence.com"
	
	path = "./mail_message.txt"
	with open(path, 'r') as text:
		msg = MIMEText(text.read()) 
	
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


names = ['1522', 'xlm1704', 'xlma', 'mce']
versions = get_latest_version(names)
generate_mail_message(versions)
send_mail()
