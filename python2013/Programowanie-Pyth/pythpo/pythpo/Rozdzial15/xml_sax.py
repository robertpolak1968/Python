#!/usr/bin/python

from xml.sax         import make_parser
from xml.sax.handler import ContentHandler

#pocz�tek bookHandler
class bookHandler(ContentHandler):
  inAuthor = False
  inTitle = False

  def startElement(self, name, attributes):
    if name == "book":
      print "*****Ksi��ka*****"

    if name == "title":
      self.inTitle = True
      print "Tytu�: ",

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
