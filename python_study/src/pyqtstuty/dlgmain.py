'''
Created on 2013-6-6

@author: jiang
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import uiDlgAddObject
from random import Random
class DlgAddObject(QWidget):
    
    def __init__(self):
        super(DlgAddObject, self).__init__(None)
        self.ui = uiDlgAddObject.Ui_DlgAddObject()
        self.ui.setupUi(self)
        self.connect(self.ui.pushButton_2, SIGNAL("clicked()"), self.close)
        self.connect(self.ui.pushButton, SIGNAL("clicked()"), self.slotadd)
        for i in range(10):
            self.ui.comboBox.insertItem(i, str(i))
            
    def slotadd(self):        
        strName = self.ui.lineEdit.text()
        strSex = self.ui.comboBox.currentIndex()
        if "" == strName:
            QMessageBox.critical(None, "QString", "invaidate string")
            return 
        item = QListWidgetItem()
        item.setText(strName)
        rand = Random()
        clrr = rand.randint(0, 255)
        clrg = rand.randint(0, 255)
        item.setForeground(QBrush(QColor(clrr, clrg, 00)))
        self.ui.listWidget.addItem(item)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = DlgAddObject()
    window.show()
    (app.exec_())