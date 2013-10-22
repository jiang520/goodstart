#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import ims
from ims.model.dbClient import *
from ims.ui.uiDlgClient import *
from ims.DlgClientAdd import DlgClientAdd
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
        self.tableView.setSortingEnabled(True)
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
        #�����Ҽ��˵��¼�
        #self.ui.tableView.clicked.connect(self.slotRightMenu)
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.slotRightMenu)
        self.updateTableWidget()
        self.ui.tableView.setFocus()

        #Ȩ������
        curUser = ims.model.dbSysUser.g_current_user
        #print '-----------',curUser.is_enable_write_all()
        if curUser == None or not curUser.is_enable_write_all():
            self.ui.pushButton_add.setEnabled(False)
            self.ui.pushButton_del.setEnabled(False)
            self.ui.pushButton_modify.setEnabled(False)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDeleteClient()
            return
        return QDialog.keyPressEvent(self, event) 

    def slotRightMenu(self):
        menu = QMenu()
        action_export = QAction(u'����', self)
        action_modify = QAction(u'�޸�', self)
        action_del = QAction(u'ɾ��', self)
        action_del.triggered.connect(self.slotDeleteClient)
        action_export.triggered.connect(self.slotExportClient)
        action_modify.triggered.connect(self.slotModifyClient)
        gUser = ims.model.dbSysUser.g_current_user
        if gUser==None or  not gUser.is_enable_write_all():
            action_del.setEnabled(False)
            action_modify.setEnabled(False)
        menu.addAction(action_modify)
        menu.addAction(action_del)
        menu.addSeparator()
        menu.addAction(action_export)
        menu.exec_(QCursor.pos())

    def slotExportClient(self):
        import FunctionTools
        FunctionTools.ExportTableToExcel(self.ui.tableView)

    def slotAddClient(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        dlg = DlgClientAdd(self)
        dlg.setModal(True)
        dlg.exec_()
        self.updateTableWidget()
        self.tableView.setFocus()

    def slotModifyClient(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all(): return
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
        self.tableView.setFocus()
        
    def slotDeleteClient(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all(): return
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
        self.tableView.setFocus()
            
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
        self.ui.tableView.setModel(None)
        clientlist  = dbClient().getAll()
        model = QStandardItemModel(len(clientlist),8, self)
        lablelist = QStringList()
        lablelist.append(u'���')
        lablelist.append(u'��˾/��λ����')
        lablelist.append(u'�ͻ�����')
        lablelist.append(u'��ַ')
        lablelist.append(u'��ϵ��')
        lablelist.append(u'�绰')
        lablelist.append(u'�ֻ�')
        lablelist.append(u'��ע')
        model.setHorizontalHeaderLabels(lablelist)
        i = 0
        for cli in clientlist:
            model.setItem(i, 0, QStandardItem('%d'%cli.id))
            model.setItem(i, 1, QStandardItem('%s'%cli.name))
            model.setItem(i, 2, QStandardItem('%s'%cli.type))
            model.setItem(i, 3, QStandardItem('%s'%cli.address))
            model.setItem(i, 4, QStandardItem('%s'%cli.boss))
            model.setItem(i, 5, QStandardItem('%s'%cli.phone))
            model.setItem(i, 6, QStandardItem('%s'%cli.mobile))
            model.setItem(i, 7, QStandardItem('%s'%cli.detail))
            i=i+1 
        oldIndex = self.tableView.currentIndex()    
        self.tableView.setModel(model)
        self.tableView.selectRow(oldIndex.row())
        self.tableView.setFocus()
        #�����и�
        for i in range(model.rowCount()): self.tableView.setRowHeight(i,20)
        self.tableView.setColumnWidth(0, 40)

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgClient(None)
    window.show()
    appp.exec_()