from SendMail import SmartMessage, MailServer
msg = SmartMessage("Ja <ja@przyklad.pl",
                   "Ty <ty@przyklad.pl>",
                   "Twoje zdj�cie",
                   "Oto zdj�cie, kt�re Ci zrobi�em.")
msg.addAttachment(open("zdjecie.jpg").read(), "zdjecie.jpg")
MailServer("localhost").sendMessage(msg)
