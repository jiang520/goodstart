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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = unicode("空行去除器"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 500,300 ), wx.DefaultSize )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText.Wrap( -1 )
        bSizer7.Add( self.m_staticText, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_filePicker = wx.FilePickerCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer7.Add( self.m_filePicker, 1, wx.BOTTOM|wx.LEFT, 5 )
        
        self.m_buttonStart = wx.Button( self.m_panel3, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_buttonStart, 0, wx.BOTTOM|wx.LEFT, 5 )
        
        self.m_buttonQuit = wx.Button( self.m_panel3, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_buttonQuit, 0, wx.LEFT, 5 )
        
        self.m_panel3.SetSizer( bSizer7 )
        self.m_panel3.Layout()
        bSizer7.Fit( self.m_panel3 )
        bSizer6.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        bSizer8.Add( self.m_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_buttonStart.Bind( wx.EVT_BUTTON, self.OnButtonStart )
        self.m_buttonQuit.Bind( wx.EVT_BUTTON, self.OnButtonQuit )
        
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnButtonStart( self, event ):
        from FileBlankDeleter import FileBlankDeleter
        deleter = FileBlankDeleter(self.m_filePicker.GetPath())
        self.m_textCtrl.SetValue(deleter.process())
    
    def OnButtonQuit( self, event ):
        self.Close()
        event.Skip()
    



if __name__ == '__main__':
    
    app = wx.App();
    frame = MyFrame2(None)
    frame.Show(True)
    app.MainLoop()
    
    pass