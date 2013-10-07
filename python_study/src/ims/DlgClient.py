#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from ims.model.dbClient import *
from ims.ui.uiDlgClient import *
from ims.DlgClientAdd import DlgClientAdd
from FunctionTools import ExportTableWidgetData
class DlgClient(QDialog):
    '''
    classdocs
    '''
    def __init__(self,parent, bUsedForChooseClient=False):
        '''
        Constructor
        '''
        super(QDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(600,400)
        self.tableView = self.ui.tableView
        self.__initTableView()  
        self.ui.pushButton_add.clicked.connect(self.slotAddClient)
        self.ui.pushButton_modify.clicked.connect(self.slotModifyClient)
        self.ui.pushButton_del.clicked.connect(self.slotDeleteClient)
        self.ui.pushButton_export.clicked.connect(self.slotExportClient)
        self.__client_choosed = None
        if bUsedForChooseClient:
            self.setWindowTitle(u'��ѡ��ͻ���Ϣ(˫��ѡ��)')
            self.tableView.doubleClicked.connect(self.slotChooseClient)
        else:
            self.setWindowTitle(u'�ͻ���Ϣ(˫�����޸�)')
            self.ui.tableView.doubleClicked.connect(self.slotModifyClient)                      
             
        self.updateTableWidget()
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDeleteClient()
            return True    
        return QDialog.keyPressEvent(self, event) 

    def slotExportClient(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        ExportTableWidgetData(self.ui.tableView, filePath)
        QMessageBox.information(self, u'info', u'�ѵ�����%s'%filePath)

    def slotAddClient(self):
        dlg = DlgClientAdd(self)
        dlg.setModal(True)
        dlg.exec_()
        self.updateTableWidget()
        
    def slotModifyClient(self):
        model = self.tableView.model()
        curIndex = self.tableView.currentIndex()
        data = model.index(curIndex.row(), 0).data()
        res =  data.toInt()
        if not res[1]: return 
        clientid = res[0]
        #print clientid
        client = dbClient().getById(clientid)
        dlg = DlgClientAdd(self, client)
        dlg.setModal(True)
        dlg.exec_()
        self.updateTableWidget()
        
    def slotDeleteClient(self):
        res = QMessageBox.warning(self, u'warning', u'ȷ��ɾ��������Ϣ��?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.No: 
            self.tableView.setFocus()
            return
        model = self.tableView.model()
        curIndex = self.tableView.currentIndex()
        data = model.index(curIndex.row(), 0).data()
        res =  data.toInt()
        if not res[1]: return 
        clientid = res[0]
        if not dbClient().delete(clientid):
            QMessageBox.critical(self, u'error', u'ɾ���ͻ���Ϣʧ��')
        else:
            self.updateTableWidget()
            
    '''ѡ�пͻ����,ֱ���˳�'''
    def slotChooseClient(self):     
        model = self.tableView.model()
        curIndex = self.tableView.currentIndex()
        data = model.index(curIndex.row(), 0).data()
        res =  data.toInt()
        if not res[1]: return 
        clientid = res[0]
        self.__client_choosed = dbClient().getById(clientid)
        self.accept()
        
    '''ѡ�еĿͻ�id'''   
    def getChooseClient(self):
        return self.__client_choosed
            
    def __initTableView(self):
        self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableView.setSelectionMode(QTableWidget.SingleSelection)        
        self.tableView.setAlternatingRowColors(True)
        
    '''���±������'''    
    def updateTableWidget(self):
        clientlist  = dbClient().getAll()
        model = QStandardItemModel(len(clientlist),8, self)
        lablelist = QStringList()
        lablelist.append(u'ϵͳ���')
        lablelist.append(u'��˾/��λ����')
        lablelist.append(u'��ַ')
        lablelist.append(u'��ϵ��')
        lablelist.append(u'�绰')        
        lablelist.append(u'�ֻ�')
        lablelist.append(u'�ͻ�����')
        lablelist.append(u'��ע')
        model.setHorizontalHeaderLabels(lablelist)
        i = 0
        for cli in clientlist:
            model.setItem(i, 0, QStandardItem('%d'%cli.id))
            model.setItem(i, 1, QStandardItem('%s'%cli.name))
            model.setItem(i, 2, QStandardItem('%s'%cli.address))
            model.setItem(i, 3, QStandardItem('%s'%cli.boss))
            model.setItem(i, 4, QStandardItem('%s'%cli.phone))
            model.setItem(i, 5, QStandardItem('%s'%cli.mobile))  
            model.setItem(i, 6, QStandardItem('%s'%cli.clienttype))  
            model.setItem(i, 7, QStandardItem('%s'%cli.detail))             
            i=i+1 
        oldIndex = self.tableView.currentIndex()    
        self.tableView.setModel(model)
        self.tableView.selectRow(oldIndex.row())
        self.tableView.setFocus()
        for i in range(model.rowCount()):
            self.tableView.setRowHeight(i,20)        
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgClient(None)
    window.show()
    appp.exec_()