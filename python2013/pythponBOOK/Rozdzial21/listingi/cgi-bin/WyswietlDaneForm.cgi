#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
textField = form.getfirst("poleTekstowe")
radioButton = form.getfirst("przyciskOpcji")
submitButton = form.getfirst("przycisk")

print 'Content-type: text/html\n'
print '<html>'
print '<body>'
print '<p>Oto warto�ci uzyskane z formularza:</p>'
print '<ul>'
print '<li>W polu tekstowym zosta� wpisany tekst "%s".</li>' % textField
print '<li>Wybrana zosta�a opcja numer "%s".' % radioButton
print '<li>Klikni�to przycisk o nazwie "%s".' % submitButton
print '</ul>'
print '</body>'
print '</html>'
