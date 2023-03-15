import smtplib
import ssl
import os
from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()

email_attacker = os.getenv('email_sender')
password = os.getenv("email_password")
email_receiver = 'ronaldomar6@gmail.com'
# email_attacker = 'watadomar10@gmail.com'
# password = 'hrzr qqlf naek tsge'
# email_receiver = 'ramibh11113@gmail.com '

subject = 'Greetings, a message from master Watad'
body = 'Hello,' + \
       'My name is Vortex, I am nothing but bot, created by master Watad. ' + \
       'I have a message for you, which is that you are a هلس. However, please refrain from replying to this email as I am merely an assistant and do not possess the ability to comprehend. ' + \
       'Any attempt to respond would be futile since my sole purpose is to aid my master in managing his emails. ' + \
       'Thanks.'


em = EmailMessage()
em['From'] = email_attacker
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_attacker, password)
#     for i in range (1,10):
    smtp.sendmail(email_attacker, email_receiver, em.as_string())
