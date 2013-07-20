'''
Created on 2012-6-18

@author: jiang
'''
import wx

class myFrame(wx.Frame):
    '''frame class that display a image'''
    def __init__(self, image):
        wx.Frame.__init__(self,None, -1, "title", (250, 250),(400, 300))
        print image
        temp = image.ConvertToBitmap()        
        size = temp.GetWidth(), temp.GetHeight()        
        print type(image)
        self.bmp = wx.StaticBitmap(parent = self, bitmap = temp)
        
        
import sys        
import wx
class mainApp(wx.App):

    
    def OnInit(self):
        image = wx.Image('d:\\pic\\fuck.png', wx.BITMAP_TYPE_PNG)
        print image
        print image.GetWidth(), image.GetHeight()
        
        type(image)
        self.frame = myFrame(image);
        self.frame.Show()
        self.SetTopWindow(self.frame)
       
        return True
    
    
        
if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
