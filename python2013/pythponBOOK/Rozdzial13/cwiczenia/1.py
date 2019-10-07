#!/usr/bin/env python
import findgtk

import gtk
import gtk.glade

class ex1gui:
    def __init__(self):
        self.wTree = gtk.glade.XML ("cw1.glade", "window1")
        dic={ "on_window1_destroy" : self.quit,
                  "on_button1_clicked" : self.send,
              }
        self.wTree.signal_autoconnect (dic)
        #ustaw okno dziennika
        self.logwindowview=self.wTree.get_widget("textview1")
        self.logwindow=gtk.TextBuffer(None)
        self.logwindowview.set_buffer(self.logwindow)
        return

    def send(self,obj):
        print "wywołano send"
        command=self.wTree.get_widget("entry1").get_text()
        print "Polecenie: %s"%command
        self.log("Wykonuję: "+command,"black")
        import os
        fd=os.popen(command)
        data=fd.read()
        self.log("Wynik: %s"%data,"red")
        
        return

    def log(self,message,color,enter="\n"):
        """
        umieszcza komunikat w obszarze tekstowym i przesuwa obszar na sam dół
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
        return
    
    def quit(self,obj):
        import sys
        gtk.main_quit()
        sys.exit(1)
    
if __name__ == '__main__':
    #wyświetlenie ekranu początkowego
    thegui=ex1gui()
    
    try:
        gtk.threads_init()
    except:
        print "W trakcie kompilacji pyGTK nie były włączone wątki!"
        sys.exit(1)
    gtk.threads_enter()
    gtk.main ()
    gtk.threads_leave()
