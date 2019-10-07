from twisted.internet import protocol, reactor
from twisted.protocols import basic

class MirrorProtocol(basic.LineReceiver):
    "Obsługuje żądania odwrócenia tekstu."
    
    def lineReceived(self, line):
        """Klient wysłał wiersz tekstu. Zapisz jego odwróconą wersję."""    
        self.transport.write(line[::-1]+ '\r\n')

class MirrorFactory(protocol.ServerFactory):
    protocol = MirrorProtocol    

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Użycie: %s [adres] [numer portu]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    reactor.listenTCP(port, MirrorFactory(), interface=hostname)
    reactor.run()
