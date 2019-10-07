#!/usr/bin/env python
import findgtk
import gtk
import time

class PyRAPGUI:
    def __init__(self):
        self.wTree = gtk.glade.XML ("pyrap.glade", "window1")
        dic={ "on_window1_destroy" : self.quit,
              "on_button1_clicked" : self.send,
              }
        self.wTree.signal_autoconnect (dic)
        self.username="Jan"
        #Ustaw obszar tekstowy, by działał jako dziennik.
        self.logwindowview=self.wTree.get_widget("textview1")
        self.logwindow=gtk.TextBuffer(None)
        self.logwindowview.set_buffer(self.logwindow)
        return

    #Obsługa sygnałów.
    def quit(self,obj):
        "Obsługuje sygnał 'destroy' okna."
        gtk.main_quit()
        sys.exit(1)
        
    def send(self,obj):
        "Obsługuje sygnał 'clicked' przycisku."
        message=self.wTree.get_widget("entry1").get_text()
        print "Wiadomość=%s" % message
        self.log(self.username + ": " + message, "black")

    def log(self,message,color,enter="\n"):
        """
        Metoda pomocnicza dla kodu obsługi zdarzenia kliknięcia: 
        umieszcza komunikat w obszarze tekstowym i przesuwa obszar na sam dół.
        """
        message=message+enter
        
        buffer = self.logwindow
        iter = buffer.get_end_iter()
        #obsługa różnych wersji GTK
        if color != "black":
            tag = buffer.create_tag()
            tag.set_property("foreground", color)
            self.logwindow.insert_with_tags(buffer.get_end_iter(), message, tag)	
        else:
            self.logwindow.insert(iter, message)
        #gtk.FALSE i gtk.TRUE w starszych pyGTK
        mark = buffer.create_mark("end", buffer.get_end_iter(), False)
        self.logwindowview.scroll_to_mark(mark,0.05,True,0.0,1.0)
        #print "Koniec funkcji log"

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
