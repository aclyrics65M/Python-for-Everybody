# Python program
# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the sum of the numbers in 
# the file and enter the sum below:

# Link_address variable
# link_address = urllib.urlopen(url_link_two)

# Data Object
# data_object = link_address.read()

# Import statements
import json
import urllib.request

url_link_one = 'http://py4e-data.dr-chuck.net/comments_42.json'
url_link_two = 'http://py4e-data.dr-chuck.net/comments_167678.json'

with urllib.request.urlopen(url_link_two) as url:
   link_address = url.read()

# Length of url link
url_length = len(url_link_two)

# Total summation
total_summation = 0

# While loop
while True:
   if url_length < 1:
      break
   
   data_length = len(link_address)
   information_to_analyze = json.loads(link_address)
   
   # Print statements
   print('Retrieving: ', link_address)
   print('Retrieved: ', data_length, ' characters')
   
   information_to_analyze = information_to_analyze['comments']
   
   # For loop
   for element in information_to_analyze:
      object_variable = element['count']
      integer_variable = int(object_variable)
      
      print('Count: ', object_variable)
      
      total_summation = total_summation + integer_variable
      print('Sum: ', total_summation)
   
   
   # Print out the final sum
   print('Final Sum: ', total_summation)
   break       
