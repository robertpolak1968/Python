#!/usr/bin/python

# checkmenuitem.py

import wx

ID_STAT = 1
ID_TOOL = 2

class CheckMenuItem(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 250))

        menubar = wx.MenuBar()
        file = wx.Menu()
        view = wx.Menu()
        self.shst = view.Append(ID_STAT, 'Show statubar', 'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = view.Append(ID_TOOL, 'Show toolbar', 'Show Toolbar', kind=wx.ITEM_CHECK)
        view.Check(ID_STAT, True)
        view.Check(ID_TOOL, True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, id=ID_STAT)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, id=ID_TOOL)

        menubar.Append(file, '&File')
        menubar.Append(view, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(3, '', wx.Bitmap('icons/quit.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.Centre()
        self.Show(True)

    def ToggleStatusBar(self, event):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, event):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

app = wx.App()
CheckMenuItem(None, -1, 'check menu item')
app.MainLoop()
