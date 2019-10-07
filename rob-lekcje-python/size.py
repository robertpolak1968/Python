#!/usr/bin/python

# size.py

import wx

class Size(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 250))

        self.Show(True)


app = wx.App()
Size(None, -1, 'Size definition')
app.MainLoop()
