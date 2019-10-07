#!/usr/bin/python
from imaplib import IMAP4
import email
import re

#U�ywane do przetworzenia odpowiedzi IMAP.
FROM_HEADER = 'From: '
IMAP_UID = re.compile('UID ([0-9]+)')

#Po��czenie z serwerem.
server = IMAP4('imap.przyklad.pl')
server.login('[u�ytkownik]', '[has�o]')
server.select('Inbox')

#Pobranie unikatowych identyfikator�w wiadomo�ci.
uids = server.uid('SEARCH', 'ALL')[1][0].split(' ')
uidString = ','.join(uids)

#Pobierz nag��wek From ka�dej wiadomo�ci.
headers = server.uid('FETCH', '%s' % uidString,	
                     '(BODY[HEADER.FIELDS (FROM	)])')
for header in headers[1]:
    if len(header) > 1:
        uid, header = header
        #Przetw�rz odpowied� IMAP na rzeczywisty UID i warto�� nag��wka From.
        match = IMAP_UID.search(uid)
        uid = match.groups(1)[0]

        fromHeader = header[len(FROM_HEADER):].strip()

        #Utw�rz skrzynk� dla osoby, kt�ra wys�a�a wiadomo��.
        #Je�li ju� istnieje, serwer zg�osi b��d, ale my go zignorujemy.
        server.create(fromHeader)

        #Skopiuj wiadomo�� do skrzynki.
        server.uid('COPY', uid, fromHeader)

#Usu� wiadomo�ci ze skrzynki odbiorczej, poniewa� zosta�y przetworzone.
server.uid('STORE', uidString, '+FLAGS.SILENT', '(\\Deleted)')
server.expunge()        
