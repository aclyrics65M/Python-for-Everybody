# Python program 
# In this assignment you will write a Python program somewhat 
# similar to https://py4e.com/code3/geoxml.py. The program will 
# prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file and enter the sum.

# import statements
import xml.etree.ElementTree as ET
import urllib.request
import urllib

url_link_one = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url_link_two = 'http://py4e-data.dr-chuck.net/comments_167677.xml'

# First print statement
print('Retrieving ', url_link_two)

with urllib.request.urlopen(url_link_two) as url:
   xml_parse = url.read()
   
# xml_parse = urllib.urlopen(url_link_two).read()

link_length = str(len(xml_parse))

# Second print statement
print('Retrieved: ' + link_length + ' characters')

tree_parse = ET.fromstring(xml_parse)

variable_list = tree_parse.findall('.//count')
convertedvariable = str(len(variable_list))

# Third print statement
print('Count: ' + convertedvariable)

total_summation = 0

for element in variable_list:
   integer_variable = int(element.text)
   total_summation = total_summation + integer_variable

string_summation = str(total_summation)

# Fourth print statement
print('Sum: ' + string_summation)   
