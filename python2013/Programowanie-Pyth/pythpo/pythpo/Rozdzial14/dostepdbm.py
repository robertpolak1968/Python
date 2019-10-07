#!/usr/bin/env python

import anydbm
import whichdb

# Sprwd� typ.
print "Typ pliku DBM =", whichdb.whichdb('witryny')

# Otw�rz istniej�cy plik.
db = anydbm.open('witryny', 'w')

# Dodaj nowy element.
db['helion.pl'] = 'Witryna wydawnictwa Helion'

# Sprawd�, czy wcze�niejszy element istnieje.
if db['www.python.org'] != None:
    print 'Znaleziono www.python.org'
else:
    print 'B��d: brakuje elementu'


# Przejd� przez wszystkie klucze. Mo�e dzia�a� powoli.
# Mo�e u�ywa� du�o pami�ci.
for key in db.keys():
    print "Klucz =",key," warto�� =",db[key]

del db['helion.pl']
print "Po usuni�ciu helion.pl otrzymujemy:"

for key in db.keys():
    print "Klucz =",key," warto�� =",db[key]

# Zamknij i zapisz na dysk.
db.close()
