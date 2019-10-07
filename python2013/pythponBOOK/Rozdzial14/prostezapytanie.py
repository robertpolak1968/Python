#!/usr/bin/env python

import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

cursor.execute("""
select pracownik.imie, pracownik.nazwisko, dzial.nazwa 
from pracownik, dzial
where pracownik.dzial = dzial.iddzialu
order by pracownik.nazwisko desc
""")

for row in cursor.fetchall(): 
    print row

cursor.close()
connection.close()
