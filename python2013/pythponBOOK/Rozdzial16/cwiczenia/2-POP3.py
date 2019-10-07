#!/usr/bin/python
from poplib import POP3
from email.Parser import Parser

#Po³±cz siê z serwerem i przetwórz odpowied¼, by dowiedzieæ siê, ile
#jest wiadomo¶ci. Element ten jest bardzo podobny do przyk³adu z rozdzia³u.
server = POP3("pop.przyklad.pl")
server.user("[u¿ytkownik]")
response = server.pass_("[has³o]")
numMessages = response[response.rfind(', ')+2:]
numMessages = int(numMessages[:numMessages.find(' ')])

#Przetwórz ka¿d± wiadomo¶æ i umie¶æ j± w pliku o nazwie zgodnej z nag³ówkiem
#From wiadomo¶ci.
parser = Parser()
openFiles = {}
for messageNum in range(1, numMessages+1):
    messageString = '\n'.join(server.retr(messageNum)[1])
    message = email.parsestr(messageString, True)
    fromHeader = message['From']
    mailFile = openFiles.get(fromHeader)
    if not mailFile:
        mailFile = open(fromHeader, 'w')
        openFiles[fromHeader] = mailFile
    mailFile.write(messageString)
    mailFile.write('\n')
#Zamknij wszystkie pliki, w jakich by³y zapisywane wiadomo¶ci.
for openFile in openFiles.values():
    openFile.close()
