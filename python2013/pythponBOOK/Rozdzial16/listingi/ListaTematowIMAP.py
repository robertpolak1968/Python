#!/usr/bin/python
from imaplib import IMAP4

class SubjectLister(IMAP4):
    """£±czy siê ze skrzynk± IMAP4 i pobiera listê tematów wszystkich
    wiadomo¶ci."""

    def __init__(self, server, username, password):
        "£±czy siê z serwerem IMAP."
        IMAP4.__init__(self, server)
        #Usuñ komentarz z poni¿szego wiersza, by zobaczyæ szczegó³y komunikacji.
        #self.debug = 4
        self.login(username, password)

    def summarize(self, mailbox='Inbox'):
        "Pobiera tematy wszystkich wiadomo¶ci ze wskazanej skrzynki."
        #Polecenie SELECT czyni wskazan± skrzynkê sprzynk± aktualn±
        #i zwraca liczbê wiadomo¶ci. Ka¿da wiadomo¶æ dostêpna jest na 
        #podstawie numeru. Je¶li skrzynka zawiera 10 wiadomo¶cin
        #to s± one ponumerowane od 1 do 10.
        numberOfMessages = int(self._result(self.select(mailbox)))
        
        print '%s wiadomo¶ci w skrzynce "%s":' % (numberOfMessages, mailbox)

        #Polecenie FETCH przyjmuje oddzielon± przecinkami listê numerów
        #wiadomo¶ci i tekst okre¶laj±cy, które czê¶ci wiadomo¶ci maj± zostaæ
        #pobrane. W przedstawionym przyk³adzie potrzenujemy jedynie 
        #nag³ówka 'Subject', wiêc stosujemy tekst o nastêpuj±cej tre¶ci:
        #'(BODY[HEADER.FIELDS (SUBJECT)])'.
        #
        #Sekcja 6.4.5 dokumentu RFC3501 zawiera szczegó³owe informacje na temat
        #formatu i elementów tekstu okre¶laj±cego elementy wiadomo¶ci.
        #Aby pobraæ ca³± wiadomo¶æ w formacie odpowiednim dla analizatora,
        #zastosuj tekst '(RFC822)'.

        subjects = self._result(self.fetch('1:%d' % numberOfMessages,
                                         '(BODY[HEADER.FIELDS (SUBJECT)])'))
        for subject in subjects:
            if hasattr(subject, '__iter__'):
                subject = subject[1]                
                print '', subject[:subject.find('\n')]

    def _result(self, result):
        """Ka¿da metoda z imaplib zwraca listê zawieraj±c± kod statusu
        i zbiór rzeczywistych danych. Ta metoda dodatkowa zg³asza wyj±tek,
        je¶li kod statusu jest inny od "OK".
        Je¶li wszystko jest w porz±dku, zwraca uzyskane dane.
        """
        status, result = result
        if status != 'OK':
            raise status, result
        if len(result) == 1:
            result = result[0]
        return result

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print 'U¿ycie: %s [adres serwera IMAP] [u¿ytkownik IMAP] [has³o IMAP]' % sys.argv[0]
        sys.exit(0)
    lister = SubjectLister(sys.argv[1], sys.argv[2], sys.argv[3])
    lister.summarize()
