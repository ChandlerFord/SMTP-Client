__author__ = 'Chandler'

import smtplib

sender = "test@gmail.com"
reciever = "chandlerford452@gmail.com"
message = "Test Message"

server = smtplib.SMTP('localhost')
server.debuglevel = 1
server.sendmail(sender, reciever, message)
print "Successfully sent email"
server.quit()