# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
load_dotenv()
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="Hello, there!",
    to="whatsapp:+33758732741",
)

print(message.body)