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

    words = line.split() 
    # Second for-loop
    if line.startswith("From "):        
        python_di[words[1]] = python_di.get(words[1],0) + 1
        
# Finding the most common word
maximumValue = 0
wordToFind = None

for key in python_di:
    #print(key, value)
    
    if python_di[key] > maximumValue:
        maximumValue = python_di[key]
        wordToFind = key
        
print(wordToFind,maximumValue) 
           
        ##
        #if element in python_di:
        #    python_di[element] = python_di[element] + 1
        #else:
        #	python_di[element] = 1
        #	print("**New**")
            
        #print(element,python_di[element])
