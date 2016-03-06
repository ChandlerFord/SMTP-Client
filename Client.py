__author__ = 'Chandler'

import smtplib

sender = "Test@Duracrypt.com"
reciever = "Test@Duracrypt.com"
message = "Test Message"


server = smtplib.SMTP()
server.connect('smtp.dotster.com', 587)
server.login('Test@Duracrypt.com', 'Th!$Is4T3stP4$$werd')
server.set_debuglevel(1)
server.sendmail(sender, reciever, message)
server.quit()
print "Successfully sent email"
