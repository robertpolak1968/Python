#!/usr/bin/python
import sys
import SimpleXMLRPCServer
from BittyWiki import Wiki

class BittyWikiAPI:
    """Prosta klasa otoczkowa zapewniaj±ca udostêpnienie funkcjonalno¶ci
    BittyWiki jako prosty interfejs API."""

    def __init__(self, wikiBase):
        "Inicjalizacja wiki znajduj±cego siê w podanym folderze."
        self.wiki = Wiki(wikiBase)

    def getPage(self, pageName):
        "Zwraca tekst wskazanej strony."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, page.name
        return page.getText()

    def save(self, pageName, newText):
        "Zapisuje stronê w wiki."
        page = self.wiki.getPage(pageName)
        page.text = newText
        page.save()
        return "Strona zapisana."

    def delete(self, pageName):
        "Usuwa stronê wiki."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, pageName
        page.delete()
        return "Strona usuniêta."                    

class NoSuchPage(Exception):
    pass

def handlerSetup(handler, api):
    """Funkcja rejestruje metody interfejsu BittyWiki API
    jako funkcje procedury obs³ugi XML-RPC."""

    #Zarejestruj standardowe funkcje u¿ywane przez XML-RPC, aby poinformowaæ,
    #które funkcje bêd± dostêpne na serwerze.
    handler.register_introspection_functions()

    #Zarejestruj metody BittyWiki API jako funkcje XML-RPC w przestrzeni
    #nazw 'bittywiki'.
    handler.register_function(api.getPage, 'bittywiki.getPage')
    handler.register_function(api.save, 'bittywiki.save')
    handler.register_function(api.delete, 'bittywiki.delete')

    #Oto przyk³ad rejestracji wszystkich trzech metod w jednym wierszu
    #kodu dziêki zastosowaniu ca³ego obiektu. Rozwi±zanie jest zakomentowane,
    #poniewa¿ w starszych wersjach Pythona zawiera³o lukê w zabezpieczeniach
    #(dotyczy wersji 2.2, 2.3.4 i 2.4.0). Szczegó³ów szukaj na stronie
    #http://www.python.org/security/PSF-2005-001/.
    #
    #handler.register_instance(api)
    #
    #Nale¿y pamiêtaæ, ¿e w tym rozwi±zaniu zrejestracj±, funkcje XML-RPC
    #nie bêd± mia³y przedrostka 'bittywiki.': pojawi± siê nazwy typy
    #"getPage" zamiast "bittywiki.getPage". Aby tego unikn±æ, mo¿na 
    #pos³u¿yæ siê nastêpuj±c± sztuczk±:
    #class Container:
    #    pass
    #container = Container()
    #container.bittywiki = api
    #handler.register_instance(container)


if __name__ == '__main__':
    WIKI_BASE = 'wiki/'
    api = BittyWikiAPI(WIKI_BASE)
    standalonePort = None
    if len(sys.argv) > 1:
        #U¿ytkownik przekaza³ numer portu; oznacza to chêæ utworzenia
        #niezale¿nego serwera.
        standalonePort = sys.argv[1]
        try:
            standalonePort = int(standalonePort)
        except ValueError:
            #To jednak nie by³ numer portu. Poinformuj u¿ytkownika o poprawnej sk³adni.
            scriptName = sys.argv[0]
            print 'U¿ycie:'
            print ' "%s [numer portu]" uruchamia niezale¿ny serwer.' \
                  % scriptName
            print ' "%s" w celu wywo³ania jako CGI.' % scriptName
            sys.exit(1)
        isStandalone = 1
        print "Uruchamiam niezale¿ny serwer XML-RPC na porcie %s." \
              % standalonePort
        handler = SimpleXMLRPCServer.SimpleXMLRPCServer\
                  (('localhost', standalonePort))
    else:
        #Nie podano numeru portu, wiêc wywo³anie CGI.
        handler = SimpleXMLRPCServer.CGIXMLRPCRequestHandler()

    #Krok rejestracji funkcji jest taki sam dla
    #SimpleXMLRPCServer i CGIXMLRPCRequestHandler.
    handlerSetup(handler, api)

    if standalonePort:
        handler.serve_forever()
    else:
        handler.handle_request()
