#!/usr/bin/python
import socket
import select
import sys
import os
from threading import Thread

class ChatClient:

    def __init__(self, host, port, nickname):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.input = self.socket.makefile('rb', 0)
        self.output = self.socket.makefile('wb', 0)

        #Send the given nickname to the server.
        authenticationDemand = self.input.readline()
        if not authenticationDemand.startswith("Kim jesteś?"):
            raise Exception, "To nie wydaje się być serwer pogawędek."
        self.output.write(nickname + '\r\n')
        response = self.input.readline().strip()
        if not response.startswith("Witaj"):
            raise Exception, response
        print response

        #Zacznij od wyświetlenia listy pseudonimów.
        self.output.write('/names\r\n')
        print "Aktualnie w pokoju znajdują się:", self.input.readline().strip()

        self.run()

    def run(self):
        """Uruchom osobny wątek, by pobierać dane z klawiatury, nawet
        jeśli w tym samym czasie przyjdzie komunikat z sieci.
        W ten sposób klient może jednocześnie wysyłać i odbierać wiadomości."""
        
        propagateStandardInput = self.PropagateStandardInput(self.output)
        propagateStandardInput.start()

        #Odczytaj nadesłane dane i wyświetl je na standardowym wyjściu.
        #Brak danych oznacza rozłączenie.
        inputText = True
        while inputText:
            inputText = self.input.readline()
            if inputText:
                print inputText.strip()
        propagateStandardInput.done = True

    class PropagateStandardInput(Thread):
        """Klasa, która kopiuje standardowe wejście do serwera aż do momentu,
        gdy nie zostanie przerwana."""

        def __init__(self, output):
            """Niech ten wątek będzie wątkiem demonowym, by interpreter Pythona
            nie czekał na jego zakończenie, gdy będzie to jedyny działający
            wątek."""
            Thread.__init__(self)
            self.setDaemon(True)
            self.output = output
            self.done = False

        def run(self):
            "Przekazuj standardowe wejście do serwera aż do informacji o zatrzymaniu."
            while not self.done:
                inputText = sys.stdin.readline().strip()
                if inputText:
                    self.output.write(inputText + '\r\n')

class SelectBasedChatClient(ChatClient):

    def run(self):
        """W krótkiej pętli sprawdzaj, czy użytkownik wpisał tekst lub też
        czy przyszłydane z sieci. Wykonuj to zadanie aż do momentu zwrócenia
        EOF przez połączenie sieciowe."""
        socketClosed = False
        while not socketClosed:
            toRead, ignore, ignore = select.select([self.input, sys.stdin],
                                                   [], [])
            #Nie jesteśmy rozłączeni.
            for input in toRead:                
                if input == self.input:
                    inputText = self.input.readline()
                    if inputText:
                        print inputText.strip()
                    else:
                        #Próba odczytu nie powiodła się. Gniazdo jest zamknięte.
                        socketClosed = True
                elif input == sys.stdin:
                    input = sys.stdin.readline().strip()
                    if input:
                        self.output.write(input + '\r\n')

if __name__ == '__main__':
    import sys
    #Sprawdż, czy można zastosować nazwę użytkownika z systemu operacyjnego.
    #Jeśli nie, należy pobrać nazwę z przekazanych parametrów.
    try:
        import pwd
        defaultNickname = pwd.getpwuid(os.getuid())[0]
    except ImportError:
        defaultNickname = None

    if len(sys.argv) < 3 or not defaultNickname and len(sys.argv) < 4:
        print 'Użycie: %s [adres serwera] [numer portu] [pseudonim]' % sys.argv[0]
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])

    if len(sys.argv) > 3:
        nickname = sys.argv[3]
    else:
        #Musimy korzystać z systemu z nazwami użytkowników.
        #W przeciwnym razie już zakończylibyśmy skrypt.
        nickname = defaultNickname

    ChatClient(hostname, port, nickname)
