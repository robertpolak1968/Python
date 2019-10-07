#!/usr/bin/env python

import os
import gadfly
connection = gadfly.gadfly()

os.mkdir('db')

connection.startup('pydb', 'db')

cursor = connection.cursor()


# Utwórz tabele.
cursor.execute("""
create table pracownik 
    (idprac integer, 
    imie varchar, 
    nazwisko varchar, 
    dzial integer,
    kierownik integer,
    telefon varchar)
""")

cursor.execute("""
create table dzial 
    (iddzialu integer, 
    nazwa varchar, 
    kierownik integer)
""")

cursor.execute("""
create table uzytkownik 
    (iduzyt integer, 
    nazwauz varchar, 
    idprac integer)
""")

# Utwórz indeksy.
cursor.execute("""create index iduzyt on uzytkownik (iduzyt)""")
cursor.execute("""create index idprac on pracownik (idprac)""")
cursor.execute("""create index iddzialu on dzial (iddzialu)""")
cursor.execute("""create index kodzial on pracownik (dzial)""")
cursor.execute("""create index kier on pracownik (kierownik)""")
cursor.execute("""create index idpraco on uzytkownik (idprac)""")
cursor.execute("""create index kierdzial on dzial (kierownik)""")


connection.commit()
cursor.close()

connection.close()
