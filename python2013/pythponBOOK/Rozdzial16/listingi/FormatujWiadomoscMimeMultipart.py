#!/usr/bin/python
from email.MIMEMultipart import MIMEMultipart
import os
import sys

filename = sys.argv[1]

msg = MIMEMultipart()
msg['From'] = 'Ja <ja@przyklad.pl>'
msg['To'] = 'Ty <jeffar@localhost>'
msg['Subject'] = 'Twoje zdjêcie'

from email.MIMEText import MIMEText
text = MIMEText("Oto zdjêcie, które Ci zrobi³em.","plain","iso-8859-2")
msg.attach(text)

from email.MIMEImage import MIMEImage
image = MIMEImage(open(filename).read(), name=os.path.split(filename)[1])
msg.attach(image)
print str(msg)
