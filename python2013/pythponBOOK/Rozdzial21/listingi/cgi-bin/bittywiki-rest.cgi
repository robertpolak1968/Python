#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import re
from BittyWiki import Wiki, Page, NotWikiWord

class WikiRestApiCGI:

    #Mo¿liwe operacje zwi±zane ze stron± wiki.
    VIEW = ''
    WRITE = 'zapisz'
    DELETE = 'usun'

    #Mo¿liwe kody odpowiedzi zwracane przez us³ugê.
    RESPONSE_CODES = { 200 : 'OK',
                       400 : 'Bad Request',
                       404 : 'Not Found'}
    
    def __init__(self, wikiBase):
        "Inicjalizacja konkretn± wiki."
        self.wiki = Wiki(wikiBase)

    def run(self):
        """Sprawd¼ polecenie, przeka¿ je do odpowiedniego modu³u i
        wy¶wietl wyniki jako dokument XML."""
        toDisplay = None
        try:
            page = os.environ.get('PATH_INFO', '')
            if page:
                page = page[1:]
            page = self.wiki.getPage(page)
        except NotWikiWord, badName:
            toDisplay = 400, '"%s" nie jest poprawn± nazw± wiki.' % badName

        if not toDisplay:
            form = cgi.FieldStorage()
            operation = form.getfirst('operacja', self.VIEW)
            operationMethod = self.OPERATION_METHODS.get(operation)
            if operationMethod:
                if not page.exists() and operation != self.WRITE:
                    toDisplay = 404, 'Nie ma strony: "%s"' % page.name
                else:
                    toDisplay = operationMethod(self, page, form)
            else:
                toDisplay = 400, '"%s" nie jest poprawn± operacj±.' % operation
                
        #Wy¶wietl odpowied¼.
        responseCode, payload = toDisplay
        print 'Status: %s %s' % (responseCode,
                                 self.RESPONSE_CODES.get(responseCode))
        print 'Content-type: text/plain\n'
        print payload

    def viewOperation(self, page, form=None):
        "Zwraca surowy tekst strony wiki."
        return 200, page.getText()
    
    def writeOperation(self, page, form):
        "Zapisuje stronê wiki."
        page.text = form.getfirst('dane')
        page.save()
        return 200, "Strona zapisana."
    
    def deleteOperation(self, page, format, form=None):
        "Usuwa wskazana stronê."
        if not page.exists():
            toDisplay = 404, "Nie mo¿na usun±æ nieistniej±cej strony."
        else:
            page.delete()
            toDisplay = 200, "Strona usuniêta."
        return toDisplay

    #Odwzorowanie operacji na odpowiadaj±ce im metody.
    OPERATION_METHODS = { VIEW : viewOperation,
                          WRITE: writeOperation,
                          DELETE: deleteOperation }

if __name__ == '__main__':
    WikiRestApiCGI('lokalnewiki').run()
