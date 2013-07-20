'''
Created on 2012-6-19

@author: jiang
'''
import wx
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "this is a dialog for eidt",size=(388, 288))
        panel = wx.Panel(self, -1)
        
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        st = wx.StaticText(panel, -1, "pos:", pos=(10, 20))
        self.posCtrl= wx.TextCtrl(panel, -1, "", pos=(40, 50))
      

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s,%s"%(pos.x, pos.y))
        
        
if __name__=="__main__":
    app = wx.PySimpleApp(False)
    frame = myFrame()
    frame.Show(True)
    app.MainLoop()
        