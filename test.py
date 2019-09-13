import math
import os.path #Python 2
from pathlib import Path #Python 3
from urllib.request import urlopen

print("Hello World")

print('math.sqrt(2): ')
print(math.sqrt(2))
print(math.cos(45))
print(float(7))
a= None
print(a is None) 
print(bool(0)) 
print(bool(1)) 

print(bool([])) 
print(bool([1,2,3,4,5]))  
s1 = """This is\nmultiline string"""
print(s1) 
path = "source_data\\text_files\\"
print(path) 

#Python 2
data_folder = os.path.join("source_data", "text_files")
file_to_open = os.path.join(data_folder, "raw_data.txt")
print(data_folder) 
print(file_to_open) 
#f = open(file_to_open)
#print(f.read())

#Python 3
data_folder3 = Path("source_data/text_files/")
file_to_open3 = data_folder3 / "raw_data.txt"
print(data_folder3) 
print(file_to_open3) 
#f = open(file_to_open)
#print(f.read())

mylist = list ('charakters')
print(mylist) 
print(mylist[2]) #base 0
print(mylist[:2]) #base 0
print(mylist[-2:]) #base 0

a = ['Mary', 'had', 'a', 'little', 'lamb']
b = list(range(2,10))
print(b) 
for i in range(len(a)):  
    print i, a[i]

print("Double the list numbers using for loop and range() function")
sampleList = [3, 6, 9, 12, 15]
for i in range(len(sampleList)):
    print( "Element Index[", i, "]", "Previous Value ", sampleList[i], "Now ", sampleList[i] * 2)

for n in b:
     print(n)

for n in a:
     print(n)

for n in (0, 1, 2, 3, 4):
     print(n)

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        #line_words = line.split()
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)
