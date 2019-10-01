count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

print('next1')
for i in range(3, 6):
     print(i)
print('next2')

for i in range(4, 9, 2):
    print(i)


    
my_list = ['one', 'two', 'three', 'four', 'five']
for i in range(len(my_list)):
     print(my_list[i])

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

    
print('next2')
list_of_ints = list(range(3))

for iteam in list_of_ints:
    print(iteam)

print(list_of_ints)

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

    def toString(self):
        print("This is a message inside the class toString.")

myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.toString()

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

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
