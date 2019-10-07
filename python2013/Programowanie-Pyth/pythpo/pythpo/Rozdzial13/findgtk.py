#!/usr/bin/env python
"""
findgtk.py - Znajduje biblioteki pyGTK niezale¿nie od ich po³o¿enia.
"""
import os
import sys
sys.path.append("/usr/local/lib/python2.3/site-packages/")

def try_import():
    import sys
    """Próbuje wczytaæ gtk, w przypadku sukcesu zwraca 1."""
    #print "APróba wczytania gtk...Path=%s"%sys.path
    # Wymagana wersja: 2.0.
    try:
        import pygtk
        pygtk.require("2.0")
    except:
        print "Nie znaleziono pyGTK. Do poprawnego dzia³ania wymaga GTK2."
        print "Czy wykona³eœ wczeœniej \"export PYTHONPATH=/usr/local/lib/python2.2/site-packages/\"?"
        print "Byæ mo¿e masz GTK2, ale nie pyGTK, wiêc kontynuujê poszukiwania."
        
        
    try:
        import gtk,gtk.glade
        import atk,pango #for py2exe
        import gobject
    except:
        import traceback,sys
        traceback.print_exc(file=sys.stdout)
        print "Niestety wygl¹da na to, ¿e brakuje instalacji GTK2  - próbowa³em importowaæ"
        print "gtk, gtk.glade i gobject - bez rezultatu."
     
        return 0
    return 1

if not try_import():
    site_packages=0
    #for k in sys.path:
    #    if k.count("site-packages"):
    #        print "znaleziono œcie¿kê site-packages: %s\n"%k
    #        site_packages=1
    if site_packages == 0:
        from stat import *
        #print "brak œcie¿ki site-packages, szukam...\n"
        check_lib = [ "/usr/lib/python2.2/site-packages/",
                        "/usr/local/lib/python2.2/site-packages/",
                        "/usr/local/lib/python2.3/site-packages/" ]
        for k in check_lib:
            try:
                path=os.path.join(k,"pygtk.py")
                #print "Path=%s"%path
                if open(path)!=None:
                    #print "dodajê", k
                    sys.path=[k]+sys.path
                    if try_import():
                        break
            except:
                pass
    if not try_import():
        sys.exit(0)
