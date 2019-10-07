from email.MIMEImage import MIMEImage
filename = "zdjecie.jpg"
msg = MIMEImage(open(filename).read(), name=filename)
msg['From'] = 'Ja <ja@przyklad.pl>'
msg['To'] = 'Ty <jeffar@localhost>'
msg['Subject'] = 'Twoje zdjêcie'
print str(msg)
fromAddress = 'nadawca@example.com'
toAddress = 'jeffar@localhost'
import smtplib
server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, str(msg))
