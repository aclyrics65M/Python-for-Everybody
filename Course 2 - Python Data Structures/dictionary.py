# 9.4 Write a program to read through the mbox-short.txt and figure out 
# who has the sent the greatest number of mail messages. The program looks 
# for 'From ' lines and takes the second word of those lines as the person 
# who sent the mail. The program creates a Python dictionary that maps the 
# sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

name = input("Enter file:")

if len(name) < 1 : 
    name = "mbox-short.txt"
    
handle = open(name)


# Create a dictionary
python_di = dict()

# For loop
for line in handle:
    line = line.rstrip()
    
    # print(line)
    
    words = line.split()
    
    print(words)
    
    # Second for-loop
    for element in words:        
        python_di[element] = python_di.get(element,0) + 1
        
# Finding the most common word
maximumValue = -1
wordToFind = None

for key,value in python_di.items():
    print(key, value)
    
    if value > maximumValue:
        maximumValue = value
        wordToFind = key
        
print(wordToFind,maximumValue) 
           
        ##
        #if element in python_di:
        #    python_di[element] = python_di[element] + 1
        #else:
        #	python_di[element] = 1
        #	print("**New**")
            
        #print(element,python_di[element])
