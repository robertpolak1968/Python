#-*- coding: utf-8 -*-
import wx
 
# Kilka klas które wykorzystamy w polach notatnika
 
class Prostokat(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj dlugsc boku a = ", (10,30))
        wx.StaticText(self, -1, "Podaj dlugosc boku b = ", (10,50))
        self.a = wx.TextCtrl(self, -1,'',(150,27))
        self.b = wx.TextCtrl(self, -1,'',(150,50))
        wx.Button(self, -1, "Oblicz",(150,90))
        wx.EVT_BUTTON(self, -1, self.Poleprost)
        self.w = wx.StaticText(self, -1, '', (80,140))
    def Poleprost(self, event):
        aa = float(self.a.GetValue())
        bb = float(self.b.GetValue())
        wyn = str(aa*bb)
        self.w.SetLabel("Pole prostokata wynosi: "+wyn)
 
class Trojkat(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj dlugosc podstawy", (10,30))
        wx.StaticText(self, -1, "Podaj wysokosc", (10,50)) 
        self.p = wx.TextCtrl(self, -1,'',(150,27))
        self.h = wx.TextCtrl(self, -1,'',(150,50))
        wx.Button(self, -1, "Oblicz",(150,90))
        wx.EVT_BUTTON(self, -1, self.Poletrojkat)
        self.w = wx.StaticText(self, -1, '', (80,140))
    def Poletrojkat(self, event):
        aa = float(self.p.GetValue())
        bb = float(self.h.GetValue())
        wyn = str(aa*bb/2)
        self.w.SetLabel("Pole prostokata wynosi: "+wyn)
 
class Kolo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj...", (40,60))
 
class Trapez(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj...", (40,60))
 
class Rownoleglobok(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj...", (40,60))
 
class Stozek(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj...", (40,60))
 
class Potega(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj", (40,60))
 
class Potega(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "Podaj...", (40,60))
 
class Program(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Oblicznie pol figur geometrycznych")
 
        # Tutaj tworzymy panel i notatnik na panelu
        p = wx.Panel(self)
        nb = wx.Notebook(p)
 
        # Tworzymy zakladki
        zakladka1 = Prostokat(nb)
        zakladka2 = Trojkat(nb)
        zakladka3 = Kolo(nb)
        zakladka4 = Trapez(nb)
        zakladka5 = Rownoleglobok(nb)
        zakladka6 = Stozek(nb)
        zakladka7 = Potega(nb)
 
        # dodajemy zakladki do notatnika wraz z nazw? 
        nb.AddPage(zakladka1, "Prostok?t/Kwadrat")
        nb.AddPage(zakladka2, "Trojkat")
        nb.AddPage(zakladka3, "Kolo")
        nb.AddPage(zakladka4, "Trapez")
        nb.AddPage(zakladka5, "Rownoleglobok")
        nb.AddPage(zakladka6, "Stozek")
        nb.AddPage(zakladka7, "Potega")
 
        # opisanie ulozenia zakladek
        uklad = wx.BoxSizer()
        uklad.Add(nb, 1, wx.EXPAND)
        p.SetSizer(uklad)
 
if __name__ == "__main__":
    app = wx.App()
    Program().Show()
    app.MainLoop()

