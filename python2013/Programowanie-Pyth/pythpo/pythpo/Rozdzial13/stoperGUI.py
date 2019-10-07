#!/usr/bin/env python
import time
from threading import Thread

import findgtk
import gtk
from gui_queue import Queued

class CountUpGUI(Queued):
    """Dokonuje zliczania w osobnym wątku. W celach bezpieczeństwa
    pozostałe wątku umieszczają wywołania threads_enter() i threads_leave() wokół
    całego kodu GTK."""

    START = "Kliknij mnie, by rozpocząć zliczanie."
    STOP = "Zliczyłem do %s (kliknij, by zatrzymać)."

    def __init__(self):
        Queued.__init__(self)
        self.window=gtk.Window()        
        self.button=gtk.Button(self.START)
        self.button.timesClicked = 0        
        self.window.add(self.button)
        self.thread = None


        #Wywołaj metodę toggleCount w momencie kliknięcia przycisku.
        self.button.connect("clicked", self.toggleCount)

        #Zamknięcie okna wyłącza program.
        self.window.connect("destroy", self.destroy)

        #Wyświetl GUI.
        self.button.show()
        self.window.show()

    def destroy(self, window):
        "Zamknij okno i wyłącz program."
        window.hide()
        gtk.main_quit()

    def toggleCount(self, button):
        if self.thread and self.thread.doCount:
            #Zatrzymaj odliczanie.
            self.thread.doCount = False
        else:
            #Rozpocznij odliczanie.
            self.thread = self.CountingThread(self, self.button)
            self.thread.start()

    def incrementCount(self, button, count):
        button.set_label(self.STOP % count)

    def resetCount(self, button):
        button.set_label(self.START)

    class CountingThread(Thread):
        """Inkrementuje licznik co sekundę i odpowiednio aktualizuje
        etykietę przycisku. Aktualizacja odbywa się przez umieszczenie
        zdarzenia w kolejce GUI, a nie przez bezpośrednią modyfikację
        przycisku."""
        def __init__(self, gui, button):
            self.gui = gui
            Thread.__init__(self)
            self.button = button
            self.doCount = False
            self.count = 0
            self.setDaemon(True)
            
        def run(self):
            self.doCount = True
            while self.doCount:
                self.gui.gui_queue_append("incrementCount",
                                          [self.button, self.count])
                self.count += 1
                time.sleep(1)
            self.gui.gui_queue_append("resetCount", [self.button])
            self.count = 0

if __name__ == '__main__':    
    CountUpGUI()
    try:
        gtk.threads_init()
    except:
        print "W trakcie kompilacji nie była włączona obsługa wątków pyGTK!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()
