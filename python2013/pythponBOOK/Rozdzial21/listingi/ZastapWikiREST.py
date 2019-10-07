#!/usr/bin/python
import re
import urllib

class WikiReplaceSpider:
    "Klasa wykonuj�ca operacj� znajd� i wyszukaj dla stron wiki."

    WIKI_WORD = re.compile('(([A-Z][a-z0-9]*){2,})')

    def __init__(self, restURL):
        "Adres URL dla interfejsu BittyWiki REST API."
        self.api = BittyWikiRestAPI(restURL)

    def replace(self, find, replace):
        """Zaczyna przechodzenie przez strony wiki od strony g��wnej, pobieraj�c
        je i modyfikuj�c za pomoc� odpowiedniego API."""

        processed = {} #Zapami�tuj ju� przeanalizowane strony.
        todo = ['StronaGlowna'] #Zacznij od strony g��wnej.
        while todo:
            for pageName in todo:
                print 'Sprawdzam "%s"' % pageName
                try:
                    pageText = self.api.getPage(pageName)
                except RemoteApplicationException, message:
                    if str(message).find("Nie ma strony") == 0:
                        #Znaleziono S�owoWiki, kt�re nie ma jeszcze swojej strony.
                        #Nie stanowi ono �adnego problemu.
                        pass
                    else:
                        #Inny problem, zg�o� wyj�tek.
                        raise RemoteApplicationException, message
                else:
                    #Strona istnieje, wiec j� przetw�rz.
                    #Najpierw znajd� S�owaWiki na stronie. Mog� one zawiera�
                    #referencje do innych stron.
                    for wikiWord in self.WIKI_WORD.findall(pageText):
                        linkPage = wikiWord[0]
                        if not processed.get(linkPage) and linkPage not in todo:
                            #Ta strona nie zozsta�a jeszcze przetworzona.
                            #Umie�� j� na odpowiedniej li�cie.
                            todo.append(linkPage)

                    #Uruchom wyszukiwanie i zast�powanie dla strony, by uzyska�
                    #jej now� tre��.
                    newText = pageText.replace(find, replace)

                    #Sprawd�, czy nazwa strony odpowiada wzorcowi zast�powania.
                    #Je�li tak, usu� j� i utw�rz now� z nowym tekstem.
                    #W przeciwnym razie jedynie zmodyfikuj tekst.
                    newPageName = pageName.replace(find, replace)
                    if newPageName != pageName:
                        print ' Usuwam "%s", utworz� "%s"' \
                              % (pageName, newPageName)
                        self.api.delete(pageName)
                    if newPageName != pageName or newText != pageText:
                        print ' Zapisuj� "%s"' % newPageName
                        self.api.save(newPageName, newText)
                    #Oznacz now� stron� jako przetworzon�, by nie analizowa�
                    #jej po raz drugi.
                    if newPageName != pageName:
                        processed[newPageName] = True
                processed[pageName] = True
                todo.remove(pageName)

class BittyWikiRestAPI:

    "Interfejs Pythona dla BittyWiki REST API."

    def __init__(self, restURL):
        "Zacznij od adresu bazowego URL interfejsu REST."
        self.base = restURL

    def getPage(self, pageName):
        "Zwr�� surow� tre�� strony o wskazanym znaczniku."
        return self._doGet(pageName)

    def save(self, pageName, data):
        "Zapisz stron� o tre�ci data pod wskazanym adresem."
        return self._doPost(pageName, { 'operacja' : 'zapisz',
                                        'dane' : data })

    def delete(self, pageName):
        "Usu� stron� wiki o podanej nazwie."
        return self._doPost(pageName, { 'operacja' : 'usun' })

    def _doGet(self, pageName):
        """"Og�lne wywo�anie HTTP GET. Pobierz odpowied� lub zg�o�
        wyj�tek, je�li kod odpowiedzi nie jest poprawny."""
        url = self._makeURL(pageName)
        return self.Response(urllib.urlopen(url)).body

    def _doPost(self, pageName, data):
        """Og�lne wywo�anie HTTP POST. Pobierz odpowied� lub zg�o�
        wyj�tek, je�li kod odpowiedzi nie jest poprawny."""
        url = self._makeURL(pageName)
        return self.Response(urllib.urlopen(url, urllib.urlencode(data))).body
    
    def _makeURL(self, pageName):
        "Zwraca adres URL strony wiki o wskazanej nazwie."
        url = self.base
        if url[-1] != '/':
            url += '/'
        return url + pageName

    class Response:
        """Klasa obs�uguje odpowied� HTTP zwracn� przez us�ug�
        internetow� REST."""

        def __init__(self, inHandle):
            self.body = None
            statusCode = None

            info = inHandle.info()
            #Status zosta� automatycznie wczytany do obiektu
            #zawieraj�cego wszystkie nag��wki HTTP. Tekst statusu
            #wygl�da nast�puj�co: '200 OK'.
            statusHeader = info['status']
            statusCode = int(statusHeader.split(' ')[0])

            #Pozosta�e dane to odpowied� w postaci tekstowej. W bardziej
            #z�o�onej aplikacji by�yby to zapewne dane XML i musia�yby
            #zosta� przeanalizowane.
            self.body = inHandle.read()

            #Jedynie kody odpowiedzi w zakresie 2xx s� poprawne.
            #Wszystkie inne kody spowoduj� zg�oszenie wyj�tku.
            if statusCode / 100 != 2:
                raise RemoteApplicationException, self.body

class RemoteApplicationException(Exception):
    """Prosta klasa wyj�tku u�ywana przez REST API do poinformowania
    o b��dzie."""
    pass 

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        restURL, find, replace = sys.argv[1:]
    else:
        print 'U�ycie: %s [adres URL BittyWiki REST API] [znajd�] [zast�p]' \
              % sys.argv[0]
        sys.exit(1)
    WikiReplaceSpider(restURL).replace(find, replace)
