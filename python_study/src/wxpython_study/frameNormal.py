'''
Created on 2012-6-22

@author: jiang
'''

import wx
import sys

class ToolBarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'toolbar', size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('white')
        statusbar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        img = wx.Image(name="d:\\pic\\8.bmp", type=wx.BITMAP_TYPE_BMP)
        img.Resize((50, 20), (0,0))
        temp = img.ConvertToBitmap()
        
        toolbar.AddSimpleTool(wx.NewId(), temp, "new", "long help for new")
      
        toolbar.Realize()
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menubar.Append(menu1, "fuck")
        menu2 = wx.Menu()
        menubar.Append(menu2, "cao")
        menu2.Insert(0,wx.NewId(), "C", "copy in status bar")
        self.SetMenuBar(menubar)


        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolBarFrame(None, id=-1)
    frame.Show()
    app.MainLoop()