#!/usr/bin/python

# Ten skrypt wymaga wcze¶niejszej instalacji pakietu pyXML z witryny:
# http://pyxml.sourceforge.net/

from xml.parsers.xmlproc import xmlval

class docErrorHandler(xmlval.ErrorHandler):
  def warning(self, message):
    print message
  def error(self, message):
    print message
  def fatal(self, message):
    print message

parser = xmlval.XMLValidator()
parser.set_error_handler(docErrorHandler(parser))
parser.parse_resource("biblioteczka.xml")
