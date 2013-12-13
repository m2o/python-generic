import smtplib
from email.mime.text import MIMEText

from settings import SMTP_SERVER

def send(subject,frm,to,body):

	msg = MIMEText(body)

	msg['Subject'] = subject
	msg['From'] = frm
	msg['To'] = ','.join(to)

	s = smtplib.SMTP(SMTP_SERVER)
	s.sendmail(frm,to, msg.as_string())
	s.quit()

if __name__ == '__main__':
	send('autobus','bla@bla.com','t.pivcevic@gmail.com','body')
