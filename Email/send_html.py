import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import pandas as pd
import csv

body = "TEXT YOU WANT TO SEND"

html = """
<!DOCTYPE html>
<html>
<body>

<a href="https://meowhouse.vn/" target = "_blank"><img src="https://i.ibb.co/gvv22fM/WELCOME-TO-MEOWHOUSE-TECHNOLOGY.png"></a>

</body>
</html>


"""

email_sender = 'doanxemnao19@gmail.com'
email_password = 'lampnctalarfqgla'

with open('Account_email.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for lines in csv_reader:
        for email_reciever in lines:
            
            print(email_reciever)

            date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = email_reciever
            msg['Subject'] = f'Report Email- {date_str}'


            msg.attach(MIMEText(html, "html"))

            email_string = msg.as_string()

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_reciever, msg.as_string())