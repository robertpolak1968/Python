#!/usr/bin/python
from poplib import POP3
import email
class SubjectLister(POP3):

    """Po��cz si� ze skrzynk� protoko�em POP3 i wy�wietl temat 
    ka�dej wiadomo�ci."""

    def __init__(self, server, username, password):
        "Po��cz si� z serwerem POP3."
        POP3.__init__(self, server, 110)
        #Usu� komentarz z poni�szego wiersza, by zobaczy� pe�en proces komunikacji.
        #self.set_debuglevel(2)
        self.user(username)
        response = self.pass_(password)
        if response[:3] == '+OK':
            #Wyst�pi� problem z po��czeniem.
            raise Exception, response	

    def summarize(self):
        "Pobierz ka�d� wiadomo��, przetw�rz j� i wy�wietl temat."
        numMessages = self.stat()[0]
        print '%d wiadomo�ci w skrzynce.' % numMessages
        parser = email.Parser.Parser()
        for messageNum in range(1, numMessages+1):
	          messageString = '\n'.join(self.top(messageNum, 0)[1])
            message = parser.parsestr(messageString)
            #Przekazanie True do parser.parsestr() powoduje przetwarzanie
            #tylko i wy��cznie nag��wk�w. Poniewa� interesuje nas pobranie
            #ca�o�ci, standardowa wersja mo�e chwil� potrwa�. Wersja pobieraj�ca
            #tylko nag��wki jest dost�pna od Python 2.2.2 i nowszego.
            #message = parser.parsestr(messageString, True)
            print '', message['Subject']

class TopBasedSubjectLister(SubjectLister):

    def summarize(self):
        """Pobierz pierwsz� cz�� wiadomo�ci i odnajd� nag��wek 'Subject:'."""
        print '%d wiadomo�ci w skrzynce.' % self.numMessages
        for messageNum in range(1, self.numMessages+1):
            #Pobiera tylko i wy��cznie nag��wki. W nag��wach 
            #poszukuje tematu.
            for header in self.top(messageNum, 0)[1]:
                if header.find('Subject:') == 0:
                    print header[len('Subject:'):]
                    break

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print 'U�ycie: %s [adres serwera POP3] [u�ytkownik POP3] [has�o POP3]' % sys.argv[0]
        sys.exit(0)
    lister = TopBasedSubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()
