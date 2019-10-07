#!/usr/bin/env python
import findgtk
import gtk
import gtk.glade
import gui_queue
import threading
import os
import gobject

class commandRunner(threading.Thread):
    def __init__(self,command,gui):
        threading.Thread.__init__(self)
        self.command=command
        self.gui=gui
        return

    def run(self):
        fd=os.popen(self.command)
        data="A"
        while data!="":
            data=fd.readline()
            self.gui.gui_queue_append("log",[data,"red"])
        return
    
class ex2gui:
    def __init__(self):
        #używamy tego samego interfejsu, co poprzedni program!
        self.wTree = gtk.glade.XML ("cw1.glade", "window1")
        dic={ "on_window1_destroy" : self.quit,
                  "on_button1_clicked" : self.send,
              }
        self.wTree.signal_autoconnect (dic)
        #ustaw okno dziennika
        self.logwindowview=self.wTree.get_widget("textview1")
        self.logwindow=gtk.TextBuffer(None)
        self.logwindowview.set_buffer(self.logwindow)
        self.gui_queue=gui_queue.gui_queue(self)
        gobject.io_add_watch(self.gui_queue.listensocket,gobject.IO_IN,self.clearqueue)
        return

    def send(self,obj):
        print "wywołano send"
        command=self.wTree.get_widget("entry1").get_text()
        print "Polecenie: %s"%command
        self.log("Wykonuję: "+command,"black")
        cR=commandRunner(command,self)
        cR.start() #uruchom nowy wątek!
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
    
    def clearqueue(self,source,condition):
        """Funkcja zwrotna dla zdarzeń."""
        self.gui_queue.clearqueue(source, condition)
        return 1

    def handle_gui_queue(self,command, args):
        """
        Wywołanie zwrotne używane przez gui_queue, gdy otrzyma od nas polecenie.
        command to tekst
        args to lista argumentów polecenia
        """
        gtk.threads_enter()
        #print "handle_gui_queue"
                
        if command=="log":
            text=args[0]
            color=args[1]
            self.log(text,color=color)
        else:
            print "Nierozpoznana akcja %s: %s"%(command,args)
        #print "Zakończona obsługa kolejki"
        gtk.threads_leave()
        return 1
    
    def gui_queue_append(self,command,args):
        self.gui_queue.append(command,args)
        return 1
    
if __name__ == '__main__':
    #wyświetlenie ekranu powitalnego
    thegui=ex2gui()
    
    try:
        gtk.threads_init()
    except:
        print "W trakcie kompilacji pyGTK nie były włączone wątki!"
        sys.exit(1)
    gtk.threads_enter()
    gtk.main ()
    gtk.threads_leave()
