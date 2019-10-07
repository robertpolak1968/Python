#!/usr/bin/env python
"""
gui_queue.py

Ten modu³ wykonuje zadania, które pozwalaj¹ unikn¹æ problemów z w¹tkami w systemach Linux i Windows.
Inne modu³y mog¹ go stosowaæ bez ¿adnej dodatkowej wiedzy na temat gtk.
"""

#Kod udostêpniony na licencji Python License dla ksi¹¿ki Beginning Python

import findgtk
import gtk
import random
import socket
import time
from threading import RLock
import timeoutsocket #u¿ywane dla set_timeout()

class gui_queue:
    """Budzi w¹tek GUI, który czyœci i wykonuje zadania z kolejki."""
    def __init__(self,gui,listenport=0):
        """Jeœli listenport jest równe 0, tworzymy losowy port do nas³uchiwania"""
        self.mylock=RLock()
        self.myqueue=[]
        if listenport==0:
            self.listenport=random.randint(1025,10000)
        else:
            self.listenport=listenport
        print "Lokalna kolejka GUI nas³uchuje na porcie %s"%self.listenport
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", self.listenport))  
        self.listensocket=s
        self.listensocket.listen(300) #nas³uchiwanie aktywnoœci
        #time.sleep(15)
        self.gui=gui
        return
    
    def append(self,command,args):
        """
        Metodê tê mo¿e wykonaæ dowolny w¹tek.
        """
        #print "za³o¿oenie blokady..."
        self.mylock.acquire()
        self.myqueue.append((command,args))
        #mo¿e nie dzia³aæ poprawnie na komputerze z firewallem ZoneAlarm 
        #lub przy braku po³¹czenia sieciowego...
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Niewielki limit czasu budzi w¹tek GUI, ale nie powoduje
        #d³ugich przestojów, gdy w¹tek jest ju¿ wykonywany.
        #Nale¿y pamiêtaæ o stosowaniu timeoutsocket i jego
        #wczeœniejszym za³adowaniu.
        s.set_timeout(0.01)
        #Obudzenie!
        #print "£¹czenie z portem %d"%self.listenport
        try:
            s=s.connect(("localhost",self.listenport))
        except:
            #ignorowanie limitu czasu
            pass
        #print "Zwolnienie blokady"
        self.mylock.release()
        return

    def clearqueue(self, socket, x):
        """
        Metoda wywo³ywana tylko przez g³ówny w¹tek GUI.
        Pamiêtaj o zwracaniu wartoœci 1.
        """
        #print "Czyszczenie kolejki"
        #cCzyœæ...nale¿y dodaæ wywo³anie select.
        newconn,addr=self.listensocket.accept()
        for i in self.myqueue:
            (command,args)=i
            self.gui.handle_gui_queue(command,args)
        self.myqueue=[]
        return 1

class Queued:

    def __init__(self):
        self.gui_queue=gui_queue(self) #nowakolejka GUI
        #Dla starszych pyGTK:
        #gtk.input_add(self.gui_queue.listensocket,
        #              gtk.gdk.INPUT_READ, self.gui_queue.clearqueue)
        #
        #Dla nowszych pyGTK (2.6):
        import gobject
        gobject.io_add_watch(self.gui_queue.listensocket, gobject.IO_IN,
                             self.gui_queue.clearqueue)

    def handle_gui_queue(self, command, args):
        """
        Wywo³anie zwrotne u¿ywane przez gui_queue, gdy otrzyma od nas polecenie.
        Polecenie (command) jest ci¹giem znaków.
        Parametr args zawiera listê argumentów polecenia.
        """
        gtk.threads_enter()
        #print "handle_gui_queue"
                
        method = getattr(self, command, None)
        if method:
            apply(method, args)
        else:
            print "Nierozpoznana akcja %s: %s"%(command,args)
        #print "Zakoñczenie obs³ugi kolejki GUI"
        gtk.threads_leave()
        return 1
    
    def gui_queue_append(self,command,args):
        self.gui_queue.append(command,args)
        return 1
