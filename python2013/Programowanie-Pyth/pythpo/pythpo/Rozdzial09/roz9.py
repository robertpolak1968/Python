# Przyk�ady nie s� osobnymi funkcjami w rozdziale. Tutaj zosta�y wyizolowane
# aby u�atwi� ich testowanie po wczytaniu ca�ego pliku.

def lambda_sample():
    # U�ycie labmda w funkcji filter.
    filter_me = [1, 2, 3, 4, 6,7 ,8, 11, 12, 14, 15, 19, 22]
    # Lambda zwr�ci True tylko dla liczb parzystych (poniewa� x%2 wynosi 1
    # dla liczb nieparzystych)
    result = filter(lambda x: x%2 == 0, filter_me)
    print result


def lambda_named_sample():
    # U�ycie labmda w funkcji filter, ale po�rednio przez nazw�.
    filter_me = [1, 2, 3, 4, 6,7 ,8, 11, 12, 14, 15, 19, 22]
    # Lambda zwr�ci True tylko dla liczb parzystych (poniewa� x%2 wynosi 1
    # dla liczb nieparzystych)
    func = lambda x: x%2 == 0
    result = filter(func, filter_me)
    print result


def reduce_sample():
    # Wykorzystanie reduce i funkcji lambda do zamiany kilku ma�ych
    # liczb na jedn� bardzo du�� liczb�.
    reduce_me = [ 2, 4, 4, 2, 6 ]
    result = reduce(lambda first, second: first**second, reduce_me)
    print "Wynik redukcji: %d" % result


def map_sample():
    # Funkcja map wykonuje operacj� dla ka�dego elementu listy
    map_me = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
    result = map(lambda x: "Odczytana litera to %s" % x, map_me)
    print result


def list_comprehension_sample():
    # Wy�wietl tylko warto�ci parzyste.
    everything = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
    print [ x for x in everything if x%2 == 0 ]

def range_sample():
    # Utworzenie zakresu warto�ci jako listy.
    list = range (10, 20)
    print list

    # Funkcja range dzia�a inaczej po przekazaniu jednego argumentu.
    for number in range(10):
        print "Aktualna warto��: %d" % number

    # Zastosowanie kroku.
    for number in range(5, 55, 4):
        print "Liczby od 5 to 55 co 4: %d" % number

    # Klas� xrange warto stosowa� w przypadku bardz du�ych list.
    # Przedstaiamy j� tu tylko w ramach test�w, gdy� dla ma�ych list wystarczy range.
    for r in xrange(0, 10):
        print r


def string_substitution_sample():
    person = {"imi�": "Jan", "aparat": "Nikon", "ma�kuctwo": "lewor�czny", "zesp�": "Anio�ki", "instrument": "gitara"}

    print "%(imi�)s, %(aparat)s, %(zesp�)s" % person

    person["wzrost"] = 1.6
    person["waga"] = 80
    print "%(imi�)s, %(aparat)s, %(zesp�)s, %(wzrost)2.2f, %(waga)2.2f" % person    

    # Alternatywny spos�b wykonywania zast�pie�.
    import string
    person = {"imie": "Jan", "aparat": "Nikon", "mankuctwo": "leworeczny", "zespol": "Anio�ki", "instrument": "gitara"}
    person["wzrost"] = 1.6
    person["waga"] = 80
    t = string.Template("$imie ma $wzrost m wzrostu i wa�y $waga kg")
    print t.substitute(person)


def getopt_sample():
    import sys
    import getopt
    # Pami�taj, �e zerowy element sys.argv to tre�� polecenia wywo�uj�cego program.
    # Nie jest nam ona potrzebna.
    cmdline_params = sys.argv[1:]

    opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])
    print opts, args

    for option, parameter in opts:
   
        if option == '-h' or option == '--help':
            print "Program mo�na uruchomi� z opcj� -h lub --help, by wy�wietli� ten komunikat,"
            print "lub z opcj� -c albo --config=<plik>, by okre�li� po�o�enie pliku konfiguracyjnego"
            print
        if option in ('-c', '--config'): # oznacza to dok�adnie to samo, co powy�ej
            print "U�ywam pliku konfiguracyjnego %s" % parameter

def gnu_getopt_sample():
    import sys
    import getopt
    # Pami�taj, �e zerowy element sys.argv to tre�� polecenia wywo�uj�cego program.
    # Nie jest nam ona potrzebna.
    cmdline_params = sys.argv[1:]

    opts, args = getopt.gnu_getopt(cmdline_params, 'hc:', ['help', 'config='])
    print opts, args

    for option, parameter in opts:
   
        if option == '-h' or option == '--help':
            print "Program mo�na uruchomi� z opcj� -h lub --help, by wy�wietli� ten komunikat,"
            print "lub z opcj� -c albo --config=<plik>, by okre�li� po�o�enie pliku konfiguracyjnego"
            print
        if option in ('-c', '--config'): # oznacza to dok�adnie to samo, co powy�ej
            print "U�ywam pliku konfiguracyjnego %s" % parameter

def fork_sample():
    import os
    pid = os.fork()
    # po��czenie fork i exec
    print "drugi test"
    if pid == 0: # to jest potomek
        print "to jest potomek"
        print "uruchamiam inny program"
        os.execl('/bin/cat', 'cat', '/etc/motd')
    else:
        print "pid potomka: %d" % pid
        os.wait()        

def determine_platform_sample():
    import os, sys
    if sys.platform == 'win32':
        print "Uruchamiane w systemie Windows"
        command = "C:\\winnt\\system32\\cmd.exe"
        params = []
    
    if sys.platform == 'linux2':
        print "Uruchamiane w systemie Linux identyfikowanym przez %s" % sys.platform
        command = '/bin/uname'
        params = ['uname', '-a']

    print "Uruchamianie %s" % command
    os.spawnv(os.P_WAIT, command, params)


def os_system_sample():
    # funkcja system
    if sys.platform == 'win32':
        print "Uruchamiane w systemie Windows"
        command = "cmd.exe"

    if sys.platform == 'linux2':
        print "Uruchamiane w systemie"
        command = "uname -a"

    os.system(command)


def threading_sample():
    # kod dotycz�cy w�tk�w znajduje si� w osobnym pliku


    
def password_hashing_sample():
    import sha
    import random
    import base64

    def _gen_salt():
        salt = [chr(random.randint(0,255)) for i in range(4) ]
        return ''.join(salt)

    def make_pass(cleartext):
        salt = _gen_salt()
        text = salt + cleartext
        hash = sha.new(text).digest()
        data = salt + hash
        return base64.encodestring(data)

    def check_pass(cipher, cleartext):
        cipher = base64.decodestring(cipher)
        salt, hash = cipher[:4], cipher[4:]
        hash2 = sha.new(salt + cleartext).digest()
        return hash2 == hash

    if __name__ == '__main__':
        cipher = make_pass('TEST')
        for word in 'spam', 'TEST', 'Test', 'omlet':
            passwd = check_pass(cipher, word)
            print '%s: %d' % (word, passwd)    
