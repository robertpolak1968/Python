#!/usr/bin/python
#Ten przykład jest ZŁY! Nie używaj go!
from twisted.internet import protocol, reactor
from twisted.protocols import basic
import time

class MirrorProtocol(basic.LineReceiver):
    "Obsługuje żądania odwrócenia tekstu."

    def __init__(self):
        """Ustaw licznik w taki sposób, by pierwsze żądanie klienta
        zawsze wykonało się od razu."""
        self.lastUsed = 0
        
    def lineReceived(self, line):
        """Klient wysłał wiersz tekstu. Zapisz odwróconą wersję,
        być może czekając odpowiedni przedział czasu.
        Uwaga: to nie jest dobra implementacja, ponieważ
        korzystamy ze szkieletu Twisted a time.sleep() jest
        wywołaniem blokującym."""
        elapsed = time.time() - self.lastUsed
        print elapsed
        if elapsed < (self.factory.PER_USER_TIMEOUT * 1000):
            time.sleep(self.factory.PER_USER_TIMEOUT-elapsed)
        self.transport.write(line[::-1]+ '\r\n')
        self.lastUsed = time.time()

class MirrorFactory(protocol.ServerFactory):
    "Serwer dla protokołu odwracania wierszy przedstawionego powyżej."
    protocol = MirrorProtocol    
    PER_USER_TIMEOUT = 5


#Ten przykład jest POPRAWNY! Używa metody zwracającej obiekt Deferred
#(reactor.callLater) i rejestruje dla niego odpowiednie wywołanie zwrotne.
from twisted.internet import protocol, reactor
from twisted.protocols import basic
import time

class MirrorProtocol(basic.LineReceiver):
    "Obsługuje żądania odwrócenia tekstu."
    
    def __init__(self):
        """Ustaw licznik w taki sposób, by pierwsze żądanie klienta
        zawsze wykonało się od razu."""
        self.lastUsed = 0
        
    def lineReceived(self, line):
        """Klient wysłał wiersz tekstu. Zapisz odwróconą wersję,
        być może czekając odpowiedni przedział czasu.
        To jest dobra implementacja, ponieważ korzysta z metody
        zwracającej obiekt Deferred (reactor.callLater())
        i rejestruje wywołanie zwrotne (writeLine) dla tego obiektu."""

        elapsed = time.time() - self.lastUsed
        if elapsed < self.factory.PER_USER_TIMEOUT:
            reactor.callLater(self.factory.PER_USER_TIMEOUT-elapsed,
                              self.writeLine, line)
        else:
            self.writeLine(line)

    def writeLine(self, line):
        "Zapisuje wiersz i ustala opóźnienie."
        self.transport.write(line[::-1] + '\r\n')
        self.lastUsed = time.time()

class MirrorFactory(protocol.ServerFactory):
    "Serwer obsługujący odwracanie wierszy tekstu."
    protocol = MirrorProtocol    
    PER_USER_TIMEOUT = 5

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Użycie: %s [adres] [numer portu]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    reactor.listenTCP(port, MirrorFactory(), interface=hostname)
    reactor.run()
