# Scraping Numbers from HTML using BeautifulSoup In this assignment you will 
# write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, and
# parse the data, extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we 
# give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_167675.html (Sum ends with 18)
# You do not need to save these files to your folder since your program will 
# read the data directly from the URL. Note: Each student will have a distinct 
# data url for the assignment - so only use your own data url for analysis.

# Import statements
import urllib
import re

from bs4 import BeautifulSoup4

# Prompt user to ask for URL
# url_link = input('Enter - ')

url_link_one = 'http://py4e-data.dr-chuck.net/comments_42.html'
url_link_two = 'http://py4e-data.dr-chuck.net/comments_167675.html'

html_link = urllib.urlopen(url_link_one).read()
soup = BeautifulSoup(html_link,"html.parser")

# Total sum variable
total_sum = 0
 
tags_line = soup('span')

# For loop in Python
for element_tag in tags_line:
    
    # Obtain the string version  
    string_element = str(element_tag)
    element_parts = re.findall("[0-9]+", string_element)
    
    for integer in element_parts:
      integer = int(integer)
      total_sum = total_sum + integer
      
# Print out the total sum
print(total_sum)
