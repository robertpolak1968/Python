#!/usr/bin/env python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor
from xml.parsers.xmlproc import xmlval

class docErrorHandler(xmlval.ErrorHandler):
  def warning(self, message):
    print "Ostrze�enie: " + message
  def error(self, message):
    print "B��d: " + message
  def fatal(self, message):
    print "B��d krytyczny: " + message

# Otw�rz pliki HTML i XSTL jako strumienie.
html = open('mojblog.html')
xsl = open('HTMLnaRSS.xsl')

# Przetw�rz strumienie i utw�rz z nich �r�d�a wej�ciowe.
parsedxml = InputSource.DefaultFactory.fromStream(html, "mojblog.html")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "HTMLnaRSS.xsl")

# Utw�rz nowy procesor, do��cz do niego arkusz stylu a nast�pnie przekszta�� XML.
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

# Zapisz wyj�ciowy dokument RSS w pliku.
output = open("kanalRSS.xml", 'w')
output.write(HTML)
output.close

# Dokonaj walidacji kana�u RSS.
parser=xmlval.XMLValidator()
parser.set_error_handler(docErrorHandler(parser))
parser.parse_resource("kanalRSS.xml")
