#!/usr/bin/python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor

# Otwórz plik XSTL jako strumień.
xsl = open('RSSnaHTML.xsl')

# Przetwórz strumienie i utwórz z nich źródła wejściowe.
parsedxml = InputSource.DefaultFactory.fromUri("http://www.pheedo.com/f/newscientist_mars-rovers")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "RSSnaHTML.xsl")

# Utwórz nowy procesor, dołącz do niego arkusz stylu a następnie przekształć XML.
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

# Zapisz wyjściowy dokument HTML w pliku.
output = open("agregator.html", 'w')
output.write(HTML)
output.close
