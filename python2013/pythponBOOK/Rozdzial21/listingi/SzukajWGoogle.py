import SOAPpy

class GoogleAPI:

    "Implementuje czêœæ Google Web API jako prost¹ klasê Pythona."

    URL = 'http://api.google.com/search/beta2'
    NAMESPACE = 'urn:GoogleSearch'

    def __init__(self):
        self.server = SOAPpy.SOAPProxy(self.URL, self.NAMESPACE)
        #Te dwa polecenia z SOAPpy powoduj¹ wyœwietlanie pe³nego
        #¿¹dania i odpowiedzi dla ka¿dego wywo³ania SOAP, co pozwala
        #poznaæ szczegó³y dzia³ania protoko³u.
        #self.server.config.dumpSOAPOut=1
        #self.server.config.dumpSOAPIn=1
    
    def doGoogleSearch(self, key, searchString, resultOffset=0, maxResults=10,
                       filter=True, restrict="", safeSearch=True,
                       languageRestrict="pl"):
        """Metoda pomocnicza, która pozwala ukryæ fakt, i¿ wywo³anie
        doGoogleSearch wymaga 10 argumantów, z których 2 s¹ przestarza³e
        i nie powinny byæ stosowane. Wywo³uj¹c tê metodê, mo¿na wykonaæ 
        wyszukiwanie, podaj¹c jedynie klczu Google API i poszukiwany tekst
        Znaczenie pozosta³ych argumentów jest szczegó³owo opisane w 
        dokumentacji Google Web API."""
        return self.server.doGoogleSearch(key, searchString, resultOffset,
                                          maxResults, filter, restrict,
                                          safeSearch, languageRestrict, "", "")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print "U¿ycie: %s [klucz Google] [szukana fraza]" % sys.argv[0]
        sys.exit(1)
    key, term = sys.argv[1:3]
    resultObj = GoogleAPI().doGoogleSearch(key, term)
    results = resultObj.resultElements
    print 'Pierwszych %s wyników dla "%s":' % (len(results), term)
    for result in results:
        print " %s: %s" % (result.title, result.URL)
