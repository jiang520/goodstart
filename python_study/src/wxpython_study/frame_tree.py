###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DlgDirTree
###########################################################################

class DlgDirTree ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"dir list", pos = wx.DefaultPosition, size = wx.Size( 399,294 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
											 wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer2.Add( self.m_filePicker1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_btnSet = wx.Button( self, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_btnSet, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer3.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_btnSet.Bind( wx.EVT_BUTTON, self.OnBtnSet )
		self.m_filePicker1.Bind(wx.EVT_BUTTON, self.OnDirChange)
		
	
	def __del__( self ):
		pass
	
	def OnDirChange(self, event):
		import os
		lstDirectory(os.getcwd())
		
	# Virtual event handlers, overide them in your derived class
	def OnBtnSet( self, event ):
		event.Skip()
		
		
def lstDirectory( path):
		import os
		files = os.listdir(path)
		for file in files:
			print file
	
if __name__=='__main__':
	app=wx.App(False)
	
	frame = DlgDirTree(None)
	#lstDirectory('d:\\')
	frame.Show()
	app.MainLoop()
	
else:
	print 'this is not in main'
