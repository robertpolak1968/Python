#!/usr/bin/python
import cgi
import cgitb
import os
import re
from BittyWiki import Wiki, Page, NotWikiWord
cgitb.enable()

#Najpierw kilka szablonów HTML.
MAIN_TEMPLATE = '''<html>
<head><title>%(title)s</title>
<body>%(body)s<hr />%(navLinks)s</body>
</html>'''

VIEW_TEMPLATE = '''%(banner)s
<h1>%(name)s</h1> 
%(processedText)s'''

WRITE_TEMPLATE = '''%(banner)s
<h1>%(title)s</h1>
<form method="POST" action="%(pageURL)s">
 <input type="hidden" name="operacja" value="zapisz">
 <textarea rows="15" cols="80" name="dane">%(text)s</textarea><br />
 <input type="submit" value="Zapisz">
</form>'''

DELETE_TEMPLATE = '''<h1>%(title)s</h1>
<p>Czy jeste¶ pewien, ¿e chcesz usun±æ stronê %(name)s?</p>

<form method="POST" action="%(pageURL)s">
 <input type="hidden" name="operacja" value="usun">
 <input type="submit" value="Usuñ %(name)s!">
</form>'''

ERROR_TEMPLATE = '<h1>B³±d: %(error)s</h1>'
BANNER_TEMPLATE = '<p style="color:red;">%s</p><hr />'

#Fragment ³±cz±cy S³owoWiki z odpowiedni± stron± wiki.
VIEW_LINK = '<a href="%s">%%(wikiword)s</a>'

#Fragment ³±cz±cy S³owoWiki, dla którego nie istnieje odpowiednia strona
#wiki o podanej nazwie.
ADD_LINK = '%%(wikiword)s<a href="%s">?</a>'

class WikiCGI:

    #Mo¿liwe operacje zwi±zane ze stron± wiki.
    VIEW = ''
    WRITE = 'zapisz'
    DELETE = 'usun'

    def __init__(self, wikiRoot):
        self.wiki = Wiki(wikiRoot)

    def run(self):
        toDisplay = None
        try:
            #Pobierz stronê ¿±dan± przez u¿ytkownika.
            page = os.environ.get('PATH_INFO', '')
            if page:
                page = page[1:]
            page = self.wiki.getPage(page)
        except NotWikiWord, badName:
            page = None
            error = '"%s" nie jest poprawn± nazw± wiki.' % badName
            toDisplay = self.makeError(error)

        if page:
            #Okre¶l, co u¿ytkownik chce zrobiæ z ¿±dan± stron±.
            makeChange = os.environ['REQUEST_METHOD'] == 'POST'
            if makeChange:
                defaultOperation = self.WRITE
            else:
                defaultOperation = ''
            form = cgi.FieldStorage()
            operation = form.getfirst('operacja', defaultOperation)

            #Wiemy, do którego zasobu ¿ytkownik ¿±da dostêpu
            #("page" w po³±czeniu z "operation"). Element "form"
            #zawiera efektulan± reprezentacjê uzyskan± od u¿ytkownika.
            #Przekqazujemy sterowanie do odpowiednich metod na podstawie
            #operacji i jej danych.        
            operationMethod = self.OPERATION_METHODS.get(operation)
            if not operationMethod:
                error = '"%s" nie jest poprawn± operacj±.' % operation
                toDisplay = self.makeError(error)

            if not page.exists() and operation and not \
               (makeChange and operation == self.WRITE):
                #Mo¿na za¿±daæ zasobu, którego strona nie istnieje, ale pod
                #warunkiem, ¿e chce siê stronê utworzyæ.
                toDisplay = self.makeError('Brak strony "%s"' % page.name)

            if operationMethod:
                toDisplay = operationMethod(self, page, makeChange, form)

        #Wszystkie metody operacji a tak¿e makeError maj± zwracaæ zbiór
        #warto¶ci, który mo¿e pos³u¿yæ do wygenerowania odpowiedzi HTML:
        #tytu³ strony, tre¶æ szablonu, s³ownik ze zmiennymi maj±cymi 
        #wype³niæ szablon oraz zestaw ³±cz nawigacyjnych na dó³ strony.    
        title, bodyTemplate, bodyArgs, navLinks = toDisplay
        if page and page.name != Wiki.HOME_PAGE_NAME:
            backLink = '<a href="%s">Powrót na stronê g³ówn±</a>'
            navLinks.append(backLink % self.makeURL())
        print "Content-type: text/html\n"
        print MAIN_TEMPLATE % {'title' : title,
                               'body' : bodyTemplate % bodyArgs,
                               'navLinks' : ' | '.join(navLinks)}

    def viewOperation(self, page, makeChange, form=None, banner=None):
        """Renderuje stronê jako HTML czy to jako efekt g³ównego ¿±dania,
        czy jako efekt uboczny wykonania innej operacji."""
        if banner:
            banner = BANNER_TEMPLATE % banner
        else:
            banner = ''
        if not page.exists():
            title = 'Tworzê %s' % page.name
            toDisplay = (title, WRITE_TEMPLATE,
                         {'title' : title,
                          'banner' : banner,
                          'pageURL' : self.makeURL(page),
                          'text' : ''},
                         [])
        else:
            writeLink = '<a href="%s">Edytuj stronê</a>' \
                        % self.makeURL(page, self.WRITE)
            deleteLink = '<a href="%s">Usuñ stronê</a>' \
                         % self.makeURL(page, self.DELETE)
            toDisplay = (page.name, VIEW_TEMPLATE,
                         {'name' : page.name,
                          'banner' : banner,
                          'processedText' : self.renderPage(page)},
                         [writeLink, deleteLink])
        return toDisplay
            
    def writeOperation(self, page, makeChange, form):
        "Zapisuje stronê lub wy¶wietla formularz edycji lub tworzenia."
        if makeChange:
            data = form.getfirst('dane')
            page.text = data
            page.save()
            #Operacja zosta³a wykonana, ale i tak trzeba zwróciæ co¶ 
            #u¿ytkownikowi. Wy¶wietl now± wersjê strony z odpowiedni± informacj±.
            toDisplay = self.viewOperation(page, 0, banner='Strona zapisana.')
        else:
            navLinks = []
            pageURL = self.makeURL(page)
            if page.exists():
                title = 'Edytujê ' + page.name
                navLinks.append('<a href="%s">Wróæ do %s</a>' % (pageURL,
                                                                 page.name))
            else:
                title = 'Tworzê ' + page.name
            toDisplay = (title, WRITE_TEMPLATE, {'title' : title,
                                                 'banner' : '',
                                                 'pageURL' : pageURL,
                                                 'text' : page.getText()},
                         navLinks)
        return toDisplay
    
    def deleteOperation(self, page, makeChange, form=None):
        "Usuwa stronê lub wy¶wietla formularz usuwania."
        if makeChange:
            page.delete()
            banner = 'Strona "%s" zosta³a usuniêta.' % page.name
            #Strona zosta³a usuniêta, wiêc przejd¼ do g³ównej strony wiki
            #i wy¶wietl tekst informacyjny.
            toDisplay = self.viewOperation(self.wiki.getPage(), 0,
                                           banner=banner)
        else:
            if page.exists():
                title = 'Usuwam ' + page.name
                pageURL = self.makeURL(page)
                backLink = '<a href="%s">Back to %s</a>'
                toDisplay = (title, DELETE_TEMPLATE, {'title' : title,
                                                      'name' : page.name,
                                                      'pageURL' : pageURL},
                             [backLink % (pageURL, page.name)])
            else:
                error = "Nie mo¿na usun±æ nieistniej±cej strony."
                toDisplay = self.makeError(error)
        return toDisplay

    #Odwzorowanie operacji na odpowiadaj±ce im metody.
    OPERATION_METHODS = { VIEW : viewOperation,
                          WRITE: writeOperation,
                          DELETE: deleteOperation }

    def makeError(self, errorMessage):
        "Tworzy s³ownik z informacj± o b³êdzie."
        return (ERROR_TEMPLATE, "B³±d", {'error' : errorMessage,
                                          'mainURL' : self.makeURL("")}, [])

    def makeURL(self, page="", operation=None):
        "Tworzy adres URL dla zasobu zdefiniowanego przez stronê i operacjê."
        if hasattr(page, 'name'):
            #Przekazano obiekt Page zamiast nazwy strony.
            page = page.name
        url = os.environ['SCRIPT_NAME'] + '/' + page
        if operation:
            url += '?operacja=' + operation
        return url

    #Wyra¿enie regularne umo¿liwiaj±ce zmianê wielu znaków nowego wiersza na
    #akapity.
    MULTIPLE_NEWLINES = re.compile("(\r?\n){2,}")

    def renderPage(self, page):
        """Zwraca tekst strony po przekszta³ceniach, w których to tworzy
        kod  HTML: S³owaWiki s± powi±zane z odpowiednimi stronami wy¶wietlania
        lub formularza dodawania natomiast znaki nowego wiersza s± zamienione
        na znaczniki akapitu.."""

        #Najierw zamieñ wszystkie znaczniki HTML na wersje, dziêki którym nie
        #bêd± interpretowane przez przegl±darkê.    
        text = page.getText()
        for find, replace in (('<', '&lt;'), ('>', '&gt;'), ('&', '&amp;')):
            text = text.replace(find, replace)

        #Dowi±¿ wszystkie S³owaWiki do odpowiednich zasobów.
        html = '<p>' + page.WIKI_WORD.sub(self._linkWikiWord, text) \
               + '</p>'

        #Zamieñ wielokrotne znaki nowego wiersza na akapity.
        html = self.MULTIPLE_NEWLINES.sub('</p>\n<p>', html)
        return html

    def _linkWikiWord(self, match):
        """Funkcja pomocnicza u¿ywana do zamiany S³owaWiki na ³±cze do
        odpowiedniej strony (je¶li istnieje) lub na ³±cze zapewniaj±ce utworzenie
        strony (je¶li nie istnieje)."""
        linkedPage = self.wiki.getPage(match.group(0))
        link = ADD_LINK
        if linkedPage.exists():
            link = VIEW_LINK        
        link = link % self.makeURL("%(wikiword)s")
        #Teraz ³±cze wygl±da nastêpuj±co:
        # <a href="/cgi-bin/bittywiki.cgi/%(wikiword)s">%(wikiword)s</a>
        #Element zastêpczy 'wikiword' zostanie zast±piony nazw± strony.
        return link % {'wikiword' : linkedPage.name}

if __name__ == '__main__':
    WikiCGI("lokalnewiki").run()
