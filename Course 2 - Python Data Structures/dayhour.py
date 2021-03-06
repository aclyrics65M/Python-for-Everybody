# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. You can pull 
# the hour out from the 'From ' line by finding the time and then splitting 
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
    
handle = open(name)

# Create a dictionary called counts
counts = dict()

# Index Position at 5
indexPositionTime = 5

# For loop
for line in handle:
    if line.startswith("From "):
        
        timeValue = line.split()[indexPositionTime].split(":")
        initialTime = timeValue[0]
        valueObtain = counts.get(timeValue[0], 0)
        counts[initialTime] = valueObtain + 1
        
# Create a list object
listObject = list()

for k, v in counts.items():
    listObject.append((k, v))

listObject.sort()

# Display the results
for hourTime, counts in listObject:
    print(hourTime, counts)
