import os
from twilio.rest import Client

def send_mms():
    account_sid = [sid]
    auth_token = [token]
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='Alert !! Human Figure Detected in your room',
            media_url='https://7934-2401-4900-1c6e-50fb-d8ed-1c1e-32ca-a8a8.ngrok.io/tmp/image1.png',
            from_=[twilio_whatsapp_number],
            to=[whatsapp_number]
        )

    print(message.sid)

