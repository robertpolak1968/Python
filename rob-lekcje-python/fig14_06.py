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
print "Grade".ljust( 10 ),
print "Length".ljust( 10 ),
print "Value".ljust( 10 ),
print "Min.mult.".ljust( 10 ),
print "Max.mult.".ljust( 10 ),
print "Box Alignm.".ljust( 10 ),
print "Box".ljust( 10 ),
print "Box".ljust( 10 ),
print "Type".ljust( 10 ),
# print "Balance".rjust( 10 )
print ''
for record in records: # format each line
    fields = record.split()
    print fields[ 0 ].ljust( 10 ),
    print fields[ 1 ].rjust( 10 ),
    print fields[ 2 ].rjust( 10 ),
    print fields[ 3 ].rjust( 10 ),
    print fields[ 4 ].rjust( 10 ),
    print fields[ 5 ].rjust( 10 ),
    print fields[ 6 ].rjust( 10 ),
    print fields[ 7 ].rjust( 10 ),
    print fields[ 8 ].rjust( 10 ),
    print fields[ 9 ].rjust( 10 ),
    print fields[ 10 ].rjust( 10 ),
    print fields[ 11 ].rjust( 10 ),
    print fields[ 12 ].rjust( 10 ),
    print fields[ 13 ].rjust( 10 ),
    print fields[ 14 ].rjust( 10 ),
    print fields[ 15 ].rjust( 10 ),
    print fields[ 16 ].rjust( 10 ),
    print fields[ 17 ].rjust( 10 ),
    print fields[ 18 ].rjust( 10 ),
   
    print ''
    # print fields[ 2 ].rjust( 10 )
file.close()