import requests
import json

api_key = "Secret Token"
headers = {'Authorization': 'Bearer %s' % api_key}

url = "https://api.yelp.com/v3/businesses/search"
