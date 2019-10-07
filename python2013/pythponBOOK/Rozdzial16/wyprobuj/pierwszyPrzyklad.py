fromAddress = 'nadawca@example.com'
toAddress = 'jeffar@localhost'
msg = "Subject: Witaj\n\nTo jest treść wiadomości." 
import smtplib
server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, msg)
