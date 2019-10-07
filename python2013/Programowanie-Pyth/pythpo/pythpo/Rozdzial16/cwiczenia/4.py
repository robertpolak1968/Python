#!/usr/bin/python
import SocketServer
import re
import socket

class ClientError(Exception):
    "Wyjątek zgłaszany, gdy klient wysłał do serwera niepoprawne dane."
    pass

class PythonChatServer(SocketServer.ThreadingTCPServer):
    "Klasa serwera."

    def __init__(self, server_address, RequestHandlerClass):
        """Tworzy początkowo puste odwzorowanie pseudonimów na 
        obiekt pseudopliku używanego do wysyłania informacji do klienta."""
        SocketServer.ThreadingTCPServer.__init__(self, server_address,
                                                 RequestHandlerClass)
        self.users = {}

class RequestHandler(SocketServer.StreamRequestHandler):
    """Obsługuje cykl życia połączenia klienta z serwerem:
    połączenie, rozmowę, przekazywanie poleceń i rozłączenie."""

    NICKNAME = re.compile('^[A-Za-z0-9_-]+$') #Wyrażenie regularne sprawdza poprawność pseudonimu.

    def handle(self):
        """Obsługa połączenia: pobiera pseudonim użytkownika a następnie
        przetwarza wejście aż do uzyskania polecenia quit lub zerwania
        połączenia."""
        self.nickname = None

        self.privateMessage('Kim jesteś?')
        nickname = self._readline()
        done = False
        try:
            self.nickCommand(nickname)
            self.privateMessage('Witaj %s. Witamy na serwerze pogawędek.'\
                                % nickname)
            self.broadcast('%s dołączył do pokoju.' % nickname, False)
        except ClientError, error:
            self.privateMessage(error.args[0])        
            done = True
        except socket.error:
            done = True

        #Użytkownik zalogowany, więc może rozmawiać.
        while not done:
            try:
                done = self.processInput()
            except ClientError, error:
                self.privateMessage(str(error))
            except socket.error, e:
                done = True

    def finish(self):                        
        "Wywoływany automatycznie po zakończeniu handle()."
        if self.nickname:
            #Użytkownik był poprawnie połączony przed rozłączeniem. 
            #Poinformuj innych o jego wyjściu.
            message = '%s opuścił pokój.' % self.nickname
            if hasattr(self, 'partingWords'):
                message = '%s opuścił pokój: %s' % (self.nickname,
                                               self.partingWords)
            self.broadcast(message, False)

            #Usuń użytkownika z listy, aby nie wysyłać do niego nowych wiadomości.
            if self.server.users.get(self.nickname):
                del(self.server.users[self.nickname])
        self.request.shutdown(2)
        self.request.close()

    def processInput(self):
        """Odczytaj wiersz z gniazda. Sprawdź, czy jest to polecenie.
        Jeśli nie, roześlij tekst do wszystkich osób."""
        done = False
        l = self._readline()
        command, arg = self._parseCommand(l)
        if command:
            done = command(arg)
        else:            
            l = '<%s> %s\n' % (self.nickname, l)
            self.broadcast(l)
        return done

    #Implementacje poleceń serwera.

    def nickCommand(self, nickname):
        "Próbuje zmienić pseudonim użytkownika."
        if not nickname:
            raise ClientError, 'Nie podano pseudonimu.'
        if not self.NICKNAME.match(nickname):
            raise ClientError, 'Niepoprawy pseudonim: %s' % nickname
        if nickname == self.nickname:
            raise ClientError, 'Jesteś już znany jako %s.' % nickname
        if self.server.users.get(nickname, None):
            raise ClientError, 'Istnieje już użytkownik o pseudonimie "%s".' % nickname
        oldNickname = None
        if self.nickname:
            oldNickname = self.nickname
            del(self.server.users[self.nickname])
        self.server.users[nickname] = self.wfile
        self.nickname = nickname
        if oldNickname:
            self.broadcast('%s zmienił pseudonim na %s' % (oldNickname, self.nickname))

    def quitCommand(self, partingWords):
        """Informuje innych użytkowników o opuszczaniu pokoju i
        zapewnia zamknięcie połączenia przez uchwyt."""
        if partingWords:
            self.partingWords = partingWords
        #Zwrócenie True zapewnia rozłączenie użytkownika.
        return True

    def namesCommand(self, ignored):
        "Zwraca listę użytkowników obecnych w pokoju."
        self.privateMessage(', '.join(self.server.users.keys()))

    def msgCommand(self, nicknameAndMsg):
        "Wysyła prywatną wiadomość do innego użytkownika."
        if not ' ' in nicknameAndMsg:
            raise ClientError('nie określono wiadomości.')
        nickname, msg = nicknameAndMsg.split(' ', 1)
        if nickname == self.nickname:
            raise ClientError('Naprawdę chcesz wysłać wiadomość do samego siebie?')
        user = self.server.users.get(nickname)
        if not user:
            raise ClientError('Nie ma użytkownika: %s' % nickname)
        msg = '[Wiadomość prywatna od %s] %s' % (self.nickname, msg)
        user.write(self._ensureNewline(msg))

    #Metody pomocnicze.
    
    def broadcast(self, message, includeThisUser=True):
        """Wysyła wiadomość do wszystkich osób, ewentualnie wyłącza z tej listy
        użytkownika, który oryginalnie wysyłał wiadomość."""
        message = self._ensureNewline(message)
        for user, output in self.server.users.items():
            if includeThisUser or user != self.nickname:
                output.write(message)

    def privateMessage(self, message):
        "Wysyła do użytkownika wiadomość prywatną."
        self.wfile.write(self._ensureNewline(message))

    def _readline(self):
        "Wczytuje wiersz, usuwając białe spacje."
        return self.rfile.readline().strip()

    def _ensureNewline(self, s):
        "Upewnia się, że tekst kończy się znakiem końca wiersza."
        if s and s[-1] != '\n':
            s += '\r\n'
        return s

    def _parseCommand(self, input):
        """Próbuje przetworzyć tekst jako polecenie serwera. Jeśli istnieje
        zaimplementowana metoda dla polecenia, wykonuje ją."""
        commandMethod, arg = None, None
        if input and input[0] == '/':
            if len(input) < 2:
                raise ClientError, 'Niepoprawne polecenie: "%s"' % input
            commandAndArg = input[1:].split(' ', 1)
            if len(commandAndArg) == 2:
                command, arg = commandAndArg
            else:
                command, = commandAndArg
            commandMethod = getattr(self, command + 'Command', None)
            if not commandMethod:
                raise ClientError, 'Brak polecenia: "%s"' % command
        return commandMethod, arg

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print 'Użycie: %s [adres] [numer portu]' % sys.argv[0]
        sys.exit(1)
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    PythonChatServer((hostname, port), RequestHandler).serve_forever()
