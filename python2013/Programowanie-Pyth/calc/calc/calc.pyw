#!/usr/bin/env python

ver = " Kalkulator v1.5 (12.03.2007) by Tom'Ash "
tytul = "Kalkulator by Tom'Ash"

helptytul = "Pomoc - " + tytul
zlywynik = " NIEPRAWIDLOWE DZIALANIE !!! "
HELP = 0
cyfry1 = "0123456789)ABCie"  # "*", "/" i "**"
cyfry2 = "0123456789"        # "."
cyfry3 = " (*"               # zmienne i stale


from sys import exit
def bad_import( modul ):
    print "\n\nNie mozna zaimportowac modulu \"" + modul + "\" !!!\n" +\
          "Praca programu zostaje przerwana!"
    exit()

try: from math import *
except: bad_import( "math" )
try: from Tkinter import *
except: bad_import( "Tkinter" )
try: import tkFont
except: bad_import( "tkFont" )
try: from tkMessageBox import *
except: bad_import( "tkMessageBox" )



A, B, C = 0, 0, 0
tlo  = "#3D8B8F" #stardardowe obliczeniowe i cyfry
tlo2 = "#00A3D2" #funkcjonarne
tlo3 = "#9E72B1" #obliczeniowe
tlo4 = "#FFFF80" #zmienne
tloF = "#3D8B8F" #inne funkcje
okno = Tk()
okno.title( tytul )
czcionka = tkFont.Font( font=( 'Courier', 10, 'bold' ) )
czcionka2 = tkFont.Font( font=( 'Courier', 5, 'bold' ) )
pole = Entry( okno )
pole.config( width=50, fg='black', bg='#FFFFB7', font=czcionka )
pole.grid( row=0, column=1, columnspan=9, pady=10 )

def blad(): showwarning("Blad!", "Wpisano nieprawidlowa wartosc")



# ---------------------------------- definicje przyciskow --------------------------------

def zero():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "0" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '0')
def jeden():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "1" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '1')
def dwa():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "2" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '2')
def trzy():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "3" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '3')
def cztery():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "4" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '4')
def piec():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "5" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '5')
def szesc():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "6" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '6')
def siedem():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "7" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '7')
def osiem():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "8" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '8')
def dziewiec():
    if HELP: showinfo(helptytul, 'Dopisuje cyfre "9" do obszaru wyswietlania kalkulatora')
    else: pole.insert(END, '9')
def kropka():
    if HELP: showinfo(helptytul, 'Wstawia separator dziesietny (kropka)')
    elif pole.get()[-1:] in cyfry2: pole.insert(END, '.')
def dodac():
    if HELP: showinfo(helptytul, 'Dopisuje "+" (oblicza sume)')
    else: pole.insert(END, ' + ')
def odjac():
    if HELP: showinfo(helptytul, 'Dopisuje "-" (oblicza roznice)')
    else: pole.insert(END, ' - ')
def razy():
    if HELP: showinfo(helptytul, 'Dopisuje "*" (oblicza iloczyn)')
    elif pole.get()[-1:] in cyfry1 and pole.get() != '': pole.insert(END, ' * ')
def podzielic_na():
    if HELP: showinfo(helptytul, 'Dopisuje "/" (oblicza iloraz)')
    elif pole.get()[-1:] in cyfry1 and pole.get() != '':
        formula = pole.get()
        if not '.' in formula:
            if formula[-1:] == '0' or formula[-1:] == '1' or formula[-1:] == '2' or formula[-1:] == '3' or formula[-1:] == '4' or formula[-1:] == '5' or formula[-1:] == '6' or formula[-1:] == '7' or formula[-1:] == '8' or formula[-1:] == '9':
                pole.insert(END, '.0 / ')
            else: pole.insert(END, ' / ')
        else: pole.insert(END, ' / ')
def CE():
    if HELP: showinfo(helptytul, 'Kasuje obecne obliczenia')
    else: pole.delete(0,END)
def reset():
    if HELP: showinfo(helptytul, 'Kasuje obecne obliczenia i zmienne  "A"  "B"  "C"')
    else:
        global A, B, C
        CE()
        A, B, C = '', '', ''

def nawias1():
    if HELP: showinfo(helptytul, 'Dopisuje "(" (otwarcie nawiasu)\nMozna stosowac kilkakrotnie np. "(((5+5)*2)+9)*3"')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '': pole.insert(END, '(')
def nawias2():
    if HELP: showinfo(helptytul, 'Dopisuje ")" (zamkniecie nawiasu)\nMozna stosowac kilkakrotnie np. "(((5+5)*2)+9)*3"')
    else: pole.insert(END, ')')
def PI():
    if HELP: showinfo(helptytul, 'Dopisuje liczbe "pi" (3,1415...)')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '': pole.insert(END, 'pi')
def E():
    if HELP: showinfo(helptytul, 'Dopisuje liczbe "e" (2,7182...)')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '': pole.insert(END, 'e')
def potega1():
    if HELP: showinfo(helptytul, 'Dopisuje "**" (potegowanie)\nNp. "2 **5" podniesie 2 do potegi 5')
    elif pole.get()[-1:] in cyfry1 and pole.get() != '': pole.insert(END, ' **')

def potega2():
    if HELP: showinfo(helptytul, 'Oblicza kwadrat wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(pow(eval(formula), 2))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def pierwiastek():
    if HELP: showinfo(helptytul, 'Oblicza pierwiastek kwadratowy z obenie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(sqrt(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def SIN():
    if HELP: showinfo(helptytul, 'Oblicza sinus obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(sin(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)
def COS():
    if HELP: showinfo(helptytul, 'Oblicza cosinus obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(cos(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)
def TAN():
    if HELP: showinfo(helptytul, 'Oblicza tangens obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(tan(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def hyp_SIN():
    if HELP: showinfo(helptytul, 'Oblicza sinus hiperboliczny obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(sinh(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)
def hyp_COS():
    if HELP: showinfo(helptytul, 'Oblicza cosinus hiperboliczny obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(cosh(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)
def hyp_TAN():
    if HELP: showinfo(helptytul, 'Oblicza tangens hiperboliczny obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(tanh(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def LOG():
    if HELP: showinfo(helptytul, 'Oblicza logarytm naturalny (o podstawie e) obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(log(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)
def LOG_10():
    if HELP: showinfo(helptytul, 'Oblicza logarytm dziesietny (o podstawie 10) obecnie wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str(log10(eval(formula)))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def Del():
    if HELP: showinfo(helptytul, 'Usuwa ostatni znak wyswietlanej liczby')
    else:
        formula = pole.get()
        if formula[-1:] == ' ':
            while 1:
                formula = formula[:-1]
                CE()
                pole.insert(END, formula)
                formula = pole.get()
                if formula[-1:] == ' ': continue
                else: break
        else:
            formula = formula[:-1]
            CE()
            pole.insert(END, formula)

def info():
    if HELP: showinfo(helptytul, 'Wyswietla informacje na temat wersji programu')
    else:
        if pole.get() == ver: CE()
        else:
            CE()
            pole.insert(END, ver)

def oblicz():
    if HELP: showinfo(helptytul, 'Wykonuje obecnie wyswietlane dzialanie')
    else:
        formula = pole.get()
        if formula:
            try: wynik = str( eval( formula ) )
            except: wynik = zlywynik
        else: wynik = ''
        CE()
        pole.insert(END, wynik)

def ulamek():
    if HELP: showinfo(helptytul, 'Oblicza odwrotnosc wyswietlanej liczby')
    else:
        formula = pole.get()
        try: wynik = str( 1.0 / ( eval( formula ) ) )
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def FLOOR():
    if HELP: showinfo(helptytul, 'Zaniza wynik do liczby calkowitej')
    else:
        formula = pole.get()
        try: wynik = str(floor((eval(formula))))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def CEIL():
    if HELP: showinfo(helptytul, 'Zawyza wynik do liczby calkowitej')
    else:
        formula = pole.get()
        try: wynik = str(ceil((eval(formula))))
        except: wynik = zlywynik
        CE()
        pole.insert(END, wynik)

def ZmienZnak():
    if HELP: showinfo(helptytul, 'Zmienia znak wyswietlanej liczby')
    else:
        formula = pole.get()
        oblicz()
        formula = pole.get()
        if formula[:1] == '-': wynik = formula[1:]
        elif formula[:2] == ' -': ynik = formula[2:]
        else: wynik = ' -' + formula
        CE()
        pole.insert(END, wynik)

def pomoc():
    global HELP
    if HELP == 1:
        a = askquestion(helptytul, 'Wlacza/wylacza tryb pomocy.\n\nWyjsc z pomocy?')
        if a == 'yes':
            pole.delete(0,END)
            HELP = 0
    elif HELP == 0:
        a = askquestion(helptytul, 'Uruchomic tryb pomocy?')
        if a == 'yes':
            pole.delete(0,END)
            pole.insert(END, 'TRYB POMOCY')
            HELP = 1
    return HELP

def zmiennaA1():
    if HELP: showinfo(helptytul, 'Oblicza wyswietlane dzialanie i wynik zapisuje jako zmienna "A"')
    else:
        global A
        try: A = eval(pole.get())
        except: pole.insert(END, zlywynik)
def zmiennaB1():
    if HELP: showinfo(helptytul, 'Oblicza wyswietlane dzialanie i wynik zapisuje jako zmienna "B"')
    else:
        global B
        try: B = eval(pole.get())
        except: pole.insert(END, zlywynik)
def zmiennaC1():
    if HELP: showinfo(helptytul, 'Oblicza wyswietlane dzialanie i wynik zapisuje jako zmienna "C"')
    else:
        global C
        try: C = eval(pole.get())
        except: pole.insert(END, zlywynik)

def zmiennaA2():
    if HELP: showinfo(helptytul, 'Wstawia zmienna "A"')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '':
        global A
        try: pole.insert(END, 'A')
        except: pole.insert(END, '')
def zmiennaB2():
    if HELP: showinfo(helptytul, 'Wstawia zmienna "B"')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '':
        global B
        try: pole.insert(END, 'B')
        except: pole.insert(END, '')
def zmiennaC2():
    if HELP: showinfo(helptytul, 'Wstawia zmienna "C"')
    elif pole.get()[-1:] in cyfry3 or pole.get() == '':
        global C
        try: pole.insert(END, 'C')
        except: pole.insert(END, '')

def wyjdz():
    if HELP: showinfo(helptytul, 'Zamyka program')
    else: sys.exit()
            

# --------------------------------------- "porownaj" -------------------------------------

def startP():
    if HELP: showinfo(helptytul, "Porownuje dwie liczby (otwiera nowe okno)\n"+\
                      "Mozna pobrac liczbe z glownego okna kalkulatora lub wpisac nowe dzialanie.\n"+\
                      "Przy wpisywaniu dzialania mozna korzystac z funkcji i zmiennych np. sqrt(16), sin(A), floor(pi), itp.")
    else:
        global oknoP, pole1, pole2
        oknoP = Tk()
        oknoP.title(tytul)
        pole1 = Entry(oknoP)
        pole1.config(width=40, fg='black', bg='#FFFFB7', font=czcionka)
        pole1.grid(row=1, column=0, columnspan=3, pady=10, sticky=NSEW)
        pole2 = Entry(oknoP)
        pole2.config(width=40, fg='black', bg='#FFFFB7', font=czcionka)
        pole2.grid(row=1, column=4, columnspan=3, pady=10, sticky=NSEW)
        button = Button(oknoP, text='wyczysc', command=wyczyscP1, bg=tloF, font=czcionka)
        button.grid(row=2, column=0, sticky=NSEW)
        button = Button(oknoP, text='pobierz', command=pobierzP1, bg=tloF, font=czcionka)
        button.grid(row=2, column=1, sticky=NSEW)
        button = Button(oknoP, text='oblicz', command=obliczP1L, bg=tloF, font=czcionka)
        button.grid(row=2, column=2, sticky=NSEW)
        button = Button(oknoP, text='Porownaj', command=sprawdzP, bg=tloF, font=czcionka)
        button.grid(row=3, column=3, sticky=NSEW)
        button = Button(oknoP, text='oblicz', command=obliczP2L, bg=tloF, font=czcionka)
        button.grid(row=2, column=4, sticky=NSEW)
        button = Button(oknoP, text='pobierz', command=pobierzP2, bg=tloF, font=czcionka)
        button.grid(row=2, column=5, sticky=NSEW)
        button = Button(oknoP, text='wyczysc', command=wyczyscP2, bg=tloF, font=czcionka)
        button.grid(row=2, column=6, sticky=NSEW)
        oknoP.mainloop()
def wyczyscP1(): pole1.delete(0, END)
def wyczyscP2(): pole2.delete(0, END)
def obliczP1():
    global wynik1, wynik1L
    formula1 = pole1.get()
    wyczyscP1()
    if formula1 == '':
        wynik1, wynik1L = '0', 0
    else:
        try:
            wynik1 = str(eval(formula1))
            wynik1L = float(wynik1)
        except: wynik1 = False
def obliczP2():
    global wynik2, wynik2L
    formula2 = pole2.get()
    wyczyscP2()
    if formula2 == '':
        wynik2, wynik2L = '0', 0
    else:
        try:
            wynik2 = str(eval(formula2))
            wynik2L = float(wynik2)
        except: wynik2 = False
def obliczP1L():
    global wynik1L
    obliczP1()
    wyczyscP1()
    pole1.insert(END, wynik1L)
def obliczP2L():
    global wynik2L
    obliczP2()
    wyczyscP2()
    pole2.insert(END, wynik2L)
def pobierzP1():
    wyczyscP1()
    formula = pole.get()
    pole1.insert(END, formula)
def pobierzP2():
    wyczyscP2()
    formula = pole.get()
    pole2.insert(END, formula)


def sprawdzP():
    global wynik1, wynik1L, wynik2, wynik2L
    obliczP1()
    obliczP2()
    if wynik1 != False and wynik2 != False:
        if wynik1L > wynik2L:
            wynikP = wynik1 + ' > ' + wynik2
        elif wynik1L < wynik2L:
            wynikP = wynik1 + ' < ' + wynik2
        elif wynik1L == wynik2L:
            wynikP = wynik1 + ' = ' + wynik2
    else:
        if wynik1 == False and wynik2 == False:
            wynikP = 'Wprowadzone dzialania zawieraja bledy!'
        elif wynik1 == False:
            wynikP = 'Pierwsze dzialanie zawiera blad!'
        elif wynik2 == False:
            wynikP = 'Drugie dzialanie zawiera blad!'
    showinfo(tytul, wynikP)



# ------------------------------------------ przyciski ------------------------------------

button = Button(okno, text='<--', command=Del, bg=tlo2, font=czcionka)
button.grid(row=1, column=1, sticky=NSEW, columnspan = 4)
button = Button(okno, text='CE', command=CE, bg=tlo2, font=czcionka)
button.grid(row=1, column=5, sticky=NSEW, columnspan = 4)
button = Button(okno, text='C', command=reset, bg=tlo2, font=czcionka)
button.grid(row=1, column=9, sticky=NSEW)

button = Button(okno, text='1', command=jeden, bg=tlo, font=czcionka)
button.grid(row=6, column=1, sticky=NSEW)
button = Button(okno, text='2', command=dwa, bg=tlo, font=czcionka)
button.grid(row=6, column=2, sticky=NSEW)
button = Button(okno, text='3', command=trzy, bg=tlo, font=czcionka)
button.grid(row=6, column=3, sticky=NSEW)
button = Button(okno, text='4', command=cztery, bg=tlo, font=czcionka)
button.grid(row=5, column=1, sticky=NSEW)
button = Button(okno, text='5', command=piec, bg=tlo, font=czcionka)
button.grid(row=5, column=2, sticky=NSEW)
button = Button(okno, text='6', command=szesc, bg=tlo, font=czcionka)
button.grid(row=5, column=3, sticky=NSEW)
button = Button(okno, text='7', command=siedem, bg=tlo, font=czcionka)
button.grid(row=4, column=1, sticky=NSEW)
button = Button(okno, text='8', command=osiem, bg=tlo, font=czcionka)
button.grid(row=4, column=2, sticky=NSEW)
button = Button(okno, text='9', command=dziewiec, bg=tlo, font=czcionka)
button.grid(row=4, column=3, sticky=NSEW)
button = Button(okno, text='0', command=zero, bg=tlo, font=czcionka)
button.grid(row=7, column=1, sticky=NSEW, columnspan = 2)

button = Button(okno, text='.', command=kropka, bg=tlo, font=czcionka)
button.grid(row=7, column=3, sticky=NSEW)
button = Button(okno, text='/', command=podzielic_na, bg=tlo, font=czcionka)
button.grid(row=3, column=2, sticky=NSEW)
button = Button(okno, text='*', command=razy, bg=tlo, font=czcionka)
button.grid(row=3, column=3, sticky=NSEW)
button = Button(okno, text='-', command=odjac, bg=tlo, font=czcionka)
button.grid(row=3, column=4, sticky=NSEW)
button = Button(okno, text='+', command=dodac, bg=tlo, font=czcionka)
button.grid(row=4, column=4, sticky=NSEW, rowspan=2)
button = Button(okno, text='=', command=oblicz, bg=tlo, font=czcionka)
button.grid(row=6, column=4, sticky=NSEW, rowspan=2)

button = Button(okno, text='**', command=potega1, bg=tlo3, font=czcionka)
button.grid(row=3, column=9, sticky=NSEW)
button = Button(okno, text='= x^2', command=potega2, bg=tlo3, font=czcionka)
button.grid(row=5, column=8, sticky=NSEW)
button = Button(okno, text='=sqrt', command=pierwiastek, bg=tlo3, font=czcionka)
button.grid(row=5, column=7, sticky=NSEW)

button = Button(okno, text='(', command=nawias1, bg=tlo3, font=czcionka)
button.grid(row=3, column=7, sticky=NSEW)
button = Button(okno, text=')', command=nawias2, bg=tlo3, font=czcionka)
button.grid(row=3, column=8, sticky=NSEW)

button = Button(okno, text='= +/-', command=ZmienZnak, bg=tlo3, font=czcionka)
button.grid(row=5, column=9, sticky=NSEW)
button = Button(okno, text='=floor', command=FLOOR, bg=tlo3, font=czcionka)
button.grid(row=4, column=8, sticky=NSEW)
button = Button(okno, text='=ceil', command=CEIL, bg=tlo3, font=czcionka)
button.grid(row=4, column=7, sticky=NSEW)
button = Button(okno, text='= 1/x', command=ulamek, bg=tlo3, font=czcionka)
button.grid(row=4, column=9, sticky=NSEW)

button = Button(okno, text='=sin', command=SIN, bg=tlo3, font=czcionka)
button.grid(row=6, column=7, sticky=NSEW)
button = Button(okno, text='=cos', command=COS, bg=tlo3, font=czcionka)
button.grid(row=6, column=8, sticky=NSEW)
button = Button(okno, text='=tan', command=TAN, bg=tlo3, font=czcionka)
button.grid(row=6, column=9, sticky=NSEW)
button = Button(okno, text='=hyp sin', command=hyp_SIN, bg=tlo3, font=czcionka)
button.grid(row=7, column=7, sticky=NSEW)
button = Button(okno, text='=hyp cos', command=hyp_COS, bg=tlo3, font=czcionka)
button.grid(row=7, column=8, sticky=NSEW)
button = Button(okno, text='=hyp tan', command=hyp_TAN, bg=tlo3, font=czcionka)
button.grid(row=7, column=9, sticky=NSEW)

button = Button(okno, text='=log', command=LOG, bg=tlo3, font=czcionka)
button.grid(row=10, column=7, sticky=NSEW)
button = Button(okno, text='=log10', command=LOG_10, bg=tlo3, font=czcionka)
button.grid(row=10, column=8, sticky=NSEW)

button = Button(okno, text='A+', command=zmiennaA1, bg=tlo4, font=czcionka)
button.grid(row=11, column=1, sticky=NSEW)
button = Button(okno, text='B+', command=zmiennaB1, bg=tlo4, font=czcionka)
button.grid(row=11, column=2, sticky=NSEW)
button = Button(okno, text='C+', command=zmiennaC1, bg=tlo4, font=czcionka)
button.grid(row=11, column=3, sticky=NSEW)
button = Button(okno, text='A', command=zmiennaA2, bg=tlo4, font=czcionka)
button.grid(row=10, column=1, sticky=NSEW)
button = Button(okno, text='B', command=zmiennaB2, bg=tlo4, font=czcionka)
button.grid(row=10, column=2, sticky=NSEW)
button = Button(okno, text='C', command=zmiennaC2, bg=tlo4, font=czcionka)
button.grid(row=10, column=3, sticky=NSEW)
button = Button(okno, text='pi', command=PI, bg=tlo4, font=czcionka)
button.grid(row=10, column=4, sticky=NSEW)
button = Button(okno, text='e', command=E, bg=tlo4, font=czcionka)
button.grid(row=11, column=4, sticky=NSEW)

button = Button(okno, text='> == <', command=startP, bg=tlo2, font=czcionka)
button.grid(row=10, column=9, sticky=NSEW)

button = Button(okno, text='pomoc', command=pomoc, bg=tlo2, font=czcionka)
button.grid(row=11, column=7, sticky=NSEW)
button = Button(okno, text='info', command=info, bg=tlo2, font=czcionka)
button.grid(row=11, column=8, sticky=NSEW)
button = Button(okno, text='X', command=wyjdz, bg='#FF0000', font=czcionka)
button.grid(row=11, column=9, sticky=NSEW)

button = Button(okno)
button.grid(row=2, column=13, sticky=NSEW)
button = Button(okno)
button.grid(row=9, column=13, sticky=NSEW)
button = Button(okno)
button.grid(row=1, column=0, rowspan=12, sticky=NSEW)
button = Button(okno)
button.grid(row=1, column=13, rowspan=12, sticky=NSEW)



okno.mainloop()

