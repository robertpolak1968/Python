#!/usr/bin/env python
import time
import findgtk
import gtk

from gui_queue import Queued

class ClickCountGUI(Queued):
    "Kliknięcie przycisku inkrementuje licznik."

    CLICK_COUNT = 'Licznik kliknięć: %d'

    def __init__(self):
        Queued.__init__(self)
        self.window=gtk.Window()        
        self.button=gtk.Button(self.CLICK_COUNT % 0)
        self.button.timesClicked = 0        
        self.window.add(self.button)

        #Wywołaj metodę toggleCount po kliknięciu przycisku.
        self.button.connect("clicked",
                            lambda(x): self.gui_queue_append("buttonClicked",
                                                             [x]))

        #Wyłącz program po zamknięciu okna.
        self.window.connect("destroy",
                            lambda(x): self.gui_queue_append("destroy",
                                                             [x]))

        #Wyświetl interfejs.
        self.button.show()
        self.window.show()

    def buttonClicked(self, button):
        "Kliknięto przycisk, zwiększ licznik."
        button.timesClicked += 1
        button.set_label(self.CLICK_COUNT % button.timesClicked)

    def destroy(self, window):
        "Zamknij okno i wyłącz program."
        window.hide()
        gtk.main_quit()

if __name__ == '__main__':    
    ClickCountGUI()
    try:
        gtk.threads_init()
    except:
        print "W trakcie kompilacji pyGTK nie włączono wątków!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
