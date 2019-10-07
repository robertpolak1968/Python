from SendMail import SmartMessage
msg = SmartMessage("Ja <ja@przyklad.pl>", "Ty <jeffar@przyklad.pl>", "Twoje zdjêcie", "Oto zdjêcie, które Ci zrobi³em.")
print str(msg)
msg.addAttachment(open("zdjecie.jpg").read(), "zdjecie.jpg")
print str(msg)
