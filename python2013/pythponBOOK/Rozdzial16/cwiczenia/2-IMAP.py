#!/usr/bin/python
from imaplib import IMAP4
import email
import re

#U¿ywane do przetworzenia odpowiedzi IMAP.
FROM_HEADER = 'From: '
IMAP_UID = re.compile('UID ([0-9]+)')

#Po³±czenie z serwerem.
server = IMAP4('imap.przyklad.pl')
server.login('[u¿ytkownik]', '[has³o]')
server.select('Inbox')

#Pobranie unikatowych identyfikatorów wiadomo¶ci.
uids = server.uid('SEARCH', 'ALL')[1][0].split(' ')
uidString = ','.join(uids)

#Pobierz nag³ówek From ka¿dej wiadomo¶ci.
headers = server.uid('FETCH', '%s' % uidString,	
                     '(BODY[HEADER.FIELDS (FROM	)])')
for header in headers[1]:
    if len(header) > 1:
        uid, header = header
        #Przetwórz odpowied¼ IMAP na rzeczywisty UID i warto¶æ nag³ówka From.
        match = IMAP_UID.search(uid)
        uid = match.groups(1)[0]

        fromHeader = header[len(FROM_HEADER):].strip()

        #Utwórz skrzynkê dla osoby, która wys³a³a wiadomo¶æ.
        #Je¶li ju¿ istnieje, serwer zg³osi b³±d, ale my go zignorujemy.
        server.create(fromHeader)

        #Skopiuj wiadomo¶æ do skrzynki.
        server.uid('COPY', uid, fromHeader)

#Usuñ wiadomo¶ci ze skrzynki odbiorczej, poniewa¿ zosta³y przetworzone.
server.uid('STORE', uidString, '+FLAGS.SILENT', '(\\Deleted)')
server.expunge()        
