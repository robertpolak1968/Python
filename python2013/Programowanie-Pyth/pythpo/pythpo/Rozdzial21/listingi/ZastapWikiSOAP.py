#!/usr/bin/python
import re
import SOAPpy

class WikiReplaceSpider:
    "Klasa wykonuj�ca operacj� znajd� i wyszukaj dla stron wiki."

    WIKI_WORD = re.compile('(([A-Z][a-z0-9]*){2,})')

    def __init__(self, rpcURL):
        "Adres URL dla interfejsu BittyWiki SOAP API."
        self.api = SOAPpy.SOAPProxy(rpcURL, "urn:BittyWiki")
        self.api.config.dumpSOAPIn=1

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
                except SOAPpy.Types.faultType, fault:
                    if fault.detail.find("NoSuchPage") != -1:
                        #Znaleziono S�owoWiki, kt�re nie ma jeszcze swojej strony.
                        #Nie stanowi ono �adnego problemu.
                        pass
                    else:
                        #Inny problem, zg�o� wyj�tek.
                        raise SOAPpy.Types.faultType, fault
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

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        rpcURL, find, replace = sys.argv[1:]
    else:
        print 'U�ycie: %s [adres URL BittyWiki SOAP API] [znajd�] [zast�p]' \
              % sys.argv[0]
        sys.exit(1)
    WikiReplaceSpider(rpcURL).replace(find, replace)
