import smtplib
import string
import time
import cred

def send_mail():
	print ' Setting up Mail...'
	print '......................'

	msg= ' The door was opened at : ' 
	tm = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')
	SUBJECT = 'Alert '
	TO = cred.TO
	FROM = cred.FROM
	text = msg + tm
	BODY = string.join((
        	"From: %s" % cred.FROM,
        	"To: %s" % cred.TO,
        	"Subject: %s" % SUBJECT ,
        	"",
        	text
        	), "\r\n")
	server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	server.starttls()
	server.login( cred.FROM, cred.PASS )
	server.sendmail(cred.FROM, cred.TO, BODY)
	server.quit()
	print ' the message sent '

temperature = float(input('What is the temperature? '))
if temperature > 70:
	print('start sending mail.')
	send_mail()
else:
	print('it s okey.')
	


