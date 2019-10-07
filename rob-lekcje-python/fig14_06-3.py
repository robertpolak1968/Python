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
mm = [[1]*17,[2]*17,[3]*17,[4]*17,[5]*17,[6]*17,[7]*17,[8]*17,[9]*17,[10]*17,
      [11]*17,[12]*17,[13]*17,[14]*17,[15]*17,[16]*17,[17]*17,[18]*17,[19]*17,[20]*17,
      [21]*17,[22]*17,[23]*17,[24]*17,[25]*17,[26]*17,[27]*17,[28]*17,[29]*17,[30]*17,
      [31]*17,[32]*17,[33]*17,[34]*17,[35]*17,[36]*17,[37]*17,[38]*17,[39]*17,[40]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[50]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[60]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[70]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[80]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[90]*17,
      [41]*17,[42]*17,[43]*17,[44]*17,[45]*17,[46]*17,[47]*17,[48]*17,[49]*17,[100]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[110]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[120]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[120]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[130]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[140]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[150]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[160]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[170]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[180]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[190]*17,
      [101]*17,[102]*17,[103]*17,[104]*17,[105]*17,[106]*17,[107]*17,[108]*17,[109]*17,[200]*17]   

red = []
redukcja = []
wymiary = []
sumkiwymiar = [0]*15000 #max lenght of timber 15000 mm

ilosckolumn=17 # number of colums "Grade", "Length" ....
iloscwierszy=0 # number of rows 0,1,2,3,...
j=0
for record in records:
    j+=1
    for i in range(0,ilosckolumn):
        #print 'j=',j, 'i=',i
        fields = record.split()     
        mr += [fields[ i ]] #split record for seperatly string for each column ... to database mr  

print 'j=', j
iloscwierszy=j #number or record in records (in file) 

for w in range (0,iloscwierszy) :
    for i in range (0,ilosckolumn):
        mm [w][i]= mr[i+ilosckolumn*w] # create data base for each row, w-rows, i-column

print  'Number of rows of file (Ilosc wierszyw pliku): ',iloscwierszy, # max. 200 

# print 'Ostatni wiersz : ',mm [iloscwierszy-1]
#for i in range (0, iloscwierszy) :
 #   print mm[i]


print 'Rows to reduce quantity, (Wiersze do redukcji) :'    
for i in range (0, iloscwierszy) :
    if mm [i][8] == '_' and mm[i][11]=='S': # 8-Remarks , 11-Code
        #print i, ':' ,mm[i]
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

print 'Reduced quantity of studs'

file.close()