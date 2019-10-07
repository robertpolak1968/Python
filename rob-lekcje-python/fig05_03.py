# Fig. 5.3: fig05_03.py
# Creating, accessing and changing a list.
import math, cmath

aList = [] # create empty list

# add values to list
for number in range( 1, 11 ):
    
    if number in ( 1,2,3,4,5) : x=number*2
    if number in ( 6,7,8,9,10,11) : x=number*3-number*2
    aList += [ x ]

print "The value of aList is:", aList

# access list values by iteration
print "\nAccessing values by iteration:"

for item in aList:
    print item,

print

# access list values by index
print "\nAccessing values by index:"
print "Subscript Value"

for i in range( len( aList ) ):
    print "%9d %7d %s" % ( i, aList[ i ] ,"*" * aList[ i ])

# modify list
print "\nModifying a list value..."
print "Value of aList before modification:", aList
aList[ 0 ] = -100
aList[ -3 ] = 19
print "Value of aList after modification:", aList