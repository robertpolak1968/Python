#!/usr/bin/python
import cgi
import cgitb
import os

cgitb.enable()
form = cgi.FieldStorage()

print 'Content-type: text/html\n'
print '<html>'
print '<body>'
if form.keys():
    verb = os.environ['REQUEST_METHOD']
    print '<p>Oto warto¶ci z formularza otrzymane metod± %s:</p>' % verb
    print '<ul>'
    for field in form.keys():
        valueObject = form[field]
        if isinstance(valueObject, list):
            #Wys³ano wiêcej ni¿ jedn± warto¶æ. Z tego wzglêdu mamy ca³± listê
            #warto¶ci ValueObjects. Metoda getlist() pozwoli nam uzyskaæ warto¶ci
            #tekstowe.
            values = [v.value for v in valueObject]
            if len(values) == 2:
                connector = '" i "' #'"Foo" i "bar"'
            else:
                connector = '" oraz "' #'"Foo", "bar" oraz "baz"'
            value = '", "'.join(values[:-1]) + connector + values[-1]
        else:
            #Nades³ano tylko jedn± warto¶æ. Mamy wiêc tylko jeden obiekt
            #ValueObject. Metoda getfirst() pozwoli bezpo¶rednio pobraæ
            #tekstow± reprezentacjê warto¶ci.
            value = valueObject.value
        print '<li>Dla <var>%s</var> otrzyma³em "%s"</li>' % (field, value)
else:
    print '''<form method="GET" action="%s">

<p>To prosty formularz HTML.</p>

<p><input type="text" name="poleTekstowe" value="Pewien tekst" /><br />
<input type="password" name="poleHasla" value="Has³o" />
<input type="hidden" name="poleUkryte" value="Ukryte pole" /></p>

<p>Pola opcji:  
<input type="checkbox" name="poleOpcji1" checked="checked" /> 1
<input type="checkbox" name="poleOpcji2" selected="selected" /> 2
</p>

<p>Wybierz jeden:<br />
<input type="radio" name="przyciskOpcji" value="1" /> 1<br />
<input type="radio" name="przyciskOpcji" value="2" checked="checked" /> 2<br />
<input type="radio" name="przyciskOpcji" value="3" /> 3<br /></p>

<textarea name="obszarTekstu">Mnóstwo tekstu</textarea>

<p>Wybierz jedn± lub wiêcej warto¶ci: <select name="selection" size="4" multiple="multiple">
<option value="Opcja 1">Opcja 1</option>
<option value="Opcja 2" selected="selected">Opcja 2</option>
<option value="Opcja 3" selected="selected">Opcja 3</option>
<option value="Opcja 4" selected="selected">Opcja 4</option>
</select></p>

<p><input type="Submit" name="przycisk" value="Wy¶lij formularz" />
<p><input type="Submit" name="przycisk" value="Wy¶lij formularz (drugi przycisk)" />

</form>''' % os.environ['SCRIPT_NAME']
 
print '</body>'
print '</html>'
