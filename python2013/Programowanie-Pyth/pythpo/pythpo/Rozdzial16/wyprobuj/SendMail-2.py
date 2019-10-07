from SendMail import SmartMessage, MailServer
msg = SmartMessage("Ja <ja@przyklad.pl",
                   "Ty <ty@przyklad.pl>",
                   "Twoje zdjêcie",
                   "Oto zdjêcie, które Ci zrobi³em.")
msg.addAttachment(open("zdjecie.jpg").read(), "zdjecie.jpg")
MailServer("localhost").sendMessage(msg)
