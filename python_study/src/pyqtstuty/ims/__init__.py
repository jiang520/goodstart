#encoding=gb2312
'''
Created on 2013-6-6

@author: jiang
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from json.decoder import errmsg
import urllib2
from locale import str
from DlgClient import DlgClient

class DlgRfmasterMain(QMainWindow): 
    def __init__(self):
        super(DlgRfmasterMain, self).__init__(None)
        spliterV = QSplitter(Qt.Vertical, self)     
        self.tableWidget = QTableWidget()
        spliterV.addWidget(self.tableWidget)
        self.listwidget = QListWidget(self)
        spliterV.addWidget(self.listwidget)
        spliterH = QSplitter(Qt.Horizontal, self)
       
        self.treeCtrl = QTreeWidget(self)
        self.__initTreeCtrl()
        spliterH.addWidget(self.treeCtrl)       
       
        spliterH.addWidget(spliterV)
        spliterH.setLineWidth(0)
        spliterH.setLineWidth(1)
        spliterH.setStretchFactor(0, 30)
        spliterH.setStretchFactor(1, 100)
        self.setCentralWidget(spliterH)
        
        self.__initMenu()                
        self.setMinimumSize(800, 600)
    def __initTreeCtrl(self):
        self.treeCtrl.setColumnCount(3)
        headerStringList = QStringList()
        headerStringList.append(u'类别')
        headerStringList.append(u'型号')
        headerStringList.append(u'封装')
        self.treeCtrl.setColumnWidth(0,50)
        self.treeCtrl.setColumnWidth(1,50)
        self.treeCtrl.setColumnWidth(1,50)
        self.treeCtrl.setHeaderLabels(headerStringList)
        item = QTreeWidgetItem()
        item.setText(0, QString('test1'))
        item.setText(2, QString(u'test2'))
        self.treeCtrl.insertTopLevelItem(0, item)
        
    def __initMenu(self):
        menubar = self.menuBar()
        #menufile = menubar.addMenu("filde")
        menufile = QMenu("file",self)
    
        self.action_in = QAction(u"进货", self)
        self.action_out = QAction(u"出货", self)
        self.action_client  = QAction(u"客户管理", self)        
        self.action_article = QAction(u"物品管理", self)
        self.action_exit = QAction(u'退出系统', self)
        
        menufile.addAction(self.action_in)
        menufile.addAction(self.action_out)
        menufile.addSeparator()
        menufile.addAction(self.action_article)
        menufile.addAction(self.action_client)
        
        menufile.addSeparator()
        menufile.addAction(self.action_exit)   
                
        menubar.addMenu(menufile)                
        toolbar = QToolBar(self)      
        toolbar.setFixedHeight(33)
        toolbar.addAction(self.action_in)
        toolbar.addAction(self.action_out)
        toolbar.addAction(self.action_client)
        toolbar.addSeparator()
        toolbar.addAction(self.action_article)
        toolbar.addSeparator()
        toolbar.addAction(self.action_exit)     
        
        self.action_client.triggered.connect(self.slotDlgClient)     
        self.action_exit.triggered.connect(self.slotExitSystem)     
        self.action_in.triggered.connect(self.slotInOut)           
        self.action_out.triggered.connect(self.slotInOut)
        self.action_article.triggered.connect(self.slotArticle)
        self.addToolBar(toolbar)        
        menubar.addMenu("edit")
        menubar.addMenu("help")
        
    def slotExitSystem(self):
        print 'slot exit system'
        self.close()
        
    def slotDlgClient(self):
        print 'slot dlg client'
        
        dlg = DlgClient()
        dlg.setModal(True)
        dlg.exec_()
        
    '''查找一个上下的图片文件,把文件名放到listwidget中,'''
    def slotInOut(self):
        import DlgInOutArticle
        dlg = DlgInOutArticle.DlgInOutArticle()
        dlg.setModal(True)
        dlg.exec_()
     
                
    def slotArticle(self):
        import DlgArticle
        dlg = DlgArticle.DlgArticle()
        dlg.setModal(True)
        dlg.exec_()
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