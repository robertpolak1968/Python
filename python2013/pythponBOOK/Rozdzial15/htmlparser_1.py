#!/usr/bin/env python

# Zastosuj ten plik wraz z plikiem "naglowki.html"

from HTMLParser import HTMLParser

class HeadingParser(HTMLParser):
  inHeading = False

  def handle_starttag(self, tag, attrs):
    if tag == "h1":
      self.inHeading = True
      print "Znalaz³em nag³ówek H1"

  def handle_data(self, data):
    if self.inHeading:
      print data

  def handle_endtag(self, tag):
    if tag =="h1":
      self.inHeading = False


hParser = HeadingParser()
file = open("naglowki.html", "r")
html = file.read()
file.close()
hParser.feed(html)
