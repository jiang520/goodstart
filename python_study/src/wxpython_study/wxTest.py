'''
Created on 2012-6-14

@author: jiang
'''
import wx
import os
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, 'helloworld',size = (500, 500) )
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        txt = wx.StaticText(panel, -1, 'helloworld')
        txt.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        sizer.Add(txt, 0, wx.TOP|wx.LEFT, 100)
        self.Center()
        menubar = wx.MenuBar()
        menu = wx.Menu() 
        menu.Append(1, 'open', 'open a file')
        menu.Append(2, 'close', 'close and reset')       
        menubar.Append(menu, u'file')
        
        menu2 = wx.Menu()
        menu2.Append(1, 'delete','delete line')
        menu2.Append(2,'copy', 'copy something')
        menu2.Append(-31, 'pause', '--')
        
        menubar.Append(menu2, u'edit')
        
        
        self.SetMenuBar(menubar)
          
class MyApp(wx.App):
    def __init__(self, redirect = True, filename = None, useBestVisual = True, clearSigInt = True):
        wx.App.__init__(self,redirect, filename, useBestVisual, clearSigInt)    
    def OnInit(self):
        print 'on init'
        os.sys.stdout.write('this is a string out to stdout')
        self.frame = MyFrame(None)
       #msg = wx.MessageDialog(None, 'are you sure to delete', 'del', wx.YES_NO|wx.ICON_WARNING)
       
        return True
    
    def OnExit(self):
        msg = wx.MessageDialog()
        print 'exit'
        import time
        time.sleep(2)    
     
        
if __name__ == "__main__":
    
    app = wx.App()
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()
    



    