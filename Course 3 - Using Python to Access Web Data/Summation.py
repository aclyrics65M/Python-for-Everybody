# Python program to find the summation
import re

# Open file to analyze
python_file = open('regex_sum_167673.txt')

# Create a list of numbers
python_list = list()

# Create a variable called total_summation
total_summation = 0

# Analyze each line individually
for line in python_file:
    number = re.findall('[0-9]+', line)
    length_line = len(number)
    if length_line > 0:
        for nums in number:
            total_summation = total_summation + int(nums)

# print statement
print(total_summation)
