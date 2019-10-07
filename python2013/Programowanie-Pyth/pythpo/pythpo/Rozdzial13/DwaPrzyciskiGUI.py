#!/usr/bin/env python
import findgtk
import gtk

class TwoButtonsGUI:
    def __init__(self, msg1="Witaj świecie", msg2="Witaj ponownie"):
        #Utwórz okno i pojekmnik.
        self.window=gtk.Window()
        self.box = gtk.VBox()
        self.window.add(self.box)

        #Utwórz przyciski.
        self.button1 = gtk.Button(msg1)
        self.button2 = gtk.Button(msg2)
        self.box.pack_start(self.button1)
        self.box.pack_start(self.button2)

        #Wyświetla GUI.
        self.button1.show()
        self.button2.show()
        self.box.show()
        self.window.show()

if __name__ == '__main__':    
    TwoButtonsGUI()
    gtk.main()
