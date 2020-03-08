#import twitter
import requests

class Twitter:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.bearer_token = None

    def getBearerToken(self):
        params = {
            'grant_type': 'client_credentials'
        }
        url = 'https://{0}:{1}@api.twitter.com/oauth2/token'.format(self.api_key, self.api_secret)
        r = requests.post(url, params=params)

        self.bearer_token = r.json()['access_token']

    def getTweets(self):
        headers = {
            'Authorization': 'Bearer ' + self.bearer_token
        }
        url = " https://api.twitter.com/1.1/search/tweets.json?q=bitcoin&count=100"
        r = requests.get(url, headers=headers)
        
        return r.json()['statuses']