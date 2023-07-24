import smtplib
import sys

CARRIERS = {
        "att": "@mms.att.net",
        "tmobile": "@tmomail.net",
        "verizon": "@vtext.com",
        "sprint": "@page.nextel.com"
    }

''' Class to send text messages from a gmail account '''
class Texter:
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.email, self.password)

    def send_message(self, phone_number, carrier, message):
        recipient = str(phone_number) + CARRIERS[carrier]
     
        self.server.sendmail('texter', recipient, message)
        print("[MESSAGE SENT]")
