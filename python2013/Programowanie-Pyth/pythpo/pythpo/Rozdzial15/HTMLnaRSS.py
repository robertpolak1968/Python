#!/usr/bin/env python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor
from xml.parsers.xmlproc import xmlval

class docErrorHandler(xmlval.ErrorHandler):
  def warning(self, message):
    print "Ostrze¿enie: " + message
  def error(self, message):
    print "B³±d: " + message
  def fatal(self, message):
    print "B³±d krytyczny: " + message

# Otwórz pliki HTML i XSTL jako strumienie.
html = open('mojblog.html')
xsl = open('HTMLnaRSS.xsl')

# Przetwórz strumienie i utwórz z nich Ÿród³a wejœciowe.
parsedxml = InputSource.DefaultFactory.fromStream(html, "mojblog.html")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "HTMLnaRSS.xsl")

# Utwórz nowy procesor, do³¹cz do niego arkusz stylu a nastêpnie przekszta³æ XML.
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

# Zapisz wyjœciowy dokument RSS w pliku.
output = open("kanalRSS.xml", 'w')
output.write(HTML)
output.close

# Dokonaj walidacji kana³u RSS.
parser=xmlval.XMLValidator()
parser.set_error_handler(docErrorHandler(parser))
parser.parse_resource("kanalRSS.xml")
