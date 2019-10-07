#!/usr/bin/env python
import findgtk
import gtk

class SingleButtonGUI:
    def __init__(self, msg="Witaj świecie"):
        #Utwórz okno a w nim przycisk.
        self.window=gtk.Window()
        self.button=gtk.Button(msg)
        self.window.add(self.button)

        #Wyświetl widgety.
        self.button.show()
        self.window.show()

if __name__ == '__main__':    
    SingleButtonGUI()
    gtk.main()
