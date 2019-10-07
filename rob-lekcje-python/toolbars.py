#!/usr/bin/python

# toolbars.py

import wx

class Toolbars(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 200))

        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self, -1)
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('icons/exit.png'))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('icons/exit.png'))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('icons/exit.png'))
        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self, -1)
        toolbar2.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('icons/exit.png'))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)

        self.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def OnExit(self, event):
        self.Close()


app = wx.App()
Toolbars(None, -1, 'toolbars')
app.MainLoop()
