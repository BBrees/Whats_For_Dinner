import requests
import random
import choices


def random_dinner(location):
    location = input('Where do you want to eat tonight?')
    #flavor = input('What kind of food are you interested in tonight?')
    print("Try:")
    dinner = (random.choice(choices.ShelbyPark))
    print (dinner)

#def directions():

random_dinner(choices.ShelbyPark)


