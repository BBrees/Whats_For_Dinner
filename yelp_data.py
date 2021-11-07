# in order to utilize requests must be install, not a part of Python standard library
import requests

# json, random, webbrowser all packages are part of standard library
import json
import random
import webbrowser

# API key from YELP saved in untracked file; personal API key can be obtained from 
# - https://www.yelp.com/developers/documentation/v3/get_started. API key can be placed in separate file
# and imported or copied in as a string to the commented out variable api_key = "SECRET_TOKEN"

from api import api_key

 
# api_key = "SECRET_TOKEN"

# Authorization of API key to allow url to be accessed
headers = {'Authorization': 'Bearer %s' % api_key}

url = "https://api.yelp.com/v3/businesses/search"

# params begins as empty dictionary
params = {}

# writing key and value into dictionary to be utilized to request data from external API (YELP)
params['term'] = input("What kind of food would you like for dinner? (i.e. American, Pub Food, Indian, Thai, etc)\n") 
params['location'] = input("Where do you want to eat? (city, neighborhood, or zipcode)\n")

# data request to YELP, returns as json with all businesses matching both values from params (NOTE: businesses are only
# included in YELP documents when user reviews are avaliable)
req = requests.get(url, params=params, headers=headers)
parsed = json.loads(req.text)
businesses = parsed["businesses"]

# utilizing random package a single business is returned from the json file
dinner_choice = random.choice(businesses)        

# Dinner class of functions to make dinner_choice more user readable when printed in console
class Dinner:
    def dinner_name():
        Restaurant_Name = dinner_choice.get('name')
        return Restaurant_Name

    def dinner_location():
        Restaurant_Location = dinner_choice.get('location', {}).get('display_address')
        return Restaurant_Location

    def dinner_url():
        Restaurant_url = dinner_choice.get('url')
        return Restaurant_url

Dinner_One = Dinner.dinner_name()
Dinner_Two = Dinner.dinner_location()

# in terminal user views name of restaurant and display address
print ("Name:", Dinner_One)
print ("Address:", Dinner_Two)

# if user would like to get more information press y and the yelp url for the restaurant with open in browser;
# press n and the program will end
print("Would you like more information?")
more_information = input("'y' for yes or 'n' for no.\n")

if more_information == 'y':
    webbrowser.open_new(Dinner.dinner_url())
else:
    pass