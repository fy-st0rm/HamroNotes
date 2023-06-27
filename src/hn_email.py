from inc import *

class Mail:
    def __init__(self):
        try:
            clientName = os.getenv("EMAIL_CLIENT_USERNAME")
            clientPassword = os.getenv("EMAIL_CLIENT_USERNAME")
            self.mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)
            self.mailServer.ehlo()
            self.mailServer.starttls()
            self.mailServer.ehlo()
            self.mailServer.login(clientName, clientPassword)
            logging.info(f"Sucessfully Loggin In As {clientName}")
        except Exception as e:
            logging.ERROR("Unable to log in")
            logging.ERROR(e)
    
    def send_main(self, recipient, subject, sender, html):
        msg = MIMEMultipart('mixed')

        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        htmlMessage = MIMEText(html, 'html')
        msg.attach(htmlMessage)
        self.mailServer.sendmail(sender, recipient, msg.as_string())
        logging.info(f"Sucessfully sent mail to {recipient}")

    def close_mail(self):
        logging.info(f"Closing mail server")
        self.mailServer.close()

        
        
    
        

