from SendMail import SmartMessage
msg = SmartMessage("Ja <ja@przyklad.pl>", "Ty <jeffar@przyklad.pl>", "Twoje zdj�cie", "Oto zdj�cie, kt�re Ci zrobi�em.")
print str(msg)
msg.addAttachment(open("zdjecie.jpg").read(), "zdjecie.jpg")
print str(msg)
