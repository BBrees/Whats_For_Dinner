import requests

import json
import random
import webbrowser

class Dinner():
    def __init__(self, name, location):
        self.name = dinner_choice.get('name')
        self.location = dinner_choice.get('location', {}).get('display_address')
        #self. url = dinner_choice.get('url')

        def print(self):
            print("Name =", self.name)
            print("Address =", self.location)
            #print("var3 =", self.var3)
            
api_key = "wWo4R0IdYfTs35U8WcJvA1azDCVbGPVEx3POlFUUbTHNwkjQAMiA7kRUusiCOR4GJoP9WIYM1B8n_YTA6BFHcKepDcmPGvVUXPGznLZjZ9iW82Oubgss5tnFFmJ3YXYx"
headers = {'Authorization': 'Bearer %s' % api_key}

url = "https://api.yelp.com/v3/businesses/search"

params = {}
params['term'] = input("What kind of food would you like for dinner?\n")
params['location'] = input("Where do you want to eat?\n")

req = requests.get(url, params=params, headers=headers)
parsed = json.loads(req.text)
businesses = parsed["businesses"]

dinner_choice = random.choice(businesses) 

#def dinner_name():

    #Restaurant_Name = dinner_choice.get('name')
    
    #return Restaurant_Name

#def dinner_location():

    #Restaurant_Location = dinner_choice.get('location', {}).get('display_address')

    #return Restaurant_Location

#def dinner_url():

    #Restaurant_url = dinner_choice.get('url')

    #return Restaurant_url

Dinner_One = Dinner()

#Dinner_Two = dinner_location()

Dinner_One.print()
#print (Dinner_Two)

print("Would you like more information?\n")
more_information = input("'y' for yes or 'n' for no.")

#if more_information == 'y':
    #webbrowser.open_new(dinner_url())

#elif more_information == 'n':
    #map = input("Would you like directions?\n 'y' for yes or 'n' for no\n")
    #if map == 'y':



