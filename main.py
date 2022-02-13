# -*- coding: utf-8 -*-
"""
Most Active Cookie
Name: Ai Nguyen
Email: nguyennhanai1993@gmail.com

"""

# Create list for each purpose 
arr = []; # List of cookies from CSV file
arr2 = []; # List of date from CSV file
arr3 = []; # List of index match date from user input 
arr4 = []; # List of cookies match date from user
arr5 = []; # List of unique cookie from arr
arr6 = []; # List of occurrences of each cookie in arr 

# Read command from user
command = input();

# Split it into 3 different: cookie, -d, timestamp
words = command.split(' ');

# Read CSV file
f = open(words[0], 'r');
count1 = 0;
for x in f:
    if count1 != 0:
        temp = x.split(',');
        arr.append(temp[0]); # Assign cookie from Data to arr
        arr2.append(temp[1].split('T')[0]); # Assign date from Data to arr2
    count1 = count1 + 1; 

# Index match date from user input 
for i in range(0, len(arr2)):
    if arr2[i] == words[2]:
        arr3.append(i);
        
# Assign cookies match date from user
for i in range(0, len(arr3)):
    arr4.append(arr[arr3[i]]);

# Find unique cookie in arr4
for x in arr4:
    if not x in arr5:
        arr5.append(x);

# Find occurrences of each cookie in arr4 
for x in arr5:
    count = 0;
    for y in arr4:
        if x == y:
            count = count + 1; 
    arr6.append(count);        

# Print the cookie that appear the most in the Date from user
for i in range(0, len(arr5)):
    if arr6[i] == max(arr6):
        print(arr4[i]);
