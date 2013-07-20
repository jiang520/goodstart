# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Mp3InfoPicker
###########################################################################

class Mp3InfoPickerFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Mp3 infor picker", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"filePath:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.m_staticText4.Wrap( -1 )
        bSizer10.Add( self.m_staticText4, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
        
        self.m_filePicker = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
        bSizer10.Add( self.m_filePicker, 1, wx.ALL, 5 )
        
        self.m_btnGetInfo = wx.Button( self.m_panel5, wx.ID_ANY, u"GetInfo", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_btnGetInfo, 0, wx.ALL, 5 )
        
        bSizer12.Add( bSizer10, 0, wx.EXPAND, 5 )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl3 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
        bSizer14.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )
        
        self.m_panel5.SetSizer( bSizer12 )
        self.m_panel5.Layout()
        bSizer12.Fit( self.m_panel5 )
        bSizer9.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( bSizer9 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnGetInfo.Bind( wx.EVT_BUTTON, self.OnBtnGetInfo )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnBtnGetInfo( self, event ):
        from  Mp3InfoPicker import Mp3InfoPicker
        picker = Mp3InfoPicker("d://test.mp3")
        str = "author:%s %s %s"%(picker.GetAuthor(), picker.GetName(), picker.GetYear())
        self.m_textCtrl3.SetValue(str)
        event.Skip()
    
if __name__=='__main__':
    app = wx.App()
    frame = Mp3InfoPickerFrame(None)
    frame.Show(True)
    app.MainLoop()
