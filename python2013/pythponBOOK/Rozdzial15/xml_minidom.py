#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom

def printLibrary(library):
  books = myLibrary.getElementsByTagName("book")
  for book in books:
    print "*****Ksi��ka*****"
    print "Tytu�: %s" % book.getElementsByTagName("title")[0].childNodes[0].data
    for author in book.getElementsByTagName("author"):
      print "Autor: %s"  % author.childNodes[0].data


# Otw�rz plik XML i dokonaj jego konwersji do DOM.
myDoc = parse('biblioteczka.xml')
myLibrary = myDoc.getElementsByTagName("library")[0]

# Pobierz wszystkie elementy book.
books = myLibrary.getElementsByTagName("book")

# Wy�wietl tytu�y i autor�w ksi��ek.
printLibrary(myLibrary)

# Wstaw now� ksi��k�.
newBook = myDoc.createElement("book")
newBookTitle = myDoc.createElement("title")
titleText = myDoc.createTextNode("Python. Receptury")
newBookTitle.appendChild(titleText)
newBook.appendChild(newBookTitle)

newBookAuthor = myDoc.createElement("author")
authorName = myDoc.createTextNode("Alex Martelli i inni")
newBookAuthor.appendChild(authorName)
newBook.appendChild(newBookAuthor)

myLibrary.appendChild(newBook)

print "Dodano now� ksi��k�!"
printLibrary(myLibrary)

# Usu� ksi��k�.
# Znajd� ksi��k�.
for book in myLibrary.getElementsByTagName("book"):
  for author in book.getElementsByTagName("author"):
    if author.childNodes[0].data.find("Pratchett") != -1:
      removedBook= myLibrary.removeChild(book)
      removedBook.unlink()

print "Usuni�to ksi��k�."
printLibrary(myLibrary)

# Zapisz dane do pliku biblioteczki.
lib = open("biblioteczka.xml", 'w') 
lib.write(myDoc.toprettyxml("  "))
lib.close()
