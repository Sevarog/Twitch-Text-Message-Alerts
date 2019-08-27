import requests

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
