"""Ten modu³ zawiera kod rdzenia BittyWiki. Kod ten nie jest zwi±zany z 
¿adnym konkretnym interfejsem."""

import re
import os

class Wiki:
    "Klasa reprezentuj±ca wiki jako ca³o¶æ."
    HOME_PAGE_NAME = "StronaGlowna"

    def __init__(self, base):
        "Inicjalizacja wiki stosuj±cej przekazany folder g³ówny."
        self.base = base

        if not os.path.exists(self.base):
            os.makedirs(self.base)
        elif not os.path.isdir(self.base):
            raise IOError('Podana baza wiki "%s" nie jest folderem!' % self.base)

    def getPage(self, name=None):
        """Pobiera wskazan± stronê wiki, która mo¿e istnieæ, ale nie musi."""
        if not name:
            name = self.HOME_PAGE_NAME
        return Page(self, name)

class Page:
    """Klasa reprezentuj±ca jedn± stronê wiki. Zawiera ca³± logikê zwi±zan±
    z modyfikacj± strony i sprawdzaniem, na które inne strony wskazuje."""

    #Jako S³owoWiki traktujemy ka¿de s³owo zaczynaj±ce siê z wielkiej litery,
    #zawieraj±ce inn± wielk± literê i sk³adaj±cesiê z liter lub cyfr.
    WIKI_WORD_MATCH = "(([A-Z][a-z0-9]*){2,})"
    WIKI_WORD = re.compile(WIKI_WORD_MATCH)
    WIKI_WORD_ALONE = re.compile('^%s$' % WIKI_WORD_MATCH)

    def __init__(self, wiki, name):
        """Inicjalizuje stronê dla wskazsnego wiki o przekazanej nazwie.
        Sprawdza, czy nazwa jest poprawna. Strona mo¿e istnieæ, ale 
        niekoniecznie musi tak byæ."""

        #WIKI_WORD dopasowuje siê do S³owaWiki w dowolnym miejscu. Chcemy mieæ
        #pewno¶æ, ¿e strona to StrinaWiki i nic innego.
        if not self.WIKI_WORD_ALONE.match(name):
            raise NotWikiWord, name
        self.wiki = wiki
        self.name = name
        self.path = os.path.join(self.wiki.base, name)

    def exists(self):
        "Zwraca warto¶æ true, je¶li istnieje strona wiki o takiej nazwie."
        return os.path.isfile(self.path)

    def load(self):
        "Wczytuje stronê z dysku, je¶li istnieje."
        if not hasattr(self, 'text'):
            self.text = ''
            if self.exists():
                self.text = open(self.path, 'r').read()
            
    def save(self):
        "Zapisuje stronê. Je¶li nie istnia³a, tworzy j±."
        if not hasattr(self, 'text'):
            self.text = ''
        out = open(self.path, 'w')
        out.write(self.text)
        out.close()

    def delete(self):
        "Usuwa stronê, zak³adaj±c, ¿e wcze¶niej istnia³a."
        if self.exists():
            os.remove(self.path)

    def getText(self):
        "Zwraca surowy tekst strony."
        self.load()
        return self.text

class NotWikiWord(Exception):
    """Wyj±tek zg³aszany wtedy, gdy kto¶ chce przekazaæ s³owo nie bêd±ce
    SlowemWiki jako S³owoWiki.."""
    pass
