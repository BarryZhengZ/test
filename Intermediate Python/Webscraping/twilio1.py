import keys
from twilio.rest import Client


client = Client(keys.accountSID, keys.authToken)


TwilioNumber = "+12542775854"


mycellphone = '+13528076544'


textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber,
                                    body="Hey there!")


print(textmessage.status)




call = client.call.create(url="http://demo.twilio.com/docs/voice.xml",
                         to=mycellphone,from_=TwilioNumber)