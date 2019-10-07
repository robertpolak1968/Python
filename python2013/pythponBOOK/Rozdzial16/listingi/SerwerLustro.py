#!/usr/bin/python
import socket

class MirrorServer:
    """Pobiera tekst wiersz po wierszu a następnie wysyła odwróconą
    wersję tego samego tekstu."""

    def __init__(self, port):        
        "Dołącza serwer do określonego portu."
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(port)
        #Umożliwia zebranie pięciu zgłoszeń w kolejce przed odrzuceniem klienta.
        self.socket.listen(5)

    def run(self):
        "Obsługuje żadanie nieskończenie długo."
        while True:
            request, client_address = self.socket.accept()
            #Zmienia połączenia na pliki.
            input = request.makefile('rb', 0)
            output = request.makefile('wb', 0)
            l = True
            try:
                while l:
                    l = input.readline().strip()
                    if l:                        
                        output.write(l[::-1] + '\r\n')
                    else:
                        #Pusty wiersz oznacza chęć zakończenia połączenia.
                        request.shutdown(2) #Zamknij odczyt i zapis.
            except socket.error:
                #Najprawdopodobniej klient rozłączył się.
                pass
            
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Użycie: %s [adres] [numer portu]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    MirrorServer((hostname, port)).run()
