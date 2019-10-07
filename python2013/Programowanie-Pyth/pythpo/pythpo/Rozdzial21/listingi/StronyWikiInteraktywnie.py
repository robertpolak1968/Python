from BittyWiki import Wiki
wiki = Wiki("lokalnewiki")
homePage = wiki.getPage()
homePage.text = "To jest strona g³ówna\n\nZawiera ³±cza do StronaDruga i StronaTrzecia."
homePage.save()
#Teraz folder "lokalnewiki" zawiera pliki wiki.
import os
open(os.path.join("lokalnewiki","StronaGlowna")).read()
page2 = wiki.getPage("StronaDruga")
page2.exists()
page2.text = "Strona numer 2.\n\nZawiera ³±cze do StronaGlowna."
page2.save()
page2.exists()
wiki.getPage("Wiki")
