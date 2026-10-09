# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that
# URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum
# of the numbers in the file and enter the sum below:
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your
# testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2481424.json (Sum ends with 49)

import json
import urllib.request, urllib.parse

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')
print('Count:', len(info['comments']))
js = info['comments']
total = 0

for item in js:
    total = total + int(item['count'])

print("Sum:", total)