# In this assignment you will read through and parse a file with text and numbers. You will extract
# all the numbers in the file and compute the sum of the numbers.

# handle = open(r"..\..\text_files\regex_sum_2481419.txt")

import re

name = input("Enter file:")

if len(name) < 1:
    name = "regex_sum_2481419.txt"
handle = open(name)

total = 0

for line in handle:
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for y in x:
            i = int(y)
            total = total + i

print(total)