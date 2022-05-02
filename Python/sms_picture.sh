#!/bin/bash

curl -XPOST https://api.twilio.com/2010-04-01/Accounts/AC5bea98d360df7e4d50af0fb6d8e34621/Messages.json \
--data-urlencode "To=$1" \
--data-urlencode "From=+19804093427" \
--data-urlencode "MediaUrl=http://$3:8001/Pictures/$2" \
--data-urlencode "Body=$4" \
-u 'AC5bea98d360df7e4d50af0fb6d8e34621:284691e649e31c7afeae5fb9694d481d'
