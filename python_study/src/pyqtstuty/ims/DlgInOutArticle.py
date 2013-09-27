'''
Created on 2013-9-27

@author: Administrator
'''
import uiDlgInOutArticle
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DlgInOutArticle(QDialog):
    
    def __init__(self):
        super(DlgInOutArticle,self).__init__(None)
        self.ui = uiDlgInOutArticle.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_Cancel.clicked.connect(self.slotCancel)
    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgInOutArticle()
    window.show()
    appp.exec_()