#!/usr/bin/env python

import sys
import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

newmgr   = sys.argv[2]
employee = sys.argv[1]

# Zapytanie znajduj¹ce identyfikator pracownika.
query = """
select p.idprac
from uzytkownik u, pracownik p 
where nazwauz=? and u.idprac = p.idprac
"""

cursor.execute(query,(newmgr,));
for row in cursor.fetchone(): 
    if (row != None):
        mgrid = row

# Zauwa¿, w jaki sposób stosujemy to samo zapytanie, ale z innymi danymi.
cursor.execute(query,(employee,));
for row in cursor.fetchone(): 
    if (row != None):
        empid = row

# Zmodyfikuj dane pracownika.
cursor.execute("update pracownik set kierownik=? where idprac=?", (mgrid,empid))

connection.commit()
cursor.close()
connection.close()
