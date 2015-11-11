#!/usr/bin/python
#  -*- coding:utf-8 -*-

#导入smtplib和MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr

import smtplib

## ## ## ## ## ## ## ## ## ## ## ## ## ##
# 设置服务器，用户名，口令以及邮箱的后缀
mail_host="smtp.sina.com"
mail_user="boyce_developer"
mail_pass="ot2pvBgx2XdZkp"
mail_hostfix="sina.com"

## ## ## ## ## ## ## ## ## ## ## ## ## ##

def send_mail(to_list,sub,content,attachment,user=mail_user,pwd=mail_pass,host=mail_host):
	'''
	to_list:发给谁（接受的参数是列表）
	sub:主题
	content:内容
	attachment:附件的地址
	user:发件人的邮箱
	pwd:发件人的邮箱的密码
	
	return:
			True:发送成功
			False:发送失败
	ex:send_mail(["a@cym.so","sub","content","/Users/lanyy/Desktop/screenshot_at_2014-11-5_0_34_25.png","/Users/lanyy/Desktop/hannuo.py"])
				
	'''
	print("sending...")
	
	me=mail_user+"<"+mail_user+"@"+mail_hostfix+">"
	print me
	msg = MIMEMultipart()
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	
	msg.attach(MIMEText(content,'plain','utf-8'))
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user,mail_pass)
		s.sendmail(me, to_list, msg.as_string())
		s.close()
		return True
	except Exception,e:
		print str(e)
		print e
		return False

				
				

		if __name__== '__main__':
			if send_mail(["838304814@qq.com"], "测试邮件", "这是一份测试邮件", []):
				 print "发送成功"
			else:
				 print "发送失败"
		
			