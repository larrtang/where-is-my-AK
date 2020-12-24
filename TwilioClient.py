from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
class TwilioClient:
    
    
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_SID')
        self.auth_token = os.getenv('TWILIO_TOKEN')
       
        self.client = Client(self.account_sid, self.auth_token)

    def sendMessage(self, msg_body):
        message = self.client.messages \
                        .create(
                            body=msg_body,
                            from_='+12565619311',
                            to='+16306974762'
                        )

        print(message.sid)
