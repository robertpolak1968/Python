#!/usr/bin/python

# move.py

import wx

class Move(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.Move((800, 250))
        
        self.Show(True)


app = wx.App()
Move(None, -1, 'Move')

app.MainLoop()
