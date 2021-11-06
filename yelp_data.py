import requests

import json
import random

api_key = "SECRET_TOKEN"
headers = {'Authorization': 'Bearer %s' % api_key}

url = "https://api.yelp.com/v3/businesses/search"

def Restaurants():

    params = {}
    
    params['term'] = input("What kind of food would you like for dinner?\n")
    params['location'] = input("Where do you want to eat?\n")

    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]

    
    dinner = random.choice(businesses)

    dinner_name = dinner.get('name')
    dinner_address = dinner.get('location',{}).get('display_address'))

    Eat_At = dinner_name, dinner_address

    return Eat_At

Whats_For_Dinner = Restaurants()

print (Whats_For_Dinner)

