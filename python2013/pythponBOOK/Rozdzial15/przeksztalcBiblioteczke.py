#!/usr/bin/python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor

# Otwórz pliki XML i XSTL jako strumienie.
xml = open('biblioteczka.xml')
xsl = open('biblioteczkaHTML.xsl')

# Przetwórz strumienie i utwórz z nich Ÿród³a wejœciowe.
parsedxml = InputSource.DefaultFactory.fromStream(xml , "biblioteczka.xml")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "biblioteczkaHTML.xsl")

# Utwórz nowy procesor, do³¹cz do niego arkusz stylu a nastêpnie przekszta³æ XML.
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

# Zapisz wyjœciowy dokument XML w pliku.
output = open("biblioteczka.html", 'w')
output.write(HTML)
output.close
