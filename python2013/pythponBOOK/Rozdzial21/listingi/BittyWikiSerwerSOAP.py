#!/usr/bin/python
import sys
import SOAPpy
from BittyWiki import Wiki

class BittyWikiAPI:
    """Prosta klasa otoczkowa zapewniająca udostępnienie funkcjonalności
    BittyWiki jako prosty interfejs API."""

    def __init__(self, wikiBase):
        "Inicjalizacja wiki znajdującego się w podanym folderze."
        self.wiki = Wiki(wikiBase)

    def getPage(self, pageName):
        "Zwraca tekst wskazanej strony."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, page.name
        return page.getText()

    def save(self, pageName, newText):
        "Zapisuje stronę w wiki."
        page = self.wiki.getPage(pageName)
        page.text = newText
        page.save()
        return "Strona zapisana."

    def delete(self, pageName):
        "Usuwa stronę wiki."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, page.name
        page.delete()
        return "Strona usunięta."

class NoSuchPage(Exception):
    """Wyjątek zgłaszany w momencie próby pobrania strony, która nie istnieje."""
    pass

DEFAULT_PORT = 8002
NAMESPACE = 'urn:BittyWiki'

if __name__ == '__main__':
    WIKI_BASE = 'wiki/'
    api = BittyWikiAPI(WIKI_BASE)
    port = DEFAULT_PORT    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        try:
            port = int(port)
        except ValueError:
            #Nie podano poprawnego numeru portu. Poinformuj użytkownika o składni wywołania.
            print 'Użycie: "%s [numer portu]"' % sys.argv[0]
            sys.exit(1)
    print "Uruchamiam niezależny serwer SOAP na porcie %s." % port
    handler = SOAPpy.SOAPServer(('localhost', port))
    handler.registerObject(api, NAMESPACE)
    handler.serve_forever()
