#!/usr/bin/python
import sys
import SimpleXMLRPCServer
from BittyWiki import Wiki

class BittyWikiAPI:
    """Prosta klasa otoczkowa zapewniaj�ca udost�pnienie funkcjonalno�ci
    BittyWiki jako prosty interfejs API."""

    def __init__(self, wikiBase):
        "Inicjalizacja wiki znajduj�cego si� w podanym folderze."
        self.wiki = Wiki(wikiBase)

    def getPage(self, pageName):
        "Zwraca tekst wskazanej strony."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, page.name
        return page.getText()

    def save(self, pageName, newText):
        "Zapisuje stron� w wiki."
        page = self.wiki.getPage(pageName)
        page.text = newText
        page.save()
        return "Strona zapisana."

    def delete(self, pageName):
        "Usuwa stron� wiki."
        page = self.wiki.getPage(pageName)
        if not page.exists():
            raise NoSuchPage, pageName
        page.delete()
        return "Strona usuni�ta."                    

class NoSuchPage(Exception):
    pass

def handlerSetup(handler, api):
    """Funkcja rejestruje metody interfejsu BittyWiki API
    jako funkcje procedury obs�ugi XML-RPC."""

    #Zarejestruj standardowe funkcje u�ywane przez XML-RPC, aby poinformowa�,
    #kt�re funkcje b�d� dost�pne na serwerze.
    handler.register_introspection_functions()

    #Zarejestruj metody BittyWiki API jako funkcje XML-RPC w przestrzeni
    #nazw 'bittywiki'.
    handler.register_function(api.getPage, 'bittywiki.getPage')
    handler.register_function(api.save, 'bittywiki.save')
    handler.register_function(api.delete, 'bittywiki.delete')

    #Oto przyk�ad rejestracji wszystkich trzech metod w jednym wierszu
    #kodu dzi�ki zastosowaniu ca�ego obiektu. Rozwi�zanie jest zakomentowane,
    #poniewa� w starszych wersjach Pythona zawiera�o luk� w zabezpieczeniach
    #(dotyczy wersji 2.2, 2.3.4 i 2.4.0). Szczeg��w szukaj na stronie
    #http://www.python.org/security/PSF-2005-001/.
    #
    #handler.register_instance(api)
    #
    #Nale�y pami�ta�, �e w tym rozwi�zaniu zrejestracj�, funkcje XML-RPC
    #nie b�d� mia�y przedrostka 'bittywiki.': pojawi� si� nazwy typy
    #"getPage" zamiast "bittywiki.getPage". Aby tego unikn��, mo�na 
    #pos�u�y� si� nast�puj�c� sztuczk�:
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
        #U�ytkownik przekaza� numer portu; oznacza to ch�� utworzenia
        #niezale�nego serwera.
        standalonePort = sys.argv[1]
        try:
            standalonePort = int(standalonePort)
        except ValueError:
            #To jednak nie by� numer portu. Poinformuj u�ytkownika o poprawnej sk�adni.
            scriptName = sys.argv[0]
            print 'U�ycie:'
            print ' "%s [numer portu]" uruchamia niezale�ny serwer.' \
                  % scriptName
            print ' "%s" w celu wywo�ania jako CGI.' % scriptName
            sys.exit(1)
        isStandalone = 1
        print "Uruchamiam niezale�ny serwer XML-RPC na porcie %s." \
              % standalonePort
        handler = SimpleXMLRPCServer.SimpleXMLRPCServer\
                  (('localhost', standalonePort))
    else:
        #Nie podano numeru portu, wi�c wywo�anie CGI.
        handler = SimpleXMLRPCServer.CGIXMLRPCRequestHandler()

    #Krok rejestracji funkcji jest taki sam dla
    #SimpleXMLRPCServer i CGIXMLRPCRequestHandler.
    handlerSetup(handler, api)

    if standalonePort:
        handler.serve_forever()
    else:
        handler.handle_request()
