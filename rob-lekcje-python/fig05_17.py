# Fig. 5.17: fig05_17.py
# Sorting a list.

import sys

aList = [ 2, 6, 4, 8, 10, 12, 89, 68, 45, 37 ]

print "Data items in original order"

for item in aList :
    print item,

aList.sort()

print "\n\nData items after sorting"

for item in aList:
    print item,

print '\nRobert old way '

for i in range (len(aList)) :
    print aList[i],

d =[[1]*11,[2]*11,[3]*11,[4]*11,[5]*11,[6]*11,[7]*11,[8]*11,[9]*11,[10]*11,[11]*11]
print '\n'
for i in range (0,11,1) : 
    for j in range (0,11,1) :
        d [i][j]= i*j
        # print 'i=',i,' j=',j,' i*j=',d [i][j],
        # print '\n'

for i in range (0,11,1) :
        print d[i]
print 'fin1'

for iteam in range (11) :
    print d[iteam]


print 'fin2'

print "Tabliczka mnozenie 10x10".ljust( 50 ), # 0
