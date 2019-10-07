#!/usr/bin/env python
import time
import findgtk
import gtk.glade

class PyRAPGUI:
    def __init__(self):
        self.wTree = gtk.glade.XML("pyrap.glade", "window1")                

if __name__ == '__main__':    
    PyRAPGUI()
    try:
        gtk.threads_init()
    except:
        print "W trakcie kompilacji pyGTK nie były włączone wątki!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
