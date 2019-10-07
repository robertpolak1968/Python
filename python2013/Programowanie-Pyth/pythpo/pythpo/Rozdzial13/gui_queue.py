#!/usr/bin/env python
"""
gui_queue.py

Ten modu� wykonuje zadania, kt�re pozwalaj� unikn�� problem�w z w�tkami w systemach Linux i Windows.
Inne modu�y mog� go stosowa� bez �adnej dodatkowej wiedzy na temat gtk.
"""

#Kod udost�pniony na licencji Python License dla ksi��ki Beginning Python

import findgtk
import gtk
import random
import socket
import time
from threading import RLock
import timeoutsocket #u�ywane dla set_timeout()

class gui_queue:
    """Budzi w�tek GUI, kt�ry czy�ci i wykonuje zadania z kolejki."""
    def __init__(self,gui,listenport=0):
        """Je�li listenport jest r�wne 0, tworzymy losowy port do nas�uchiwania"""
        self.mylock=RLock()
        self.myqueue=[]
        if listenport==0:
            self.listenport=random.randint(1025,10000)
        else:
            self.listenport=listenport
        print "Lokalna kolejka GUI nas�uchuje na porcie %s"%self.listenport
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", self.listenport))  
        self.listensocket=s
        self.listensocket.listen(300) #nas�uchiwanie aktywno�ci
        #time.sleep(15)
        self.gui=gui
        return
    
    def append(self,command,args):
        """
        Metod� t� mo�e wykona� dowolny w�tek.
        """
        #print "za�o�oenie blokady..."
        self.mylock.acquire()
        self.myqueue.append((command,args))
        #mo�e nie dzia�a� poprawnie na komputerze z firewallem ZoneAlarm 
        #lub przy braku po��czenia sieciowego...
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Niewielki limit czasu budzi w�tek GUI, ale nie powoduje
        #d�ugich przestoj�w, gdy w�tek jest ju� wykonywany.
        #Nale�y pami�ta� o stosowaniu timeoutsocket i jego
        #wcze�niejszym za�adowaniu.
        s.set_timeout(0.01)
        #Obudzenie!
        #print "��czenie z portem %d"%self.listenport
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
        Metoda wywo�ywana tylko przez g��wny w�tek GUI.
        Pami�taj o zwracaniu warto�ci 1.
        """
        #print "Czyszczenie kolejki"
        #cCzy��...nale�y doda� wywo�anie select.
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
        Wywo�anie zwrotne u�ywane przez gui_queue, gdy otrzyma od nas polecenie.
        Polecenie (command) jest ci�giem znak�w.
        Parametr args zawiera list� argument�w polecenia.
        """
        gtk.threads_enter()
        #print "handle_gui_queue"
                
        method = getattr(self, command, None)
        if method:
            apply(method, args)
        else:
            print "Nierozpoznana akcja %s: %s"%(command,args)
        #print "Zako�czenie obs�ugi kolejki GUI"
        gtk.threads_leave()
        return 1
    
    def gui_queue_append(self,command,args):
        self.gui_queue.append(command,args)
        return 1
