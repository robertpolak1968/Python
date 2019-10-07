# Fig. 14.6: fig14_06.py
# Reading and printing a file.

import sys

# open file
try:
    file = open( "grecon.txt", "r" )
# file = open( "c:\robert/rob-lekcje/grecon.txt", "r" )
# open('C:\Robert/rob-lekcje/grecon.txt', 'r')    
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit( 1 )

records = file.readlines() # retrieve list of lines in file

print ''
#print "Grade".ljust( 10 ), # 0
#print "Length".ljust( 10 ),
#print "Value".ljust( 10 ),
#print "Min.mult.".ljust( 10 ),
#print "Max.mult.".ljust( 10 ),
#print "Box Alignm.".ljust( 10 ),
#print "Box".ljust( 10 ),
#print "Box".ljust( 10 ),
#print "Type".ljust( 10 ),
#print "Remarks".ljust( 10 ), # 9
#print "Nominal".ljust( 10 ),
#print "Actual".ljust( 10 ),
#print "Code".ljust( 10 ),
#print "Size".ljust( 10 ),
#print "x".ljust( 10 ),
#print "Size1".ljust( 10 ),
#print "Length".ljust( 10 ),
#print "Angle".rjust( 10 ), # 17
# print "Balance".rjust( 10 )
print ''
print ''
j=0
mybase = []
mr =    []
             



#for record in records: # format each line
 #   for i in range(0,10,1):
 #       fields = record.split()
 #       print fields[ i ],
      

for record in records:
    j+=1
    for i in range(0,15):
        print 'j=',j, 'i=',i
        fields = record.split()     
        mr += [[fields[ 0 ]],[fields[ 1 ]],[fields[ 2 ]],[fields[ 3 ]],[fields[ 4 ]],[fields[ 5 ]],[fields[ 6 ]]] 
        #mr += [[fields[ i ] # ok 
        #mybase += [fields[ i ]]
        # mybaserow += [[fields[ i ]]]
        #mybaserow [0][0]= fields[ i ]
       

    
    
#a0 = records [0]
#a1 = records [1]
#a2 = records [2]
#a3 = records [3]

#a0_1= a0.split('\n')
#a1_1= a1.split('\n')
#a2_1= a2.split('\n')
#a3_1= a3.split('\n')


#a[0]=a0
#a[1]=a1
#a[2]=a2
#a[3]=a3

#aa=a0,a1,a2,a3
#aaa=a0+a1+a2+a3

file.close()