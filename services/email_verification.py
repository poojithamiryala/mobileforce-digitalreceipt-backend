import smtplib

from digitalReceipt.settings import email_address, email_app_password


class Gmail(object):
    def __init__(self, fromEmail, password):
        self.fromEmail = fromEmail
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.fromEmail, self.password)
        self.session = session

    def send_message(self, subject, body, toEmail):
        headers = [
            "From: " + self.fromEmail,
            "Subject: " + subject,
            "To: " + toEmail,
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.fromEmail,
            toEmail,
            headers + "\r\n\r\n" + body)


class GmailObject:
    print("Starting gmail service")
    gm = Gmail(email_address, email_app_password)
