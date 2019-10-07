# Fig. 14.6: fig14_06.py
# Reading and printing a file.

import sys

# open file
file = open( "grecon.txt", "r" )

records = file.readlines() # retrieve list of lines in file

print ''
print "Grade".ljust( 10 ), # 0
print "Length".ljust( 10 ),
print "Value".ljust( 10 ),
print "Min.mult.".ljust( 10 ),
print "Max.mult.".ljust( 10 ),
print "Box Alignm.".ljust( 10 ),
print "Box".ljust( 10 ),
print "Box".ljust( 10 ),
print "Type".ljust( 10 ),
print "Remarks".ljust( 10 ),
print "Nominal".ljust( 10 ),
print "Actual".ljust( 10 ),
print "Code".ljust( 10 ),
print "Size".ljust( 10 ),
print "x".ljust( 10 ),
print "Size1".ljust( 10 ),
print "Length".ljust( 10 ),
print "Angle".ljust( 10 ), # 17
print "Mat".ljust( 10 ), #18
print "Grade".ljust( 10 ), # 19
print "No.".rjust( 10 ), 
# print "Balance".rjust( 10 )
print ''
for record in records: # format each line
    fields = record.split()
    print fields[ 0 ].ljust( 10 ),
    print fields[ 1 ].ljust( 10 ),
    print fields[ 2 ].ljust( 10 ),
    print fields[ 3 ].ljust( 10 ),
    print fields[ 4 ].ljust( 10 ),
    print fields[ 5 ].ljust( 10 ),
    print fields[ 6 ].ljust( 10 ),
    print fields[ 7 ].ljust( 10 ),
    print fields[ 8 ].ljust( 10 ),
    print fields[ 9 ].ljust( 10 ),
    print fields[ 10 ].ljust( 10 ),
    print fields[ 11 ].ljust( 10 ),
    print fields[ 12 ].ljust( 10 ),
    print fields[ 13 ].just( 10 ),
    print fields[ 14 ].ljust( 10 ),
    print fields[ 15 ].ljust( 10 ),
    print fields[ 16 ].ljust( 10 ),
    print fields[ 17 ].ljust( 10 ),
    
    # print fields[ 2 ].rjust( 10 )
file.close()