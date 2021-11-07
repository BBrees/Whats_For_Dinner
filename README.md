# Whats_For_Dinner

<<<<<<< HEAD
ABOUT
=======
## About
>>>>>>> bc51f30acadd41203e089ab2f7743f6a3d3812bd

Do you ever have trouble deciding which restaurants to go to? Does it every cause marital strife or make you miss the window of opportunity? This is the app for you. Utilizing Python and the Yelp API you can find a place in seconds. 

## REQUIREMENTS

Install the following package:

    pip install requests

In order to connect externally to the Yelp API an individual API key is required follow the instructions below:

1. Sign into Yelp (https://www.yelp.com/)
    
2. Scroll to the bottom of the page and click on developers

3. Click the first link to Yelp Fusion 

4. Click create app & fill form 

5. Click manage app to obtain API key 

6. Open `yelp_data.py` in VS Code

7. Copy key in api_key variable or create new file api.py

    `api_key = "SECRET_TOKEN" #Replace SECRET_TOKEN, ensure API is str`

## RUN PROGRAM

Run `python yelp_data.py` in terminal 

    "What kind of food would you like for dinner?" (i.e. Indian, American, Fast Food)
    Indian #User Input
    
    "Where do you want to eat?", provide user input (i.e. zipcode, city, or neighborhood)
    Louisville #User Input
    
Program will provide single restaurant within the parameters provide by user including name and location, example below

    Name: Flavors Cuisine Of India
    Address: ['3201 Fern Valley Rd', 'Ste 111', 'Louisville, KY 40213']

If you want more information press y, will open html yelp page for restaurant in web browser. If user presses any other letter program will exit.

    Would you like more information?
    'y' for yes or 'n' for no.

## FEATURES FOR CODE LOUISVILLE PROJECT

1. Create a dictionary or list, populate with several values, retrieve at least one and use it in your program. 
2. Read data from an external file, such as text, json, csv, etc and use that data in your application.
3. Connect to external/3rd party API and read data into your app

## ADDITIONAL FEATURES TO ADD

1. Error handling for invalid inputs
2. Master loop so that if user does not like the current randomized restaurant they can go back through the program without restarting entirely.
3. Pull up map for directions. 

