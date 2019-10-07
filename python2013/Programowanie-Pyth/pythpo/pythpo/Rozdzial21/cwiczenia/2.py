#!/usr/bin/python
import cgi
import cgitb
import os
from WishListBargainFinder import BargainFinder, getWishList
cgitb.enable()

SUBSCRIPTION_ID = '[Wstaw identyfikator subskrypcji.]'

form = cgi.FieldStorage()
wishListID = form.getfirst('wishlist', '')

args = {'title' : 'Znajdowanie okazji na podstwie listy życzeń Amazon',
        'action' : os.environ['SCRIPT_NAME'],
        'wishListID' : wishListID}

print 'Content-type: text/html\n'
print '''<html><head><title>%(title)s</title></head>
<form method="get" action="%(action)s">
<h1>%(title)s</h1>
Wpisz identyfikator listy życzeń:
<input name="wishlist" length="13" maxlength="13" value="%(wishListID)s" />
<input type="submit" value="Znajdź okazje"/>
</form>''' % args

if wishListID:
    print '<pre>'
    BargainFinder().printBargains(getWishList(SUBSCRIPTION_ID, wishListID))
    print '</pre>'
    
    print '</body></html>'
