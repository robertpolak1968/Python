import math
import os.path #Python 2
from pathlib import Path #Python 3
from urllib.request import urlopen
import csv


with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        #line_words = line.split()
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)


with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)

fileObj = open("t.txt", "r")
 
for line in fileObj.readlines():
    print(line)
fileObj.close()

# Open the file with read only permit
f = open('t.txt', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
#lines2 = f.readlines()
lines = list(f)

# close the file after reading the lines.
f.close()

for line in lines:
   print(line)


   # Open the file with read only permit
f = open('t.txt')
# use readline() to read the first line 
line = f.readline()

# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    print(line)
    # use realine() to read next line
    #line = f.readline()
    line = f.readline().split() #split bt=y space
f.close()



f = open('t.csv')

data = []
for line in f:
    data_line = line.rstrip().split('\t')
    data.append(data_line)

print (data)



from pprint import pprint

with open('t.csv', 'r', newline='') as csv_file:
    reader = csv.reader(line.replace('  ', ',') for line in csv_file)
    my_list = list(reader)
    pprint(my_list)
