#!/usr/bin/python

# submenu.py

import wx

ID_QUIT = 1

class SubmenuExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 250))

        menubar = wx.MenuBar()

        file = wx.Menu()
        file.Append(-1, '&New')
        file.Append(-1, '&Open')
        file.Append(-1, '&Save')
        file.AppendSeparator()

        imp = wx.Menu()
        imp.Append(-1, 'Import newsfeed list...')
        imp.Append(-1, 'Import bookmarks...')
        imp.Append(-1, 'Import mail...')

        file.AppendMenu(-1, 'I&mport', imp)

        quit = wx.MenuItem(file, ID_QUIT, '&Quit\tCtrl+W')
        quit.SetBitmap(wx.Bitmap('icons/exit.png'))
        file.AppendItem(quit)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=ID_QUIT)

        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        self.Centre()
        self.Show(True)

    def OnQuit(self, event):
        self.Close()

app = wx.App()
SubmenuExample(None, -1, 'Submenu')
app.MainLoop()
