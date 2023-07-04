from inc import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(email, subject, html):
    username = os.getenv("EMAIL_CLIENT_USERNAME")
    password = os.getenv("EMAIL_CLIENT_PASSWORD")
    print(username)
    print(password)
    msg = MIMEMultipart('mixed')

    sender = os.getenv("EMAIL_SENDER")
    recipient = email

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = email

    html_message = MIMEText(html, 'html')
    msg.attach(html_message)

    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used.
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(sender, recipient, msg.as_string())
    mailServer.close()

        
        
    
        

