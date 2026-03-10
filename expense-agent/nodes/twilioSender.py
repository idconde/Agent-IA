from twilio.rest import Client
import os

client = Client(os.getenv("TWILIO_ACCOUNT_SID"),
                os.getenv("TWILIO_AUTH_TOKEN"))

FROM = os.getenv("TWILIO_PHONE_NUMBER")        # whatsapp:+1...
# TO will be provided by webhook (the sender’s number)

def send_whatsapp(to_number: str, body: str):
    client.messages.create(
        from_=FROM,
        to=to_number,
        body=body
    )