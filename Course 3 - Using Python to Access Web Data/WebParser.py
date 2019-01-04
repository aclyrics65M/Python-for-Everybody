# In this assignment you will write a Python program that expands on 
# http://www.py4e.com/code3/urllinks.py. The program will use urllib
# to read the HTML from the data files below, extract the href= vaues 
# from the anchor tags, scan for a tag that is in a particular position 
# relative to the first name in the list, follow that link and repeat 
# the process a number of times and report the last name you find.

import urllib
import re

from bs4 import *

present_number = 0

url_to_analyze = input('Enter URL - ')
count_number = int(input('Enter count: '))
position = int(input('Enter position: '))

# Function to parse the html
def parsingWebHTML(position, url_to_analyze):
   j = 0
   
   with urllib.request.urlopen(url_to_analyze) as url:
      URL_Link = url.read()
   
   # html_to_analyze = urllib.urlopen(url_to_analyze).read()
   
   soup = BeautifulSoup(URL_Link, "html.parser")
   
   tags_list = soup('a')
   
   for element in tags_list:
      j = j + 1
      if j == position:
         variable = element.get('href', None)
         return variable

# While loop
while present_number < count_number:
   print('Retrieving: ', url_to_analyze)
   
   # Update the url_to_analyze
   url_to_analyze = parsingWebHTML(position, url_to_analyze)
   
   # Update the present number
   present_number = present_number + 1   
   

print('The Last URL of this turn: ', url_to_analyze)   
