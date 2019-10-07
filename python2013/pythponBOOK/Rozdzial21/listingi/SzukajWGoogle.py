import SOAPpy

class GoogleAPI:

    "Implementuje cz�� Google Web API jako prost� klas� Pythona."

    URL = 'http://api.google.com/search/beta2'
    NAMESPACE = 'urn:GoogleSearch'

    def __init__(self):
        self.server = SOAPpy.SOAPProxy(self.URL, self.NAMESPACE)
        #Te dwa polecenia z SOAPpy powoduj� wy�wietlanie pe�nego
        #��dania i odpowiedzi dla ka�dego wywo�ania SOAP, co pozwala
        #pozna� szczeg�y dzia�ania protoko�u.
        #self.server.config.dumpSOAPOut=1
        #self.server.config.dumpSOAPIn=1
    
    def doGoogleSearch(self, key, searchString, resultOffset=0, maxResults=10,
                       filter=True, restrict="", safeSearch=True,
                       languageRestrict="pl"):
        """Metoda pomocnicza, kt�ra pozwala ukry� fakt, i� wywo�anie
        doGoogleSearch wymaga 10 argumant�w, z kt�rych 2 s� przestarza�e
        i nie powinny by� stosowane. Wywo�uj�c t� metod�, mo�na wykona� 
        wyszukiwanie, podaj�c jedynie klczu Google API i poszukiwany tekst
        Znaczenie pozosta�ych argument�w jest szczeg�owo opisane w 
        dokumentacji Google Web API."""
        return self.server.doGoogleSearch(key, searchString, resultOffset,
                                          maxResults, filter, restrict,
                                          safeSearch, languageRestrict, "", "")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print "U�ycie: %s [klucz Google] [szukana fraza]" % sys.argv[0]
        sys.exit(1)
    key, term = sys.argv[1:3]
    resultObj = GoogleAPI().doGoogleSearch(key, term)
    results = resultObj.resultElements
    print 'Pierwszych %s wynik�w dla "%s":' % (len(results), term)
    for result in results:
        print " %s: %s" % (result.title, result.URL)
