import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

email_sender = 'doanxemnao19@gmail.com'

with open('Account_email.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #file csv chỉ mỗi dữ liệu email, thông thường dữ liệu khách hàng file csv gồm nhiều cột khác nhau như:
    # Tên, giới tính, năm sinh, vị trí, email, sđt, mạng xã hội,... thì xử lý như thế nào?
    for lines in csv_reader:
        for email_reciver in lines:
            
            print(email_reciver)

            msg = MIMEMultipart()

            msg['From'] = email_sender
            msg['To'] = email_reciver
            #Subject nên là biến nhập vào
            # Nếu gửi 100-1000 email có tiêu đề tương tự mặc định như vậy có bị SPAM không?
            msg['Subject'] = "SUBJECT OF THE EMAIL"

            body = "Đây là email được gửi từ Khải, intern Data Engineer của MEOWHOUSE TECHNOLOGY"

            msg.attach(MIMEText(body, 'plain'))

            filename = "Demo.txt"
            # password nên để là biến - nhập vào, không để mặc định
            attachment = open("D:\\Mobile app\\Demo.txt", "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            #password nên để là biến - nhập vào, không để mặc định
            server.login(email_sender, "lampnctalarfqgla")
            text = msg.as_string()
            server.sendmail(email_sender, email_reciver, text)
            server.quit()

# => Chưa viết ở dạng function - def ... (arg1, arg2, arg3, arg4)