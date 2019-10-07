# Fig. 13.6: fig13_06.py
# Token splitting and delimiter joining.
# splitting strings
#string1 = "A, B, C, D, E, F"
string1 = "ABCDEF"
print "String is:", string1
print "Split string by spaces:", string1.split()
print "Split string by commas:", string1.split( "," )
print "Split string by commas, max 2:", string1.split( ",", 2 )
print

# joining strings
#list1 = [ "A", "B", "C", "D", "E", "F" ]
list1 = "ABCDEF"
string2 = "___"

print "List is:", list1
print 'Joining with "%s": %s' \
    % ( string2, string2.join ( list1 ) )
print 'Joining with "-.-":', "-.-".join( list1 )