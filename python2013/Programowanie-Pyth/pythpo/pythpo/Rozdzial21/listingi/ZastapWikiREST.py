#!/usr/bin/python
import re
import urllib

class WikiReplaceSpider:
    "Klasa wykonuj±ca operacjê znajd¼ i wyszukaj dla stron wiki."

    WIKI_WORD = re.compile('(([A-Z][a-z0-9]*){2,})')

    def __init__(self, restURL):
        "Adres URL dla interfejsu BittyWiki REST API."
        self.api = BittyWikiRestAPI(restURL)

    def replace(self, find, replace):
        """Zaczyna przechodzenie przez strony wiki od strony g³ównej, pobieraj±c
        je i modyfikuj±c za pomoc± odpowiedniego API."""

        processed = {} #Zapamiêtuj ju¿ przeanalizowane strony.
        todo = ['StronaGlowna'] #Zacznij od strony g³ównej.
        while todo:
            for pageName in todo:
                print 'Sprawdzam "%s"' % pageName
                try:
                    pageText = self.api.getPage(pageName)
                except RemoteApplicationException, message:
                    if str(message).find("Nie ma strony") == 0:
                        #Znaleziono S³owoWiki, które nie ma jeszcze swojej strony.
                        #Nie stanowi ono ¿adnego problemu.
                        pass
                    else:
                        #Inny problem, zg³o¶ wyj±tek.
                        raise RemoteApplicationException, message
                else:
                    #Strona istnieje, wiec j± przetwórz.
                    #Najpierw znajd¼ S³owaWiki na stronie. Mog± one zawieraæ
                    #referencje do innych stron.
                    for wikiWord in self.WIKI_WORD.findall(pageText):
                        linkPage = wikiWord[0]
                        if not processed.get(linkPage) and linkPage not in todo:
                            #Ta strona nie zozsta³a jeszcze przetworzona.
                            #Umie¶æ j± na odpowiedniej li¶cie.
                            todo.append(linkPage)

                    #Uruchom wyszukiwanie i zastêpowanie dla strony, by uzyskaæ
                    #jej now± tre¶æ.
                    newText = pageText.replace(find, replace)

                    #Sprawd¼, czy nazwa strony odpowiada wzorcowi zastêpowania.
                    #Je¶li tak, usuñ j± i utwórz now± z nowym tekstem.
                    #W przeciwnym razie jedynie zmodyfikuj tekst.
                    newPageName = pageName.replace(find, replace)
                    if newPageName != pageName:
                        print ' Usuwam "%s", utworzê "%s"' \
                              % (pageName, newPageName)
                        self.api.delete(pageName)
                    if newPageName != pageName or newText != pageText:
                        print ' Zapisujê "%s"' % newPageName
                        self.api.save(newPageName, newText)
                    #Oznacz now± stronê jako przetworzon±, by nie analizowaæ
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
        "Zwróæ surow± tre¶æ strony o wskazanym znaczniku."
        return self._doGet(pageName)

    def save(self, pageName, data):
        "Zapisz stronê o tre¶ci data pod wskazanym adresem."
        return self._doPost(pageName, { 'operacja' : 'zapisz',
                                        'dane' : data })

    def delete(self, pageName):
        "Usuñ stronê wiki o podanej nazwie."
        return self._doPost(pageName, { 'operacja' : 'usun' })

    def _doGet(self, pageName):
        """"Ogólne wywo³anie HTTP GET. Pobierz odpowied¿ lub zg³o¶
        wyj±tek, je¶li kod odpowiedzi nie jest poprawny."""
        url = self._makeURL(pageName)
        return self.Response(urllib.urlopen(url)).body

    def _doPost(self, pageName, data):
        """Ogólne wywo³anie HTTP POST. Pobierz odpowied¿ lub zg³o¶
        wyj±tek, je¶li kod odpowiedzi nie jest poprawny."""
        url = self._makeURL(pageName)
        return self.Response(urllib.urlopen(url, urllib.urlencode(data))).body
    
    def _makeURL(self, pageName):
        "Zwraca adres URL strony wiki o wskazanej nazwie."
        url = self.base
        if url[-1] != '/':
            url += '/'
        return url + pageName

    class Response:
        """Klasa obs³uguje odpowied¼ HTTP zwracn± przez us³ugê
        internetow± REST."""

        def __init__(self, inHandle):
            self.body = None
            statusCode = None

            info = inHandle.info()
            #Status zosta³ automatycznie wczytany do obiektu
            #zawieraj±cego wszystkie nag³ówki HTTP. Tekst statusu
            #wygl±da nastêpuj±co: '200 OK'.
            statusHeader = info['status']
            statusCode = int(statusHeader.split(' ')[0])

            #Pozosta³e dane to odpowied¼ w postaci tekstowej. W bardziej
            #z³o¿onej aplikacji by³yby to zapewne dane XML i musia³yby
            #zostaæ przeanalizowane.
            self.body = inHandle.read()

            #Jedynie kody odpowiedzi w zakresie 2xx s± poprawne.
            #Wszystkie inne kody spowoduj± zg³oszenie wyj±tku.
            if statusCode / 100 != 2:
                raise RemoteApplicationException, self.body

class RemoteApplicationException(Exception):
    """Prosta klasa wyj±tku u¿ywana przez REST API do poinformowania
    o b³êdzie."""
    pass 

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        restURL, find, replace = sys.argv[1:]
    else:
        print 'U¿ycie: %s [adres URL BittyWiki REST API] [znajd¼] [zast±p]' \
              % sys.argv[0]
        sys.exit(1)
    WikiReplaceSpider(restURL).replace(find, replace)
