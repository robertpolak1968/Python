#!/usr/bin/python

# simpletoolbar.py

import wx

class SimpleToolbar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('icons/exit.png')
        toolbar.Realize()                             

        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)

        self.Centre()
        self.Show(True)

    def OnExit(self, event):
        self.Close()


app = wx.App()
SimpleToolbar(None, -1, 'simple toolbar')
app.MainLoop()
