from twilio.rest import Client
import os
account_sid = [sid]
auth_token = [token]
client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
    from_=[twilio_number],
    body='Alert! Human Figure Detected',
    to=[my_number]
    )

    print(message.sid)