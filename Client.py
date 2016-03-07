__author__ = 'Chandler'

import smtplib
import email.utils
from email.mime.text import MIMEText

#Login Info:
Username = 'Test@Duracrypt.com'
Password = 'Th!$Is4T3stP4$$werd'

#Email Info
message = MIMEText("This is a test message")
message['To'] = email.utils.formataddr(('Reciever', 'Test@Duracrypt.com'))
message['From'] = email.utils.formataddr(('Sender', 'Test@Duracrypt.com'))
message['Subject'] = 'TEST'

#Send
server = smtplib.SMTP()
server.connect('smtp.dotster.com', 587)
server.login(Username , Password)
server.set_debuglevel(1)
server.sendmail('Test@Duracrypt.com', 'Test@Duracrypt.com', message.as_string())
server.quit()
print "Successfully sent email"
