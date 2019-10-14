import math
import os.path #Python 2
from pathlib import Path #Python 3
from urllib.request import urlopen
import csv

   # Open the file with read only permit
f = open('StudentDetails.txt')
# use readline() to read the first line 
line = f.readline()

lines = list()
AvgList = list()
studentDictionary = {};

# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    #print(line)
    
    # use realine() to read next line
    #line = f.readline()
    line = f.readline().split() #split bt=y space
    lines.append(line)
f.close()


lines.pop()
for i in range(len(lines)):
    print( "Element Index[", i, "]", "Previous Value ", lines[i] )

for n in lines:
     avgGrade = round(int(n[1])+int(n[2])+int(n[3])/3,2)
     AvgList.append([n[0],avgGrade])
     print("Name: ",n[0] ,"Avarage: " , avgGrade  )

print("AvgList")
for item in AvgList:
  studentDictionary[item[0].upper()]= item[1]

  print(item)

keepGoing = 'y'
while keepGoing == 'y':
  # Get a salesperson's sales and commission rate.
  studentName = (input ( 'Enter the sutent name : ' ))

  print ('Student Name: ' ,studentName);
  print ('Student Avarage: ' , studentDictionary[studentName.upper()]);
  
  keepGoing = input( 'Do you want to calculate another student y/n? ')

