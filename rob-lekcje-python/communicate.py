#!/usr/bin/python

# communicate.py

import wx


class LeftPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)

        self.text = parent.GetParent().rightPanel.text
        #self.text = parent.GetParent().downPanel.text
       
        button1 = wx.Button(self, -1, '+', (10, 10))
        button2 = wx.Button(self, -1, '-', (10, 100))

        self.Bind(wx.EVT_BUTTON, self.OnPlus, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnMinus, id=button2.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnPlusDown, id=button1.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnMinusDown, id=button1.GetId())
 

    def OnPlus(self, event):
        value = int(self.text.GetLabel())
        value = value + 1
        self.text.SetLabel(str(value))
      

    def OnMinus(self, event):
        value = int(self.text.GetLabel())
        value = value - 1
        self.text.SetLabel(str(value))
     

    def OnPlusDown(self, event):
        pres = int(self.text.GetLabel())
        pres= pres + 1
        
        self1.text.SetLabel(str(pres))

    def OnMinusDown(self, event):
        pres = int(self.text.GetLabel())
        pres=pres + 1
        self.text.SetLabel(str(pres))

class RightPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.text = wx.StaticText(self, -1, '0', (40, 60))

class DownPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.text = wx.StaticText(self, -1, '0', (40, 60))



class Communicate(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 400))

        panel = wx.Panel(self, -1)
        self.rightPanel = RightPanel(panel, -1)
        self.downPanel = DownPanel(panel, -1)  

        leftPanel = LeftPanel(panel, -1)

        hbox = wx.BoxSizer()
        hbox.Add(leftPanel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.rightPanel, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.downPanel, 1, wx.EXPAND | wx.ALL, 5)


        panel.SetSizer(hbox) 
        self.Centre()
        self.Show(True)

app = wx.App()
Communicate(None, -1, 'widgets communicate')
app.MainLoop()
