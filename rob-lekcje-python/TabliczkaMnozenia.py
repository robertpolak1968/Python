# Fig. 5.17: fig05_17.py
# Sorting a list.

import sys

d =[[1]*11,[2]*11,[3]*11,[4]*11,[5]*11,[6]*11,[7]*11,[8]*11,[9]*11,[10]*11,[11]*11]


for i in range (0,11,1) : 
    for j in range (0,11,1) :
        d [i][j]= i*j
        # print 'i=',i,' j=',j,' i*j=',d [i][j],
        # print '\n'

# for i in range (0,11,1) :
#        print d[i]
print '\n'
print "Tabliczka mnozenie 10x10".rjust( 21 ), # 0
print '\n'
print '+','-'*42,'+'

for i in range (1,11,1) :
    if i<> 1 : print '|'
    for j in range (1,10,1) :
        if d [i][j]<=9 : print '| ', d [i][j],
        if d [i][j]>9 : print '|', d [i][j],
print '|'
print '+','-'*42,'+'

#print '\ntest'
#for iteam in d :
 #   print iteam


#print '\ntest'
#for iteam in range( len( d )-1 ) :
 #  print iteam