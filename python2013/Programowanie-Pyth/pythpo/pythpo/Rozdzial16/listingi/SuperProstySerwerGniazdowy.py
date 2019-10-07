#!/usr/bin/python
import socket
import sys

if len(sys.argv) < 3:
    print 'Użycie: %s [nazwa hosta] [numer portu]' % sys.argv[0]
    sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

#Tworzy proste gniazdo serwerowe. Metoda setsockopt umożliwia
#serwerowi użycie danego portu, nawet jeśli był wcześniej używany przez
#inny serwer (na przykład wcześniejszą wersję tego skryptu.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Dołączenie gniazda do portu i rozpoczęcie nasłuchiwania.
sock.bind((hostname, port))
sock.listen(1)
print "Oczekiwanie na żądanie."

#Obsługa żądania.
request, clientAddress = sock.accept()
print "Otrzymano żądane od", clientAddress
request.send('-=SuperProstySerwerGniazdowy 3000=-\n')
request.send('Odejdź!\n')
request.shutdown(2) #Zatrzymuje odczyt i zapis.
print "Zakończono obsługę, zatrzymuję serwer."
sock.close()
