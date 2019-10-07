#!/usr/bin/env python

import gadfly.dbapi20

connection = gadfly.dbapi20.connect('pydb', 'db')

cursor = connection.cursor()

# Tworzy pracownik�w.
cursor.execute("""
insert into pracownik (idprac,imie,nazwisko,kierownik,dzial,telefon) 
values (1,'Eryk','Majski',1,1,'555-5555')""")

cursor.execute("""
insert into pracownik (idprac,imie,nazwisko,kierownik,dzial,telefon) 
values (2,'Piotr','Turek',2,3,'555-5554')""")

cursor.execute("""
insert into pracownik (idprac,imie,nazwisko,kierownik,dzial,telefon) 
values (3,'Anna','Waimer',2,2,'555-5553')""")

# Tworzy dzia�y.
cursor.execute("""
insert into dzial (iddzialu,nazwa,kierownik) 
values (1,'projektowy',1)""")

cursor.execute("""
insert into dzial (iddzialu,nazwa,kierownik) 
values (2,'zapewnienia jako�ci',2)""")

cursor.execute("""
insert into dzial (iddzialu,nazwa,kierownik) 
values (3,'operacyjny',2)""")

# Tworzy u�ytkownik�w.
cursor.execute("""
insert into uzytkownik (iduzyt,nazwauz,idprac) 
values (1,'erykm',1)""")

cursor.execute("""
insert into uzytkownik (iduzyt,nazwauz,idprac) 
values (2,'piotr',2)""")

cursor.execute("""
insert into uzytkownik (iduzyt,nazwauz,idprac) 
values (3,'anna',3)""")

connection.commit()

   
cursor.close()

connection.close()
