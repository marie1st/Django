import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'uncle.django50@gmail.com'
	mypassword = "c0'Fdh50"
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'Admin Uncle Fruit'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()


###########Start sending#############
subject = 'ยืนยันการสมัครเว็บไซต์ซื้อผลไม้ Uncle Fruit - 2'
newmember_name = 'สมชาย'
content = '''
เนื่องจากความปลอดภัยของการเข้าใช้
กรุณายืนยันอีเมลล์ ผ่านลิ้งค์ด้านล่างนี้ 
'''
link = 'http://uncle-engineer.com/confirm/fawtkataktaktkawkejtjka'

msg = 'สวัสดีคุณ {} \n\n {}\n Verify Link: {}'.format(newmember_name,content,link)

sendthai('uncle.django50@gmail.com',subject,msg)