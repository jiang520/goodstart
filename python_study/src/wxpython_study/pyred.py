'''
Created on 2012-6-22

@author: jiang
'''
import wx
import sys
class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print "frame init"
        wx.Frame.__init__(self, parent, id, title)
        
class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print "app iniit"
        wx.App.__init__(self, redirect, filename)
    def OnInit(self):
        print "Oninit"
        self.frame = Frame(parent=None, id = -1, title="strart")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print sys.stderr, "a prentedn error message"
        return True
    def OnExit(self):
        print "OnExit"

if __name__=="__main__":
    app  = App(redirect=False)
    print "befor Mainloop"
    app.MainLoop()
    print "after MainLoop"
    