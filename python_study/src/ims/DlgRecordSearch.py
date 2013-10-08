#encoding=gb2312
'''
Created on 2013-10-2

@author: jiang
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from ims.ui.uiDlgRecordSearch import *
from ims.ui import uiDlgRecordSearch
from ims.model.dbInoutRecord import *
from ims.DlgRecordModify import DlgRecordModify

class DlgRecordSearch(QDialog):
    __articleid = None
    
    def setArticleIdFilter(self, id):
        if id == None or id <= 0:
            self.__articleid = None
        else :
            self.__articleid = id
        self.__initRecordTable()

    def __init__(self):
        super(DlgRecordSearch, self).__init__(None)
        self.ui = uiDlgRecordSearch.Ui_Dialog()
        self.ui.setupUi(self)
        self.tableInoutRecord = self.ui.tableView
        self.__initRecordTable()
        self.ui.dateEdit_end.setDate(QDate.currentDate())
        self.ui.pushButton_apply.clicked.connect(self.slotApplySearch)
        self.ui.pushButton_reset.clicked.connect(self.slotResetSearch)
        
        self.tableInoutRecord.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableInoutRecord.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableInoutRecord.setSelectionMode(QTableWidget.SingleSelection)    
        self.tableInoutRecord.setAlternatingRowColors(True)
        self.tableInoutRecord.doubleClicked.connect(self.slotModifyRecord)
        
   
    def slotModifyRecord(self):
        model = self.tableInoutRecord.model()
        curIndex = self.tableInoutRecord.currentIndex()
        celldata = model.index(curIndex.row(), 0).data()
        resTrans =  celldata.toInt()
        if not resTrans[1]: return
        recordid = resTrans[0]
        record = dbInOutRecord().getById(recordid)
        if record == None: return
        dlg = DlgRecordModify(self,record)
        dlg.setModal(True)
        dlg.exec_()
        self.__initRecordTable()
        
    def slotDelRecord(self):        
        model = self.tableInoutRecord.model()
        curIndex = self.tableInoutRecord.currentIndex()
        if curIndex == None:
            QMessageBox.critical(self, u'Error', u'δѡ���κ���')
            self.ui.tableView.setFocus()
            return
        if QMessageBox.No == QMessageBox.warning(self, u'����', u'�ؼ�����,ȷ��ɾ������?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
            self.ui.tableView.setFocus()
            return
        celldata = model.index(curIndex.row(), 0).data()
        res  =  celldata.toInt()
        print res
        if not res[1] or res[0] <= 0 :return False
        recordid = res[0]            
        print 'try to delte '
        if dbInOutRecord().delete(recordid):
            self.__initRecordTable()
        self.ui.tableView.setFocus()
        
    def keyPressEvent(self, event):
        if event.key()== Qt.Key_Delete:
            self.slotDelRecord()
            return 
        return QDialog.keyPressEvent(self, event)
    '''
            ���½�������¼�б�
    '''    
    def __initRecordTable(self):
        #��ȡ������,���δ����,��ΪNone
        strNumber = None
        if self.ui.checkBox_number.isChecked():
            strNumber = u'%s'%self.ui.lineEdit_number.text()
            strNumber.lstrip()
            strNumber.rstrip()
            if len(strNumber) <= 0:
                strNumber = None
        #��ȡ��ʼ����ʱ��
        if self.ui.checkBox_date.isChecked():
            strDateStart = self.ui.dateEdit_start.text()
            strDateEnd = self.ui.dateEdit_end.text()
        else:
            strDateEnd = None
            strDateStart = None
        #print strNumber, strDateEnd, strDateStart
        #��ȡ��ϲ�ѯ���
        recordlist = dbInOutRecord().getRecord(0, 50, strNumber, strDateStart, strDateEnd,self.__articleid)
        #����tabe�ؼ�
        model = QStandardItemModel(len(recordlist), 6)
        i = 0
        for item in recordlist:
            model.setItem(i, 0, QStandardItem(QString(str(item.id))))
            model.setItem(i, 1, QStandardItem(QString(str(item.model) )) )
            #print item.time
            model.setItem(i, 2, QStandardItem(QString('%s'%item.time)))
            model.setItem(i, 3, QStandardItem(QString( item.count < 0  and u'����' or u'���')))
            model.setItem(i, 4, QStandardItem(QString(str(item.count))))            
            model.setItem(i, 5, QStandardItem(QString(str(item.price))))
            model.setItem(i, 6, QStandardItem(QString('%f'%(item.count*item.price))))
            model.setItem(i, 7, QStandardItem(QString(item.number)))
            #print 'detail=', item.detail
            #model.setItem(i, 5, QStandardItem(QString(str(item.detail))))
            self.tableInoutRecord.setRowHeight(i,10)  
            i = i+1
        #table�ؼ��ı���ͷ
        labels = QStringList()
        labels.append(QString(u'id'))
        labels.append(QString(u'�ͺ�'))
        labels.append(QString(u'����'))
        labels.append(QString(u'�����'))
        labels.append(QString(u'����'))
        labels.append(QString(u'����'))        
        labels.append(QString(u'���'))
        labels.append(QString(u'������'))
        model.setHorizontalHeaderLabels(labels)
        self.tableInoutRecord.setModel(model)
        for i in range(model.rowCount(parent=QModelIndex())):
            self.tableInoutRecord.setRowHeight(i, 20)
        for i in range(7):
            self.tableInoutRecord.setColumnWidth(i, 80)
        self.tableInoutRecord.setColumnWidth(7, 150)
            
        
            
    def slotApplySearch(self):
        self.__initRecordTable()

    def slotResetSearch(self):
        self.ui.checkBox_date.setChecked(False)
        self.ui.checkBox_number.setChecked(False)
        self.slotApplySearch()
        
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRecordSearch()
    window.show()
    appp.exec_()
