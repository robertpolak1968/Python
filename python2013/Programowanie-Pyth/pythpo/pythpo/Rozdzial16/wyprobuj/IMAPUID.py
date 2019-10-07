import imaplib
import email
imap = imaplib.IMAP4('imap4.przyklad.pl')
imap.login('uzytkownik', 'haslo')
imap.select('Inbox')[1][0]

#Pobierz unikatowe identyfikatory wiadomo¶ci.
uids = imap.uid('SEARCH', 'ALL')
print uids
uids = uids[1][0].split(' ')

#Pobierz pierwsz± wiadomo¶æ.
messageText = imap.uid('FETCH', uids[0], "(RFC822)")[1][0][1]
message = email.message_from_string(messageText)
print message['Subject']
