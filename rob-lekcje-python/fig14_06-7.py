# Fig. 14.6: fig14_06.py
# Reading and printing a file.

import sys

# open file
try:
   #path='C:\Robert/rob-lekcje/grecon.txt'
   pathin= 'C:\Grecon/reduce/'
   filename='1-44x219.txt'
   fullpath=pathin+filename
   file = open(fullpath, 'r') # open file txt from cuting list grecon folder
# file = open( "grecon.txt", "r" ) # open file txt from cuting list grecon folder GOOD
# open('C:\Robert/rob-lekcje/grecon.txt', 'r')    
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit( 1 )

records = file.readlines() # retrieve list of lines in file , 

print ''
#print "Grade".ljust( 10 ), # 0
#print "Length".ljust( 10 ),# 1
#print "Value".ljust( 10 ),# 2
#print "Min.mult.".ljust( 10 ),# 3
#print "Max.mult.".ljust( 10 ),# 4
#print "BoxAlignm.".ljust( 10 ),# 5
#print "Box".ljust( 10 ),# 6
#print "Box1".ljust( 10 ),# 7
#print "Type".ljust( 10 ),# 8
#print "Remarks".ljust( 10 ), # 9
#print "Nominal".ljust( 10 ),# 10
#print "Actual".ljust( 10 ), #11
#print "Code".ljust( 10 ), #12
#print "Size".ljust( 10 ), #13
#print "x".ljust( 10 ), #14
#print "Size1".ljust( 10 ), #15
#print "Length".ljust( 10 ), #16
#print "Angle".rjust( 10 ), # 17
print ''

mm = [[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #0-10
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #20
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #30
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #40
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #50
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #60
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #70
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #80
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #90
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #100
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #110
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #120
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #130
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #140
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #150
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #160
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #170
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #180
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #190
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17] #200      
      
ma = [[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #0-10
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #20
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #30
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #40
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #50
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #60
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #70
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #80
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #90
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #100
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #110
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #120
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #130
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #140
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #150
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #160
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #170
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #180
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #190
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17] #200

mb = [[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #0-10
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #20
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #30
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #40
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #50
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #60
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #70
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #80
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #90
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #100
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #110
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #120
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #130
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #140
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #150
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #160
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #170
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #180
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17, #190
      [0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17,[0]*17] #200  
j=0
mr =    []
red = []
redukcja = []
wymiary = []
sumkiwymiar = [0]*15000 #max lenght of timber 15000 mm
ilosckolumn=17 # number of colums "Grade", "Length" ....
iloscwierszy=0 # number of rows 0,1,2,3,...

for record in records:
    j+=1
    for i in range(0,ilosckolumn):
        fields = record.split()     
        mr += [fields[ i ]] #split record for seperatly string for each column ... to database mr  

iloscwierszy=j #number or record in records (in file) 

for w in range (0,iloscwierszy) :
    for i in range (0,ilosckolumn):
        mm [w][i]= mr[i+ilosckolumn*w] # create data base for each row, w-rows, i-column

print  'Number of rows of file (Ilosc wierszyw pliku): ',iloscwierszy , '\n' # max. 200 
print 'Rows to reduce quantity, (Wiersze do redukcji) :' 

for i in range (0, iloscwierszy) :
    if (mm [i][8] == '_' or mm [i][8] == 'mFD') and (mm[i][11]=='S' or mm[i][11]=='FD' or mm[i][11]=='D') and (int(mm[i][9])>0): # 8-Remarks , 11-Code, 9  - Quantity
    # with reduce dwang gableladers if (mm [i][8] == '_' or 'LDD' in mm [i][8]) and (mm[i][11]=='S' or mm[i][11]=='FD' or mm[i][11]=='D'or mm[i][11]=='LDD') and (int(mm[i][9])>0): # 8-Remarks , 11-Code, 9  - Quantity
        print i, ':' ,mm[i]
        red.append (i) # data base with index of mm to reduce or delete 
print ''
for k in red :
    # print k,mm[k]
    redukcja.append (mm[k]) #create database dekukcja with records to reduce form mm


for i in range (len(redukcja)):
    wymiary.append(redukcja[i][1]) # create list of length of timber to do reduce quantity


for wymiar in wymiary: #delete repeated lenght from list wymiary 
    wymiary.count(wymiar)
    ilosc=wymiary.count(wymiar)
    # print wymiar, ilosc 
    while (wymiary.count(wymiar))>=2:
        usunac=wymiar
        if wymiar in wymiary : wymiary.remove(usunac)


for k in range (len (wymiary)) : # count each dimension from redukcja 
    for i in range (len (redukcja)) :
        # print k,i, wymiary[k] ,redukcja[i][1].count (wymiary[k])
        # old if (redukcja[i][1].count (wymiary[k])<> 0 : sumkiwymiar[int(wymiary[k])] += int(redukcja[i][9])
        if redukcja[i][1] == wymiary[k] : sumkiwymiar[int(wymiary[k])] += int(redukcja[i][9])
i=0
profil = mm[1][0]
for wymiar in wymiary :
    i+=1
    volue=str((int(wymiary[i-1])*int(wymiary[i-1]))/10000)
    ma [i-1]= [redukcja [i-1][0],wymiary[i-1],volue,redukcja [i-1][3],redukcja [i-1][4],redukcja [i-1][5],redukcja [i-1][6],redukcja [i-1][7],redukcja [i-1][8],
        sumkiwymiar[int(wymiary[i-1])],redukcja [i-1][10],redukcja [i-1][11],redukcja [i-1][12],redukcja [i-1][13],redukcja [i-1][14],wymiary[i-1],redukcja [i-1][16]]
    # ma data base with reduced quantity

# 'Rows with reduced quantity, (Wiersze po redukcji) : ma'

print 'Reduced quantity of studs, dwangs : Done'

#NEW version !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
#NEW version !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
i=0
for reduk in redukcja :
    while reduk in mm :
        if reduk in mm : mm.remove (reduk)
        #print 'delete', reduk  # delete from  mm all record from redukcja 

print 'Deleted Reduced rows: Done' + '\n'

i=0
# profil = mm[1][0]
profil= ('44x219-C16','44x219-C24','44x222-C16','44x222-C24','44x219','44x219t','44x222','44x222t',
         '38x89','38x89t','38x140','38x140t','38x195','38x195t','38x184','38x184t')
for m in range (len (mm)-1) :
    i+=1
    if mm[i][0] != '!Grade' :  # or if mm[i][0] in profil : 
        mb [i] = mm[i] # copy mm to mb with out labels first record m[1]
      
# delete all empty rows in ma !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
empty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in ma :
    for k in ma :
        if empty in ma : ma.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# delete all empty rows in mb !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if empty in mb :
    for k in mb :
        if empty in mb : mb.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in mb :
    for k in mb :
        if empty in mb : mb.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in mb :
    for k in mb :
        if empty in mb :mb.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
if empty in mb :
    for k in mb :
        if empty in mb : mb.remove ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

ms=ma+mb
# ms.sort()
print 'Cutting list after reduce studs quantity:'
for i in range (0, len(ms)) : print ms[i]
file.close() 


line=''
for i  in range (len(ms)) :
    line1=ms[i][0]+chr(9)+ms[i][1]+chr(9)+ms[i][2]+chr(9)+ms[i][3]+chr(9)+ms[i][4]+chr(9)+ms[i][5]+chr(9)+ms[i][6]+chr(9)+ms[i][7]+chr(9)+ms[i][8]+chr(9)
    line2=str(ms[i][9])+chr(9)+ms[i][10]+chr(9)+ms[i][11]+chr(9)+ms[i][12]+chr(9)+ms[i][13]+chr(9)+ms[i][14]+chr(9)
    line3=str(ms[i][15])+chr(9)+ms[i][16]+chr(10)
    line+=line1+line2+line3

print  'Number of rows of file (Ilosc wierszy w pliku): ',i+2, '\n'  # max. 200

line=records[0]+line # put labels on top
# open and save file
pathin= 'C:\Grecon/reduce/'
filenameout=filename
fullpathout=fullpath
fs = open(fullpathout, 'w')
fs.write(line)
fs.close()
print 'Source file: ', fullpath
print 'Destination file: ', fullpathout
# for i in range (len(ms)) :  GreconVolue+=int(ms[i][2])
print 'See you soon :)'

