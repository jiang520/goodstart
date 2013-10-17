#encoding=gb2312
'''
Created on 2013-10-2

@author: jiang
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ims
from ims.FunctionTools import *
from ims.ui.uiDlgRecordSearch import *
from ims.ui import uiDlgRecordSearch
from ims.model.dbInoutRecord import *
from ims.DlgRecordModify import DlgRecordModify

class DlgRecordSearch(QDialog):

    def setArticleIdFilter(self, id):
        if id == None or id <= 0:
            self.__articleid = None
        else :
            self.__articleid = id
        self.__initRecordTable()

    def __init__(self,parent=None):
        super(DlgRecordSearch, self).__init__(parent)
        self.ui = uiDlgRecordSearch.Ui_Dialog()
        self.ui.setupUi(self)

        self.__articleid = None
        self.__initRecordTable()
        self.ui.dateEdit_end.setDate(QDate.currentDate())
        self.ui.pushButton_apply.setDefault(True)
        self.ui.pushButton_apply.clicked.connect(self.slotApplySearch)
        self.ui.pushButton_reset.clicked.connect(self.slotResetSearch)
        self.ui.pushButton_export.clicked.connect(self.slotExport)
        
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.doubleClicked.connect(self.slotModifyRecord)
        self.ui.tableView.setSortingEnabled(True)
        

    #�޸ļ�¼
    def slotModifyRecord(self):
        #Ȩ�޼��
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():
            return
        model = self.ui.tableView.model()
        curIndex = self.ui.tableView.currentIndex()
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

    #ɾ����¼
    def slotDelRecord(self):        
        #Ȩ�޼��
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():
            return
        model = self.ui.tableView.model()
        curIndex = self.ui.tableView.currentIndex()
        if curIndex is None:
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

    #����DELETE��ɾ����
    def keyPressEvent(self, event):
        if event.key()== Qt.Key_Delete:
            self.slotDelRecord()
            return 
        return QDialog.keyPressEvent(self, event)

    # ���½�������¼�б�
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
        dateInterval = None
        if self.ui.checkBox_date.isChecked():
            strDateStart = self.ui.dateEdit_start.text()
            strDateEnd = self.ui.dateEdit_end.text()
            dateInterval = (strDateStart, strDateEnd)
        strArticleModel = None
        if self.ui.checkBox_model.isChecked():
            strArticleModel = unicode(self.ui.lineEdit_model.text())
            strArticleModel = strArticleModel.strip()

        #print strNumber, strDateEnd, strDateStart
        #��ȡ��ϲ�ѯ���
        recordlist = dbInOutRecord().getRecord(strNumber=strNumber,
                                               strArticleModel=strArticleModel,
                                               strClientName=None,
                                               dateInterval = dateInterval,
                                               articleid=self.__articleid
                                                )
        #���˽�����
        def func_filter_in(item): return item.count > 0
        def func_filter_out(item): return  item.count < 0
        if self.ui.checkBox_inout.isChecked():
            if self.ui.radioButton_in.isChecked():
                recordlist = filter(func_filter_in,recordlist)
            else:
                recordlist = filter(func_filter_out,recordlist)
        #����tabe�ؼ�,����ָ��parentΪself/����,�����˳��д�
        model = QStandardItemModel(len(recordlist), 6, self)
        i = 0
        for item in recordlist:
            model.setItem(i, 0, QStandardItem(QString(str(item.id))))
            articleInfo = item.getArticleInfo()
            clientInfo  = item.getClientInfo()
            #��ȡ��Ʒ�ͺ�,��λ
            if articleInfo != None:
                model.setItem(i, 1, QStandardItem(QString(unicode(articleInfo.model) )) )
                model.setItem(i, 5, QStandardItem(QString(u'%s'%articleInfo.unit )))
            model.setItem(i, 2, QStandardItem(QString(u'%s'%item.time)))
            model.setItem(i, 3, QStandardItem(QString( item.count < 0  and u'����' or u'���')))
            model.setItem(i, 4, QStandardItem(QString(u'%.2f'%item.count)))
            model.setItem(i, 6, QStandardItem(QString(u'%.2f'%item.price)))
            model.setItem(i, 7, QStandardItem(QString(u'%.2f'%(item.count*item.price))))
            model.setItem(i, 8, QStandardItem(QString(item.number)))
            model.setItem(i, 9, QStandardItem(QString(item.detail)))
            #��ȡ�ͻ���Ϣ
            if clientInfo!=None:
                model.setItem(i, 10, QStandardItem(QString(clientInfo.name)))
            self.ui.tableView.setRowHeight(i,10)
            i=i+1
        #table�ؼ��ı���ͷ
        strHeadLabels = [u'id',u'�ͺ�',u'����', u'�����', u'����', u'��λ', u'����', u'���', u'������',u'��ϸ',u'�ͻ�/������']
        labels = QStringList(strHeadLabels)
        model.setHorizontalHeaderLabels(labels)
        self.ui.tableView.setModel(model)
        #�����и�,�п�
        for i in range(model.rowCount(parent=QModelIndex())):self.ui.tableView.setRowHeight(i, 20)
        for i in range(7): self.ui.tableView.setColumnWidth(i, 80)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(3, 40)
        self.ui.tableView.setColumnWidth(5, 40)
        self.ui.tableView.setColumnWidth(7, 150)
            
        
    #Ӧ����ϲ�ѯ����
    def slotApplySearch(self):
        self.__initRecordTable()

    #���ò�ѯ����
    def slotResetSearch(self):
        self.ui.checkBox_date.setChecked(False)
        self.ui.checkBox_number.setChecked(False)
        self.ui.checkBox_inout.setChecked(False)
        self.ui.checkBox_model.setChecked(False)
        self.slotApplySearch()

    #���������ļ�
    def slotExport(self):
        ExportTableToExcel(self.ui.tableView)


if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRecordSearch()
    window.show()
    appp.exec_()
