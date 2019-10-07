#!/usr/bin/python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor

# Otw�rz pliki XML i XSTL jako strumienie.
xml = open('biblioteczka.xml')
xsl = open('biblioteczkaHTML.xsl')

# Przetw�rz strumienie i utw�rz z nich �r�d�a wej�ciowe.
parsedxml = InputSource.DefaultFactory.fromStream(xml , "biblioteczka.xml")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "biblioteczkaHTML.xsl")

# Utw�rz nowy procesor, do��cz do niego arkusz stylu a nast�pnie przekszta�� XML.
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

# Zapisz wyj�ciowy dokument XML w pliku.
output = open("biblioteczka.html", 'w')
output.write(HTML)
output.close
