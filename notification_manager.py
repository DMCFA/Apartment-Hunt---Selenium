import os
import smtplib
from twilio.rest import Client

TWILIO_SID = os.environ.get('T_SID') # twilio string identifier
TWILIO_AUTH_TOKEN = os.environ.get('T_TOKEN') # twilio authorization token
TWILIO_VIRTUAL_NUMBER = os.environ.get('T_NUMBER') # twilio virtual number
TWILIO_VERIFIED_NUMBER = os.environ.get('SENDER_NUMBER') # number used to open the account
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com" # mail provider
MY_EMAIL = os.environ.get('getEMAIL') # email used to send communications
MY_PASSWORD = os.environ.get('PASSWORD') # email's password
MESSAGE = 'Please go to the street easy website and bypass the captcha.'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body= MESSAGE,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email, # enter recipient address
                    msg=f"Subject:Apartment Hunt Verification\n\n{MESSAGE}\n".encode('utf-8')
                )