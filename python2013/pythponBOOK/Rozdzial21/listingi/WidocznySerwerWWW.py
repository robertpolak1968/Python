#!/usr/bin/python
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

#Port lokalnego komputera, do kt�rego ma zosta� d��czony serwer.
#Serwer dost�pny jest przy u�yciu adresu URL "http://localhost:8000/".
PORT = 8000

class VisibleHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Klasa ta zachowuje si� podobnie do SimpleHTTPRequestHandler, ale zamiast
    wy�wietla� na standardowym wyj�ciu jedynie podsumowanie ��dania, wy�wietla
    pe�n� tre�� ��dania i odpowiedzi HTTP."""

    def log_request(self, code='-', size='-'):
        """Wy�wietla szczeg�y ��dania. Metoda jest wywo�ywana przez
        SimpleHTTPRequestHandler.do_GET()."""
        print self._heading("��danie HTTP")
        #Najpierw wy�wietl ientyfikator zasobu i operacj�.
        print self.raw_requestline,
        #Nast�pnie wy�wietl pozosta�e dane.
        for header, value in self.headers.items():            
            print header + ":", value

    def do_GET(self, method='GET'):
        """Obs�uguje ��danie GET w ten sam spos�b, co
        SimpleHTTPRequestHandler, ale wy�wietla r�wnie� tre�� odpowiedzi
        na standardowym wyj�ciu."""

        #Zast�puje obiekt s�u��cy do wysy�ania odpowiedzi jego zmodyfikowan�
        #wersj�, kt�ra kopiuje wszystkie wysy�ane dane w miejsc, kt�re 
        #mo�emy sprawdzi�. Nast�pnie przekazuje rzeczywist� obs�ug� odpowiedzi
        #SimpleHTTPRequestHandler.
        self.wfile = FileWrapper(self.wfile)
        SimpleHTTPRequestHandler.do_GET(self)

        #Obiekt tymczasowy zawiera wszystkie wys�ane dane odpowiedzi.
        #Jest gotowy do ich wy�wietlenia. ��danie r�wnie� zosta�o wy�wietlone
        #dzi�ki modyfikacji metody log_request()
        #(wywo�anej przez metod� do_GET z SimpleHTTPRequestHandler).
        print ""
        print self._heading("Odpowied� HTTP")
        print self.wfile

    def _heading(self, s):
        """Ta metoda pomocnicza formatuje odpowiednio tekst nad nag��wkami
        ��dania i odpowiedzi."""    
        line = '=' * len(s)
        return line + '\n' + s + '\n' + line

class FileWrapper:
    """Klasa otacza podstawow� klas� pliku, by wszystko zapisywane do pliku by�o
    r�wnie� po cichu zapami�tywane w buforze w celu p�niejszego wykorzystania.
    """

    def __init__(self, wfile):
        """wfile to obiekt pliku, do kt�rego zapisywana jest odpowied�.
        Zast�pujemy go, by zapewni� zapamietywanie dodatkowych informacji."""
        self.wfile = wfile
        self.contents = []

    def __getattr__(self, key):
        """Je�li komu� nie uda�o si� uzyska� atrybutu tego obiektu, zapewne
        mia� zamiar pobra� go dla oryginalnego obiektu pliku.
        Delegujemy wi�c wywo�anie do oryginalnej wersji."""
        return getattr(self.wfile, key)

    def write(self, s):
        """Zapisuje dane do 'rzeczywistego' pliku a tak�e do specjalnego bufora
        w celu ich wy�wietlenia w dalszej cz�ci programu."""
        self.contents.append(s)
        self.wfile.write(s)

    def __str__(self):
        """Zwraca zebrane do tej pory dane jako tekst."""
        return ''.join(self.contents)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', PORT), VisibleHTTPRequestHandler)
    httpd.serve_forever()
