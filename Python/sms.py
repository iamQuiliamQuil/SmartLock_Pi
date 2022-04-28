# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC5bea98d360df7e4d50af0fb6d8e34621']
auth_token = os.environ['284691e649e31c7afeae5fb9694d481d']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19084093427',
                     to='+15186505491'
                 )

print(message.sid)