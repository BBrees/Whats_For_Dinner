import requests
import json
import random

#connect to external api
api_key = "SECRET_TOKEN"
headers = {'Authorization': 'Bearer %s' % api_key}

url = "https://api.yelp.com/v3/businesses/search"

#type of food and location in louisville 

def Restaurants():

#Create a dictionary or list, populate it with several values, retrieve at least one to use in your program

    params = {}
    
    #input function call twice in order to build dictionary
    params['term'] = input("What kind of food would you like for dinner?\n")
    params['location'] = input("Where do you want to eat?\n")

#Utilizing dictionary to filter requests to yelp api
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    businesses = parsed["businesses"]
    
    dinner = random.choice(businesses)

    keys = ['name', 'location']
    values = list(map(dinner.get, keys))

    #return for Restaurant function

    return values

Whats_For_Dinner = Restaurants()

#print function utilized to display return of Restaurant function

print (Whats_For_Dinner)

