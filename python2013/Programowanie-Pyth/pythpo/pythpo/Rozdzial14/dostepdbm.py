#!/usr/bin/env python

import anydbm
import whichdb

# SprwdŸ typ.
print "Typ pliku DBM =", whichdb.whichdb('witryny')

# Otwórz istniej¹cy plik.
db = anydbm.open('witryny', 'w')

# Dodaj nowy element.
db['helion.pl'] = 'Witryna wydawnictwa Helion'

# SprawdŸ, czy wczeœniejszy element istnieje.
if db['www.python.org'] != None:
    print 'Znaleziono www.python.org'
else:
    print 'B³¹d: brakuje elementu'


# PrzejdŸ przez wszystkie klucze. Mo¿e dzia³aæ powoli.
# Mo¿e u¿ywaæ du¿o pamiêci.
for key in db.keys():
    print "Klucz =",key," wartoœæ =",db[key]

del db['helion.pl']
print "Po usuniêciu helion.pl otrzymujemy:"

for key in db.keys():
    print "Klucz =",key," wartoœæ =",db[key]

# Zamknij i zapisz na dysk.
db.close()
