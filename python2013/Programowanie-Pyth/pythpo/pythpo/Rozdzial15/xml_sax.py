#!/usr/bin/python

from xml.sax         import make_parser
from xml.sax.handler import ContentHandler

#pocz¹tek bookHandler
class bookHandler(ContentHandler):
  inAuthor = False
  inTitle = False

  def startElement(self, name, attributes):
    if name == "book":
      print "*****Ksi¹¿ka*****"

    if name == "title":
      self.inTitle = True
      print "Tytu³: ",

    if name == "author":
      self.inAuthor = True
      print "Autor: ",

  def endElement(self, name):
    if name == "title":
      self.inTitle = False
    if name == "author":
      self.inAuthor = False

  def characters(self, content):
    if self.inTitle or self.inAuthor:
      print content
#koniec bookHandler

parser  = make_parser()
parser.setContentHandler(bookHandler())
parser.parse("biblioteczka.xml")
