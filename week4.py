import math
import copy
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

# test code
print(car1.description())

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

class Default(dict):
     def __missing__(self, key):
         return key

print('{name} was born in {country}'.format_map(Default(name='Guido')))

print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})

print(math.hypot(32,444))

b = {'one': 1, 'two': 2, 'three': 3}
print(b)

sampleList = [11,3, 6, 9, 12, 15]
print(max(sampleList))
sampleList.sort()

for i in range(len(sampleList)):
    print( "Element Index[", i, "]", "Previous Value ", sampleList[i])

vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
x= vowels.sort()


def getUserAge():
  age = 3 #int(input ("What is your agr?"))
  return age
  
test = getUserAge()
print(test)

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#https://thomas-cokelaer.info/tutorials/python/data_structures.html
info = ['e', 12, 15.00, 'o', 'i']
print(info)
print(type(info)) 


a = [5,1, 2, 3, 4]
b = copy.deepcopy(a)
b.sort()
print(a)
print(b)
print(a[0])
print(len(a))


d = {'first':'string value', 'second':[1,2]}
print(d.keys())
print(d.values())

print(d['first'])
print(d['second'])
print(d.items())

print('first' in d)

print(d.get('first'))  
# this method can set an optional value, if the key is not found

dict1 = {}.fromkeys(['first', 'second'])
print(dict1.items())

#3.7.4
#https://docs.python.org/3/tutorial/datastructures.html

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
#2
print(fruits.count('tangerine'))
#0
print(fruits.index('banana'))
#3
print(fruits.index('banana', 4))  # Find next banana starting a position 4
#6
fruits.reverse()
print(fruits)
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
#['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
print(fruits)
#'pear'
