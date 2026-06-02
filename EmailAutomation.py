'''
SMPT(Simple mail transfer protocol):
-----------------------------------
--> This is used to send emails from one server to another server.......
Note:
----
1.SMTP SSL port
---------------
465
2.SMTP TLS port
---------------
587

import smtplib

EmailMesage Class
-----------------
msg['Subject'] = 'SMTP ON MAIL'
msg['From'] = 'sender@email.com'
msg['To'] = 'Receiver@gmail.com'
'''

'''
import smtplib
from email.message import EmailMessage
sender = 'jayrajpathangay@gmail.com'
password = 'oylounomofahipxe'
msg = EmailMessage()

msg['Subject'] = 'Welcome Mail'
msg['From'] = 'jayrajpathangay@gmail.com'
msg['To'] = 'peyyalakaushik21@gmail.com'

msg.set_content('Hello My name is jay')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''

import smtplib
from email.message import EmailMessage
sender = 'jayrajpathangay@gmail.com'
password = 'tpjhwheibvbskpbl'
receiver = ['peyyalakaushik21@gmail.com','rajasainikhil.7@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
msg = EmailMessage()
for email in receiver:
    msg = EmailMessage()

    msg['Subject'] = 'Welcome Mail'
    msg['From'] = 'jayrajpathangay@gmail.com'
    msg['To'] = 'peyyalakaushik21@gmail.com'
    msg.set_content('Hello kaushik')

    server.send_message(msg)
server.quit()
