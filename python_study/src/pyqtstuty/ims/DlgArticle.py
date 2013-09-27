#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
import uiDlgArticle
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DlgArticle(QDialog):
    
    def __init__(self):
        super(DlgArticle,self).__init__(None)                
        self.ui = uiDlgArticle.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle(u'添加物品信息')
        self.ui.pushButton_cancel.clicked.connect(self.slotCancel)
        self.__initListView()
    
    def __initListView(self):
        #self.ui.treeview
        treeWidget = self.ui.treeWidget
       
        l1 = QStringList()
        l1.append(QString(u'top'))
        l1.append(QString(u'l2'))
        l1.append(QString(u'sfeoure'))
        self.ui.treeWidget.setColumnCount(1)
        self.ui.treeWidget.setHeaderLabels(l1)
        self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem(l1));
        item1 = QTreeWidgetItem(l1)
        item2  = QTreeWidgetItem(l1)
        item1.addChild(item2)
        self.ui.treeWidget.addTopLevelItem(item1);
        
    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgArticle()
    window.setModal(True)
    window.show()
    appp.exec_()