"""Ten modu� zawiera kod rdzenia BittyWiki. Kod ten nie jest zwi�zany z 
�adnym konkretnym interfejsem."""

import re
import os

class Wiki:
    "Klasa reprezentuj�ca wiki jako ca�o��."
    HOME_PAGE_NAME = "StronaGlowna"

    def __init__(self, base):
        "Inicjalizacja wiki stosuj�cej przekazany folder g��wny."
        self.base = base

        if not os.path.exists(self.base):
            os.makedirs(self.base)
        elif not os.path.isdir(self.base):
            raise IOError('Podana baza wiki "%s" nie jest folderem!' % self.base)

    def getPage(self, name=None):
        """Pobiera wskazan� stron� wiki, kt�ra mo�e istnie�, ale nie musi."""
        if not name:
            name = self.HOME_PAGE_NAME
        return Page(self, name)

class Page:
    """Klasa reprezentuj�ca jedn� stron� wiki. Zawiera ca�� logik� zwi�zan�
    z modyfikacj� strony i sprawdzaniem, na kt�re inne strony wskazuje."""

    #Jako S�owoWiki traktujemy ka�de s�owo zaczynaj�ce si� z wielkiej litery,
    #zawieraj�ce inn� wielk� liter� i sk�adaj�cesi� z liter lub cyfr.
    WIKI_WORD_MATCH = "(([A-Z][a-z0-9]*){2,})"
    WIKI_WORD = re.compile(WIKI_WORD_MATCH)
    WIKI_WORD_ALONE = re.compile('^%s$' % WIKI_WORD_MATCH)

    def __init__(self, wiki, name):
        """Inicjalizuje stron� dla wskazsnego wiki o przekazanej nazwie.
        Sprawdza, czy nazwa jest poprawna. Strona mo�e istnie�, ale 
        niekoniecznie musi tak by�."""

        #WIKI_WORD dopasowuje si� do S�owaWiki w dowolnym miejscu. Chcemy mie�
        #pewno��, �e strona to StrinaWiki i nic innego.
        if not self.WIKI_WORD_ALONE.match(name):
            raise NotWikiWord, name
        self.wiki = wiki
        self.name = name
        self.path = os.path.join(self.wiki.base, name)

    def exists(self):
        "Zwraca warto�� true, je�li istnieje strona wiki o takiej nazwie."
        return os.path.isfile(self.path)

    def load(self):
        "Wczytuje stron� z dysku, je�li istnieje."
        if not hasattr(self, 'text'):
            self.text = ''
            if self.exists():
                self.text = open(self.path, 'r').read()
            
    def save(self):
        "Zapisuje stron�. Je�li nie istnia�a, tworzy j�."
        if not hasattr(self, 'text'):
            self.text = ''
        out = open(self.path, 'w')
        out.write(self.text)
        out.close()

    def delete(self):
        "Usuwa stron�, zak�adaj�c, �e wcze�niej istnia�a."
        if self.exists():
            os.remove(self.path)

    def getText(self):
        "Zwraca surowy tekst strony."
        self.load()
        return self.text

class NotWikiWord(Exception):
    """Wyj�tek zg�aszany wtedy, gdy kto� chce przekaza� s�owo nie b�d�ce
    SlowemWiki jako S�owoWiki.."""
    pass
