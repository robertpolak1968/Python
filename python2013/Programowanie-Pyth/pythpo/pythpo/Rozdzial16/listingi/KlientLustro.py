#!/usr/bin/python
import socket

class MirrorClient:
    "Klient dla serwer odwracającego tekst."

    def __init__(self, server, port):        
        "Połącz się z serwerem."
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server, port))

    def mirror(self, s):
        "Wyślij tekst do serwera a następnie wyświetl odpowiedź."
        if s[-1] != '\n':
            s += '\r\n'
        self.socket.send(s)

        #Odczytuj fragmenty wiadomości aż do nadejścia znaku nowego wiersza;
        #oznacza to koniec odpowiedzi.

        buf = []
        input = ''
        while not '\n' in input:
            try:
                input = self.socket.recv(1024)
                buf.append(input)
            except socket.error:
                break
        return ''.join(buf)[:-1]

    def close(self):
        self.socket.send('\r\n') #Nie chcemy niczego odwracać.
        self.socket.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print 'Użycie: %s [serwer] [port] [tekst do odwrócenia]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    toMirror = sys.argv[3]

    m = MirrorClient(hostname, port)
    print m.mirror(toMirror)
    m.close()
