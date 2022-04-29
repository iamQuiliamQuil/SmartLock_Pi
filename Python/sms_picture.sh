#!/bin/bash
export TWILIO_ACCOUNT_SID=AC5bea98d360df7e4d50af0fb6d8e34621
export TWILIO_AUTH_TOKEN=284691e649e31c7afeae5fb9694d481d
export TWILIO_NUMBER=19804093427
export TO_NUMBER=$1

#curl -X POST -d "Body=$2" -d "From=$TWILIO_NUMBER" -d "To=$TO_NUMBER" "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages" -u "$TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN"

curl -XPOST https://api.twilio.com/2010-04-01/Accounts/AC5bea98d360df7e4d50af0fb6d8e34621/Messages.json \
--data-urlencode "To=$1" \
--data-urlencode "From=+19804093427" \
--data-urlencode "MediaUrl=http://169.226.103.172:8001/Pictures/$2" \ 
--data-urlencode "Body=Hello from my Twilio line!" \
-u 'AC5bea98d360df7e4d50af0fb6d8e34621:284691e649e31c7afeae5fb9694d481d'
