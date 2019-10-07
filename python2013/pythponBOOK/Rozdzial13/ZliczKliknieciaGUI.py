#!/usr/bin/env python
import findgtk        
import gtk,gtk.glade
import pygtk
pygtk.require("2.0")
import gtk

class ClickCountGUI:
    "Kliknięcie przycisku inkrementuje licznik."
    
    CLICK_COUNT = 'Licznik kliknięć: %d'

    def __init__(self):
        "Utwórz okno i przycisk licznika."
        self.window=gtk.Window()        
        self.button=gtk.Button(self.CLICK_COUNT % 0)
        self.button.timesClicked = 0        
        self.window.add(self.button)

        #Wywołaj metodę buttonClicked w momencie kliknięcia przycisku.
        self.button.connect("clicked", self.buttonClicked)

        #Wyłącz program po zamknięciu okna.
        self.window.connect("destroy", self.destroy)

        #Wyświetl GUI.
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
    gtk.main()
