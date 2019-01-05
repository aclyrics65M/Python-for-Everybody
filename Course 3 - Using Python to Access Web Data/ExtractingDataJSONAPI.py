# Python program
# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/geojson.py. The program will prompt for a location, 
# contact a web service and retrieve JSON for the web service and parse that data, 
# and retrieve the first place_id from the JSON. A place ID is a textual identifier 
# that uniquely identifies a place as within Google Maps.
#url_analysis = urllib.urlopen(url_link)
#data_analysis = url_analysis.read()

# Import statements
import urllib.request as par
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    standard_default_URL = 'http://py4e-data.dr-chuck.net/json?'
else :
    standard_default_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# While loop
while True:
   # Prompt the user to input a location
   link_location = input('Enter location: ')
   
   length_location = len(link_location)
   
   if length_location < 1:
      link_location = 'South Federal University'
      
   
   url_link = standard_default_URL + urllib.parse.urlencode({'sensor':'false', 'address': link_location})
   
   # First print statement
   print('Retrieving: ', url_link)
   
   with urllib.request.urlopen(url_link) as url:
      url_analysis = url.read()
      data_analysis = par.urlopen(url_link).read().decode('utf-8')
   
   length_data = len(data_analysis)
   
   # Second print statement   
   print('Retrieved: ', length_data, ' characters')
   
   string_variable = str(data_analysis)
   
   # try except
   try:
      js_analysis = json.loads(string_variable)
   except:
      js_analysis = None
   
   if not js_analysis or 'status' not in js_analysis or js_analysis['status'] != 'OK':
      print('==== Failure To Retrieve ====')
      print(data_analysis)
      continue

   print(json.dumps(js, indent=4))

   lat = js_analysis['results'][0]['geometry']['location']['lat']
   lng = js_analysis['results'][0]['geometry']['location']['lng']
   print('lat', lat, 'lng', lng)   
   
   location = js_analysis['results'][0]['formatted_address']
   place_ID = js_analysis['results'][0]['place_id']
   
   # Third print statement
   print('Location: ', location)
   print('Place ID: ', place_ID)
