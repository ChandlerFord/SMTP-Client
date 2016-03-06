__author__ = 'Chandler'

import smtplib

sender = "test@gmail.com"
reciever = "chandlerford452@gmail.com"
message = "Test Message"


server = smtplib.SMTP()
server.connect('smtpauth.registerapi.com', 26)
server.login('Test@Duracrypt.com', 'Th!$Is4T3stP4$$werd')
server.set_debuglevel(1)
server.sendmail(sender, reciever, message)
print "Successfully sent email"
server.quit()