#!/usr/bin/python
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

#Port lokalnego komputera, do którego ma zostaæ d³±czony serwer.
#Serwer dostêpny jest przy u¿yciu adresu URL "http://localhost:8000/".
PORT = 8000

class VisibleHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Klasa ta zachowuje siê podobnie do SimpleHTTPRequestHandler, ale zamiast
    wy¶wietlaæ na standardowym wyj¶ciu jedynie podsumowanie ¿±dania, wy¶wietla
    pe³n± tre¶æ ¿±dania i odpowiedzi HTTP."""

    def log_request(self, code='-', size='-'):
        """Wy¶wietla szczegó³y ¿±dania. Metoda jest wywo³ywana przez
        SimpleHTTPRequestHandler.do_GET()."""
        print self._heading("¯±danie HTTP")
        #Najpierw wy¶wietl ientyfikator zasobu i operacjê.
        print self.raw_requestline,
        #Nastêpnie wy¶wietl pozosta³e dane.
        for header, value in self.headers.items():            
            print header + ":", value

    def do_GET(self, method='GET'):
        """Obs³uguje ¿±danie GET w ten sam sposób, co
        SimpleHTTPRequestHandler, ale wy¶wietla równie¿ tre¶æ odpowiedzi
        na standardowym wyj¶ciu."""

        #Zastêpuje obiekt s³u¿±cy do wysy³ania odpowiedzi jego zmodyfikowan±
        #wersj±, która kopiuje wszystkie wysy³ane dane w miejsc, które 
        #mo¿emy sprawdziæ. Nastêpnie przekazuje rzeczywist± obs³ugê odpowiedzi
        #SimpleHTTPRequestHandler.
        self.wfile = FileWrapper(self.wfile)
        SimpleHTTPRequestHandler.do_GET(self)

        #Obiekt tymczasowy zawiera wszystkie wys³ane dane odpowiedzi.
        #Jest gotowy do ich wy¶wietlenia. ¯±danie równie¿ zosta³o wy¶wietlone
        #dziêki modyfikacji metody log_request()
        #(wywo³anej przez metodê do_GET z SimpleHTTPRequestHandler).
        print ""
        print self._heading("Odpowied¼ HTTP")
        print self.wfile

    def _heading(self, s):
        """Ta metoda pomocnicza formatuje odpowiednio tekst nad nag³ówkami
        ¿±dania i odpowiedzi."""    
        line = '=' * len(s)
        return line + '\n' + s + '\n' + line

class FileWrapper:
    """Klasa otacza podstawow± klasê pliku, by wszystko zapisywane do pliku by³o
    równie¿ po cichu zapamiêtywane w buforze w celu pó¼niejszego wykorzystania.
    """

    def __init__(self, wfile):
        """wfile to obiekt pliku, do którego zapisywana jest odpowied¼.
        Zastêpujemy go, by zapewniæ zapamietywanie dodatkowych informacji."""
        self.wfile = wfile
        self.contents = []

    def __getattr__(self, key):
        """Je¶li komu¶ nie uda³o siê uzyskaæ atrybutu tego obiektu, zapewne
        mia³ zamiar pobraæ go dla oryginalnego obiektu pliku.
        Delegujemy wiêc wywo³anie do oryginalnej wersji."""
        return getattr(self.wfile, key)

    def write(self, s):
        """Zapisuje dane do 'rzeczywistego' pliku a tak¿e do specjalnego bufora
        w celu ich wy¶wietlenia w dalszej czê¶ci programu."""
        self.contents.append(s)
        self.wfile.write(s)

    def __str__(self):
        """Zwraca zebrane do tej pory dane jako tekst."""
        return ''.join(self.contents)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', PORT), VisibleHTTPRequestHandler)
    httpd.serve_forever()
