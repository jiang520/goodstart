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
            self.setWindowTitle(u'请选择客户信息(双击选中)')
            self.tableView.doubleClicked.connect(self.slotChooseClient)
        else:
            self.setWindowTitle(u'客户信息(双击可修改)')
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
        QMessageBox.information(self, u'info', u'已导出到%s'%filePath)

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
        res = QMessageBox.warning(self, u'warning', u'确定删除此项信息吗?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
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
            QMessageBox.critical(self, u'error', u'删除客户信息失败')
        else:
            self.updateTableWidget()
            
    '''选中客户项后,直接退出'''
    def slotChooseClient(self):     
        model = self.tableView.model()
        curIndex = self.tableView.currentIndex()
        data = model.index(curIndex.row(), 0).data()
        res =  data.toInt()
        if not res[1]: return 
        clientid = res[0]
        self.__client_choosed = dbClient().getById(clientid)
        self.accept()
        
    '''选中的客户id'''   
    def getChooseClient(self):
        return self.__client_choosed
            
    def __initTableView(self):
        self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableView.setSelectionMode(QTableWidget.SingleSelection)        
        self.tableView.setAlternatingRowColors(True)
        
    '''更新表格内容'''    
    def updateTableWidget(self):
        clientlist  = dbClient().getAll()
        model = QStandardItemModel(len(clientlist),8, self)
        lablelist = QStringList()
        lablelist.append(u'系统编号')
        lablelist.append(u'公司/单位名称')
        lablelist.append(u'地址')
        lablelist.append(u'联系人')
        lablelist.append(u'电话')        
        lablelist.append(u'手机')
        lablelist.append(u'客户类型')
        lablelist.append(u'备注')
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