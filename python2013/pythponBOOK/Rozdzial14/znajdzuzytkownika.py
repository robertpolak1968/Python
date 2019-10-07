#!/usr/bin/env python

import sys
import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

username = sys.argv[1]

query = """
select u.nazwauz,p.imie,p.nazwisko,k.imie,k.nazwisko, d.nazwa
from uzytkownik u, pracownik p, pracownik k, dzial d where nazwauz=?
and u.idprac = p.idprac
and p.kierownik = k.idprac
and p.dzial = d.iddzialu
"""

cursor.execute(query, (username,))
for row in cursor.fetchall(): 
    (username,firstname,lastname,mgr_firstname,mgr_lastname,dept) = row
    name=firstname + " " + lastname
    manager=mgr_firstname + " " + mgr_lastname
    print username,":",name,"kierowany przez",manager,"z dzia³u",dept

cursor.close()
connection.close()

