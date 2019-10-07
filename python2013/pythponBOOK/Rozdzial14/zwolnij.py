#!/usr/bin/env python

import sys
import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

employee = sys.argv[1]

# Zapytanie znajduj¹ce identyfikator pracownika.
query = """
select p.idprac
from uzytkownik u, pracownik p 
where nazwauz=? and u.idprac = p.idprac
"""
cursor.execute(query,(employee,));
for row in cursor.fetchone(): 
    if (row != None):
        empid = row

# Usuñ pracownika
cursor.execute("delete from pracownik where idprac=?", (empid,))

connection.commit()
cursor.close()
connection.close()
