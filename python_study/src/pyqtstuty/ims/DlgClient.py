'''
Created on 2013-9-27

@author: Administrator
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from client import *
class DlgClient(QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(QDialog,self).__init__(None)
        self.resize(800,600)
        self.table = QTableView(self)
       # headerView = QHeaderView()        
        #self.table.setColumnCount(8)
        layoutMain = QVBoxLayout()
        
        
        layout1 = QHBoxLayout()
        #layout1.addSpacerItem(QSpacerItem(1,0,QSizePolicy.Maximum, QSizePolicy.Minimum))
        layout1.addWidget(QPushButton(u'modify',self))       
        layout1.addWidget(QLabel(u"input",self))
        layout1.addWidget(QPushButton(u'add',self))
        layout1.addWidget(QPushButton(u'del',self))     
       
        layoutMain.addLayout(layout1)
        layoutMain.addWidget(self.table)
        self.setLayout(layoutMain)
        self.updateTableWidget()
    def updateTableWidget(self):
        clientlist  = dbClient().getAll()
        model = QStandardItemModel(8,len(clientlist),self)
        lablelist = QStringList()
        lablelist.append(u'id')
        lablelist.append(u'company name')
        lablelist.append(u'address')
        lablelist.append(u'boss')
        lablelist.append(u'phone')        
        lablelist.append(u'mobile')
        lablelist.append(u'type')
        lablelist.append(u'detial')
        model.setHorizontalHeaderLabels(lablelist)
        i = 0
        for cli in clientlist:
            model.setItem(i, 0, QStandardItem('i'))
            model.setItem(i, 1, QStandardItem('%s'%cli.name))
            model.setItem(i, 2, QStandardItem('%s'%cli.address))
            model.setItem(i, 3, QStandardItem('%s'%cli.boss))
            model.setItem(i, 4, QStandardItem('%s'%cli.phone))
            model.setItem(i, 5, QStandardItem('%s'%cli.mobile))  
            model.setItem(i, 6, QStandardItem('%s'%cli.clienttype))  
            model.setItem(i, 7, QStandardItem('%s'%cli.detail))             
            i=i+1            
        self.table.setModel(model)
        for i in range(model.rowCount()):
            self.table.setRowHeight(i,20)        
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgClient()
    window.show()
    appp.exec_()