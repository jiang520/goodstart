
import wx
import sys
from wx import Frame
from ctypes.wintypes import SIZE

class myFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent, 22, 'helo ', (0,0), 
                       wx.Size(300, 200))        
        self.SetTitle('fuck you ')
        self.SetSize(wx.Size(33, 99))
        panel = wx.Panel(self)
        sizer = wx.Sizer()
        self.Centre()
        
        
app = wx.App(0)
frame = myFrame(None)
frame.Show()
app.MainLoop()
wx.Sleep(330)


