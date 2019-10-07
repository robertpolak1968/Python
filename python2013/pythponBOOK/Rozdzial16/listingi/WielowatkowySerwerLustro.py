#!/usr/bin/python
import SocketServer

class RequestHandler(SocketServer.StreamRequestHandler):
    "Obsługuje żądania odwrócenia tekstu."

    def handle(self):
        """Odczytuje dane ze składowej rfile dostarczanej przez
        StreamRequestHandler. Zawiera ona dane od klienta.
        Następnie odwraca tekst i zapisuje go do składowej wfile,
        czyli wysyła dane do klienta."""       
        l = True
        while l:
            l = self.rfile.readline().strip()
            if l:
                self.wfile.write(l[::-1] + '\n')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Użycie: %s [adres] [numer portu]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    server = SocketServer.ThreadingTCPServer((hostname, port), RequestHandler)
    server.serve_forever()
