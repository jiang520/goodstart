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
        

    #修改记录
    def slotModifyRecord(self):
        #权限检查
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

    #删除记录
    def slotDelRecord(self):        
        #权限检查
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():
            return
        model = self.ui.tableView.model()
        curIndex = self.ui.tableView.currentIndex()
        if curIndex is None:
            QMessageBox.critical(self, u'Error', u'未选择任何行')
            self.ui.tableView.setFocus()
            return
        if QMessageBox.No == QMessageBox.warning(self, u'警告', u'关键操作,确定删除此项?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
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

    #按下DELETE键删除项
    def keyPressEvent(self, event):
        if event.key()== Qt.Key_Delete:
            self.slotDelRecord()
            return 
        return QDialog.keyPressEvent(self, event)

    # 更新进出货记录列表
    def __initRecordTable(self):
        #获取货单号,如果未输入,则为None
        strNumber = None
        if self.ui.checkBox_number.isChecked():
            strNumber = u'%s'%self.ui.lineEdit_number.text()
            strNumber.lstrip()
            strNumber.rstrip()
            if len(strNumber) <= 0:
                strNumber = None
        #获取起始结束时间
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
        #获取组合查询结果
        recordlist = dbInOutRecord().getRecord(strNumber=strNumber,
                                               strArticleModel=strArticleModel,
                                               strClientName=None,
                                               dateInterval = dateInterval,
                                               articleid=self.__articleid
                                                )
        #过滤进出库
        def func_filter_in(item): return item.count > 0
        def func_filter_out(item): return  item.count < 0
        if self.ui.checkBox_inout.isChecked():
            if self.ui.radioButton_in.isChecked():
                recordlist = filter(func_filter_in,recordlist)
            else:
                recordlist = filter(func_filter_out,recordlist)
        #更新tabe控件,必须指定parent为self/其他,否则退出有错
        model = QStandardItemModel(len(recordlist), 6, self)
        i = 0
        for item in recordlist:
            model.setItem(i, 0, QStandardItem(QString(str(item.id))))
            articleInfo = item.getArticleInfo()
            clientInfo  = item.getClientInfo()
            #获取物品型号,单位
            if articleInfo != None:
                model.setItem(i, 1, QStandardItem(QString(unicode(articleInfo.model) )) )
                model.setItem(i, 5, QStandardItem(QString(u'%s'%articleInfo.unit )))
            model.setItem(i, 2, QStandardItem(QString(u'%s'%item.time)))
            model.setItem(i, 3, QStandardItem(QString( item.count < 0  and u'出库' or u'入库')))
            model.setItem(i, 4, QStandardItem(QString(u'%.2f'%item.count)))
            model.setItem(i, 6, QStandardItem(QString(u'%.2f'%item.price)))
            model.setItem(i, 7, QStandardItem(QString(u'%.2f'%(item.count*item.price))))
            model.setItem(i, 8, QStandardItem(QString(item.number)))
            model.setItem(i, 9, QStandardItem(QString(item.detail)))
            #获取客户信息
            if clientInfo!=None:
                model.setItem(i, 10, QStandardItem(QString(clientInfo.name)))
            self.ui.tableView.setRowHeight(i,10)
            i=i+1
        #table控件的标题头
        strHeadLabels = [u'id',u'型号',u'日期', u'出入库', u'数量', u'单位', u'单价', u'金额', u'货单号',u'详细',u'客户/供货商']
        labels = QStringList(strHeadLabels)
        model.setHorizontalHeaderLabels(labels)
        self.ui.tableView.setModel(model)
        #设置行高,列宽
        for i in range(model.rowCount(parent=QModelIndex())):self.ui.tableView.setRowHeight(i, 20)
        for i in range(7): self.ui.tableView.setColumnWidth(i, 80)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(3, 40)
        self.ui.tableView.setColumnWidth(5, 40)
        self.ui.tableView.setColumnWidth(7, 150)
            
        
    #应用组合查询条件
    def slotApplySearch(self):
        self.__initRecordTable()

    #重置查询条件
    def slotResetSearch(self):
        self.ui.checkBox_date.setChecked(False)
        self.ui.checkBox_number.setChecked(False)
        self.ui.checkBox_inout.setChecked(False)
        self.ui.checkBox_model.setChecked(False)
        self.slotApplySearch()

    #导出数据文件
    def slotExport(self):
        ExportTableToExcel(self.ui.tableView)


if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRecordSearch()
    window.show()
    appp.exec_()
