#!/usr/bin/env python

# Zastosuj ten plik wraz z plikiem "naglowki.html"

from formatter import AbstractFormatter , DumbWriter
from htmllib import HTMLParser


class HeadingParser(HTMLParser):
  def start_h1(self, tag):
    print "Znalaz³em H1"

writer = DumbWriter()
formatter = AbstractFormatter (writer)
parser=HeadingParser(formatter)
parser.feed(open('naglownik.html').read())
parser.close()
print "Koniec analizy"
