import requests

from twilio.rest import Client

account_sid = 'AC8d4ccc16010de11ddf8380629f519e15'

auth_token = 'd74cb8a3deed047c321f65cd2eb5de84'

client = Client(account_sid, auth_token)

endpoint= "https://api.twitch.tv/helix/streams?"

headers = {"Client-ID": "txdttg2hwit9iveszfzyeze63k2ojx"}


params = {"user_login": "Ayrun"}

response = requests.get(endpoint, params=params, headers=headers)

print(response.json())

json_response = response.json()

streams = json_response.get('data',[])

is_active = lambda stream: stream.get ('type') == 'live'

streams_active = filter(is_active, streams)

at_least_one_stream_active = any(streams_active)

print(at_least_one_stream_active)



last_messages_sent = client.messages.list(limit=1)
if 'last_message_sent':
    last_message_id = last_messages_sent[0].sid
    last_message_data = client.messages(last_message_id).fetch()
    last_message_content = last_message_data.body
    online_notified = "LIVE" in last_message_content
    offline_notified = not online_notified

else:
    online_notified, offline_notified = False, False

if at_least_one_stream_active and not online_notified:
    client.messages.create(body= 'LIVE !!!', from_=+441480260057, to=+447707719451)
if not at_least_one_stream_active and not offline_notified:
    client.messages.create(body= 'OFFLINE !!!', from_=+441480260057, to=+447707719451)