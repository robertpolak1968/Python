# Fig. 14.3: fig14_03.py
# Opening and writing to a file.

import sys

# open file
try:
    file = open( "clients.dat", "w" ) # open file in write mode
except IOError, message: # file open failed
    print >> sys.stderr, "File could not be opened:", message
    sys.exit( 1 )

print "Enter the account, name and balance."
print "Enter end-of-file to end input."
while 1:
    try:
        accountLine = raw_input( "? " ) # get account entry
    except EOFError:
        break # user entered EOF
    else:
        print >> file, accountLine # write entry to file

file.close()