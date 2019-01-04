# Python test file
import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


sentence = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
z = re.findall("\S+?@\S+", sentence)
abc = re.findall("\$+?@", sentence)
print(z)
print(abc)
