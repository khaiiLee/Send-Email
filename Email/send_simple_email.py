import ssl
import smtplib
from email.message import EmailMessage
from time import sleep


# Sender's email, password and reciever's email
email_sender = 'doanxemnao19@gmail.com'
# 16 digrit smtp password
email_password = 'lampnctalarfqgla'
email_reciever = 'khaichipmoon34@gmail.com'

# Body and subject of the email
subject = 'Check out my new email'
body = "Mail đây này, vip pro chưa bà con?"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())