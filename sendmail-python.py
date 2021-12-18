from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendmail(reciever_email):
    my_email = 'your_email'
    my_password = 'your_password'

    msg = MIMEMultipart()
    msg.attach(MIMEText('<html> <body>' +
                        '<p><img src="your_link_image"></p>'+
                        '<p>your_message</p>'+
                        '</body> </html>', 'html', 'utf-8'))

    msg['Subject'] = 'your_subject'
    msg['From'] = 'your_from'
    msg['To'] = reciever_email

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()

    s.login(my_email, my_password)
    s.sendmail(my_email, reciever_email.split(','), msg.as_string())
    s.quit()

sendmailth('reciever_email')
