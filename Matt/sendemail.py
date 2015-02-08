import smtplib
from email.mime.text import MIMEText

fromaddr = 'rutgerslostandfound@gmail.com'
toaddrs  = 'mattlee446@gmail.com'
subject = 'poop'

# Credentials (if needed)
username = 'rutgerlostandfound'
password = 'chalupacity'

def createmessage(froma, to, subject):
	msg = MIMEText('this is a test')
	msg['From'] = froma
	msg['To'] = to
	msg['Subject'] = subject
	return msg




# The actual mail send
msg = createmessage(fromaddr, toaddrs, subject)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()