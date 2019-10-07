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
print ''
j=0
mybase = []
mr =    []
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
      
   
red = []
dela = []
delb = []
redukcja = []
wymiary = []
sumkiwymiar = [0]*15000 #max lenght of timber 15000 mm
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


ilosckolumn=17 # number of colums "Grade", "Length" ....
iloscwierszy=0 # number of rows 0,1,2,3,...
j=0
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

print  'Number of rows of file (Ilosc wierszyw pliku): ',iloscwierszy, # max. 200 
print ''
# print 'Ostatni wiersz : ',mm [iloscwierszy-1]
#for i in range (0, iloscwierszy) :
 #   print mm[i]


print 'Rows to reduce quantity, (Wiersze do redukcji) :'
print''

for i in range (0, iloscwierszy) :
    if mm [i][8] == '_' and mm[i][11]=='S': # 8-Remarks , 11-Code
        print i, ':' ,mm[i]
        red.append (i) # data base with index of mm to reduce or delete 
       
for k in red :
    # print k,mm[k]
    redukcja.append (mm[k]) #create database dekukcja with records to reduce form mm


#redukcja[1][1].count (redukcja[1][1])
#for i in range (len(redukcja)): print redukcja[i][1]


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


print 'Rows with reduced quantity, (Wiersze po redukcji) :'
print''
i=0
profil = mm[1][0]
for wymiar in wymiary :
    i+=1
    ma [i-1]= [redukcja [0][0],wymiary[i-1],redukcja [0][2],redukcja [0][3],redukcja [0][4],redukcja [0][5],redukcja [0][6],redukcja [0][7],redukcja [0][8],
        sumkiwymiar[int(wymiary[i-1])],redukcja [0][10],redukcja [0][11],redukcja [0][12],redukcja [0][13],redukcja [0][14],redukcja [0][15],redukcja [0][16]]
    # ma data base with reduced quantity

print 'Reduced quantity of studs: Done'

for i in red :
    mm.remove (mm[i])# delete all reduced rows !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
i=0
profil = mm[1][0]
for m in range (len (mm)-1) :
    i+=1
    if mm[i][0] == profil :
        mb [i] = mm[i]
        #[mm [i][0],mm[i][1],mm [i][2],mm [i][3],mm [i][4],mm [i][5],m [i][6],mm [i][7],mm [i][8],
        #mm[i][9],mm [i][10],mm [i][11],mm [i][12],mm [i][13],mm [i][14],mm [i][15],mm [i][16]]
    


print 'Deleted Reduced rows '

for i in range (0, len(ma)) :
    if profil not in ma[i] : # data base with index empty raws ma
        dela.append (i)

for i in range (0, len(ma)) :
    if profil not in mb[i] : # data base with index empty raws mb
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

print 'ma'
for i in range (0, len(ma)) : print ma[i] 
   
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

print 'mb'   
for i in range (0, len(mb)) : print mb[i]
    


print 'See you soon :)'



# sumkiwymiar[wymiar]
file.close()