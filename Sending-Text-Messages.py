from twilio.rest import Client

account_sid = 'AC8d4ccc16010de11ddf4380629f519e15'

auth_token = 'd74cb8a3deed047c321f05cd2eb5de84'

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body= "ARYUN IS LIVE!" , from_=+441480260057, to =+447707719481)
