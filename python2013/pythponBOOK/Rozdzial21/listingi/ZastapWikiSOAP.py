#!/usr/bin/python
import re
import SOAPpy

class WikiReplaceSpider:
    "Klasa wykonuj±ca operacjê znajd¼ i wyszukaj dla stron wiki."

    WIKI_WORD = re.compile('(([A-Z][a-z0-9]*){2,})')

    def __init__(self, rpcURL):
        "Adres URL dla interfejsu BittyWiki SOAP API."
        self.api = SOAPpy.SOAPProxy(rpcURL, "urn:BittyWiki")
        self.api.config.dumpSOAPIn=1

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
                except SOAPpy.Types.faultType, fault:
                    if fault.detail.find("NoSuchPage") != -1:
                        #Znaleziono S³owoWiki, które nie ma jeszcze swojej strony.
                        #Nie stanowi ono ¿adnego problemu.
                        pass
                    else:
                        #Inny problem, zg³o¶ wyj±tek.
                        raise SOAPpy.Types.faultType, fault
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

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        rpcURL, find, replace = sys.argv[1:]
    else:
        print 'U¿ycie: %s [adres URL BittyWiki SOAP API] [znajd¼] [zast±p]' \
              % sys.argv[0]
        sys.exit(1)
    WikiReplaceSpider(rpcURL).replace(find, replace)
