import ssl
import smtplib
from email.message import EmailMessage
from time import sleep
import csv


email_sender = 'doanxemnao19@gmail.com'
email_password = 'lampnctalarfqgla'

with open('Account_email.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for lines in csv_reader:
        for email_reciver in lines:
            
            print(email_reciver)
            msg = EmailMessage()
            msg['Subject'] = 'HELLO MEOWHOUSE'
            msg['From'] = email_sender
            msg['To'] = email_reciver
            msg.set_content('Đây là email được gửi từ Lê Quang Khải, Intern Data Engineer của MeowHouse')

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465,context = context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(msg)