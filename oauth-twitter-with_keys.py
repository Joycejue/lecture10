from requests_oauthlib import OAuth1Session
import json
import secrets.py


client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food',"count":5}

r = oauth.get(protected_url, params=params)

info_json = r.text
big_dict = json.loads(info_json)
for dic in big_dict["statuses"]:
	print(dic["user"]["name"]+":")
	print(dic["text"])
	print("-------------------------------")

