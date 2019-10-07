# Fig. 14.6: fig14_06.py
# Reading and printing a file.

import sys

# open file
try:
    file = open( "grecon.txt", "r" ) # open file txt from cuting list grecon folder
# file = open( "c:\robert/rob-lekcje/grecon.txt", "r" )
# open('C:\Robert/rob-lekcje/grecon.txt', 'r')    
except IOError:
    print >> sys.stderr, "File could not be opened"
    sys.exit( 1 )

records = file.readlines() # retrieve list of lines in file , 

print ''
#print "Grade".ljust( 10 ), # 0
#print "Length".ljust( 10 ),
#print "Value".ljust( 10 ),
#print "Min.mult.".ljust( 10 ),
#print "Max.mult.".ljust( 10 ),
#print "BoxAlignm.".ljust( 10 ),
#print "Box".ljust( 10 ),
#print "Box1".ljust( 10 ),
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
mybase = []
mr =    []
red = []
dela = []
delb = []
redukcja = []
wymiary = []
sumkiwymiar = [0]*15000 #max lenght of timber 15000 mm
ilosckolumn=17 # number of colums "Grade", "Length" ....
iloscwierszy=0 # number of rows 0,1,2,3,...

for record in records:
    j+=1
    for i in range(0,ilosckolumn):
        #print 'j=',j, 'i=',i
        fields = record.split()     
        mr += [fields[ i ]] #split record for seperatly string for each column ... to database mr  

iloscwierszy=j #number or record in records (in file) 

for w in range (0,iloscwierszy) :
    for i in range (0,ilosckolumn):
        mm [w][i]= mr[i+ilosckolumn*w] # create data base for each row, w-rows, i-column
print ''
print  'Number of rows of file (Ilosc wierszyw pliku): ',iloscwierszy, # max. 200 
print ''
print 'Rows to reduce quantity, (Wiersze do redukcji) :'
print''

for i in range (0, iloscwierszy) :
    if mm [i][8] == '_' and (mm[i][11]=='S' or mm[i][11]=='FD' or mm[i][11]=='D') and (int(mm[i][9])>0): # 8-Remarks , 11-Code, 9  - Quantity
        print i, ':' ,mm[i]
        red.append (i) # data base with index of mm to reduce or delete 
       
for k in red :
    # print k,mm[k]
    redukcja.append (mm[k]) #create database dekukcja with records to reduce form mm


for i in range (len(redukcja)):
    wymiary.append(redukcja[i][1]) # create list of length of timber to do reduce quantity


for wymiar in wymiary: #delete repeated lenght from list wymiary 
    wymiary.count(wymiar)
    ilosc=wymiary.count(wymiar)
    if ilosc>=2:
        usunac=wymiar
        wymiary.remove(usunac)


for k in range (len (wymiary)) :
    for i in range (len (redukcja)) :
        # print k,i, wymiary[k] ,redukcja[i][1].count (wymiary[k])
        if redukcja[i][1].count (wymiary[k])<> 0 : sumkiwymiar[int(wymiary[k])] += int(redukcja[i][9])

for i in sumkiwymiar :
    if sumkiwymiar[i] <>0 :
       print i,sumkiwymiar[i]



i=0
profil = mm[1][0]
for wymiar in wymiary :
    i+=1
    ma [i-1]= [redukcja [0][0],wymiary[i-1],redukcja [0][2],redukcja [0][3],redukcja [0][4],redukcja [0][5],redukcja [0][6],redukcja [0][7],redukcja [0][8],
        sumkiwymiar[int(wymiary[i-1])],redukcja [0][10],redukcja [0][11],redukcja [0][12],redukcja [0][13],redukcja [0][14],redukcja [0][15],redukcja [0][16]]
    # ma data base with reduced quantity

# 'Rows with reduced quantity, (Wiersze po redukcji) : ma'

print 'Reduced quantity of studs: Done'

for i in red :
    mm.remove (mm[i])# delete all reduced rows !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
i=0
profil = mm[1][0]
for m in range (len (mm)-1) :
    i+=1
    if mm[i][0] == profil :
        mb [i] = mm[i]
      
print 'Deleted Reduced rows: Done'

for i in range (0, len(ma)) :
    if profil not in ma[i] : # data base with index empty raws ma (for future)
        dela.append (i)

for i in range (0, len(ma)) :
    if profil not in mb[i] : # data base with index empty raws mb (for future)
        delb.append (i)

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

lines= []
ms=ma+mb
print 'Cutting list after reduce studs quantity:'
for i in range (0, len(ms)) : print ms[i]
file.close() 

line=''
for i  in range (len(ms)) :
    line1=ms[i][0]+chr(9)+ms[i][1]+chr(9)+ms[i][2]+chr(9)+ms[i][3]+chr(9)+ms[i][4]+chr(9)+ms[i][5]+chr(9)+ms[i][6]+chr(9)+ms[i][7]+chr(9)+ms[i][8]+chr(9)
    line2=str(ms[i][9])+chr(9)+ms[i][10]+chr(9)+ms[i][11]+chr(9)+ms[i][12]+chr(9)+ms[i][13]+chr(9)+ms[i][14]+chr(9)
    line3=ms[i][15]+chr(9)+ms[i][16]+chr(10)
    line+=line1+line2+line3

print  'Number of rows of file (Ilosc wierszy w pliku): ',i+2, # max. 200
print ''
line=records[0]+line
fs = open('Reducedstuds.txt', 'w')
fs.write(line)
fs.close()

print 'See you soon :)'
