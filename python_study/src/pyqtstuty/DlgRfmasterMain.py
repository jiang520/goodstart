#encoding=gb2312
'''
Created on 2013-6-6

@author: jiang
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from json.decoder import errmsg
import uiFormImage
import FormImage
import urllib2
from locale import str

class DlgRfmasterMain(QMainWindow): 
    def __init__(self):
        super(DlgRfmasterMain, self).__init__(None)
        spliterV = QSplitter(Qt.Vertical, self)     
        self.formimage = FormImage.FormImage(self)   
        spliterV.addWidget(self.formimage)
        self.listwidget = QListWidget(self)
        spliterV.addWidget(self.listwidget)
        spliterH = QSplitter(Qt.Horizontal, self)
        self.listwidget = QListWidget()
        spliterH.addWidget(self.listwidget)        
       
        spliterH.addWidget(spliterV)
        spliterH.setLineWidth(0)
        spliterH.setLineWidth(1)
        spliterH.setStretchFactor(0, 10)
        spliterH.setStretchFactor(1, 100)
        self.setCentralWidget(spliterH)
        
        self.__initMenu()                
        self.setMinimumSize(800, 600)
        
    def __initMenu(self):
        menubar = self.menuBar()
        #menufile = menubar.addMenu("filde")
        menufile = QMenu("file",self)
    
        self.action_quit = QAction("quit", self)
        self.action_exit = QAction("Exit", self)
        self.action_open = QAction("openfile", self)
        self.action_next = QAction("next", self)
        self.action_pre  = QAction("previous", self)
        self.edit_url = QLineEdit(self)
        self.action_urlimage = QAction("Get", self)  
        self.edit_url.setMaximumWidth(250)
       
        menufile.addAction(self.action_open)
        menufile.addAction(self.action_quit)
        menufile.addSeparator()
        menufile.addAction(self.action_exit)
                
        menubar.addMenu(menufile)                
        toolbar = QToolBar(self)      
        toolbar.setFixedHeight(33)
        toolbar.addAction(self.action_open)
        toolbar.addAction(self.action_pre)
        toolbar.addAction(self.action_next)
        toolbar.addSeparator()
        toolbar.addAction(self.action_exit)
        toolbar.addWidget(QLabel('url:',self))
        toolbar.addWidget(self.edit_url)
        toolbar.addAction(self.action_urlimage)
               
        self.action_open.triggered.connect(self.slotopen)
        self.action_next.triggered.connect(self.slotnext)
        self.action_pre.triggered.connect(self.slotpre)
        self.listwidget.currentRowChanged.connect(self.slotSelImage)
        self.action_exit.triggered.connect(self.close)
        self.addToolBar(toolbar)        
        menubar.addMenu("edit")
        menubar.addMenu("help")
        
        '''
                 当listwidget选中一个项时,更改图像窗口的图像,并重绘
        '''
    def slotSelImage(self):
        print 'selchaned'
        print self.listwidget.currentIndex()
        item = self.listwidget.currentItem()
        import os
        print 'item text=',self.strdir,item.text()
        strpath = self.strdir+"\\"+item.text()
        print strpath
        self.formimage.setimagepath(strpath)
        
    '''查找一个上下的图片文件,把文件名放到listwidget中,'''
    def slotopen(self):
        directory = QFileDialog.getExistingDirectory(self, "Find Files", QDir.currentPath())
        if len(directory) == 0: 
            directory = 'd:\\pic'
        self.strdir = directory
        self.setWindowTitle(self.strdir)
        import os
        self.listwidget.clear() 
        self.listwidget.setMinimumSize(165, 200)      
        strExt = ['.bmp','.jpg','.png','.gif','.jpeg']
        for filename in os.listdir(directory):
            if filename == '.' or filename == '..':
                continue
            print file
            if strExt.count(filename[-4:]) > 0:
                strQt = QString()
                strQt = QString.fromUtf8(unicode(filename))
                
                self.listwidget.insertItem(0, QListWidgetItem(strQt))
                #self.listwidget.insertItem(0, QListWidgetItem(file))
                
    def slotGetUrlImage(self):        
        conn = urllib2.httplib.HTTPConnection('www.baidu.com')
        strRes = conn.getresponse()
        print str
    '''
    select the next image
    '''   
    def slotnext(self):
        row = self.listwidget.currentRow()
        if row + 1 >= self.listwidget.count():
            return
        self.listwidget.setCurrentRow(row+1)
        
    def slotpre(self):
        row = self.listwidget.currentRow()
        if row -1 < 0:
            return
        self.listwidget.setCurrentRow(row-1)
'''主函数
'''        
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRfmasterMain()
    window.show()
    appp.exec_()