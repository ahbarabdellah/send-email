
'''

fast way

import smtplib
MYEmail = 'ahbarabdellah12@gmail.com'

msg= 'hi I am Ahbar Abdellah i send this msg for test ...\n' \
     'join us in this party'
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(MYEmail,MYPassword)
with open('email.txt') as f:
    for i in f:
        contactEmail= f.readline()
        server.sendmail(MYEmail,contactEmail,msg)
'''

import smtplib


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
message = input('your message :')
MY_ADDRESS =input('your email :')   #your email
PASSWORD = input('your email password')     #your email password 
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
names, emails = get_contacts('email.txt')

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
for name, email in zip(names, emails):
    msg = MIMEMultipart()  # create a message. object from the class MIMEMultipart()

    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = ("send email to "+name)

    
    msg.attach(MIMEText(message, 'plain'))


    s.send_message(msg)
    del msg

'''Up UP yupi '''