#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.uiDlgInOutArticle import Ui_Dialog
from ims.model.dbArticleType import *
from ims.model.dbArticle import *
from ims.model.dbInoutRecord import *
from datetime import *
import time

class DlgInOutArticle(QDialog):   
    recordList = []
     
    def __init__(self):
        super(DlgInOutArticle,self).__init__(None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
       
        self.ui.tableView.setLineWidth(50)
        self.ui.lineEdit_count.setText(u'1')
        self.ui.lineEdit_price.setText(u'1.0')
        self.ui.lineEdit_articlename.setEnabled(False)
        self.ui.lineEdit_articleid.setEnabled(False)
        self.ui.radioButton_in.setChecked(True)
        self.ui.pushButton_Cancel.clicked.connect(self.slotCancel)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.treeWidget.itemSelectionChanged.connect(self.slotChooseArticle)
        self.ui.pushButton_addtolist.clicked.connect(self.slotAddToList)
        self.ui.pushButton_Submit.clicked.connect(self.slotSubmit)
        self.ui.pushButton_gen.clicked.connect(self.slotGenNumber)
        self.ui.pushButton_reset.clicked.connect(self.slotReset)
        self.ui.pushButton_clear.clicked.connect(self.slotClearlist)
        
        self.__initListView()
        self.__initTableWidget()
        self.slotUpdateList()
        self.slotGenNumber()
    
    def __initTableWidget(self):
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
    ''' 清空货单列表项'''
    def slotClearlist(self):
        if QMessageBox.warning(self, u'删除提示', u'确定清空货单子项么?你将需要重新添加记录!', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            self.recordList = []
            self.slotUpdateList()
        
    '''重置输入'''
    def slotReset(self):
        self.ui.lineEdit_articleid.setText('')
        self.ui.lineEdit_articlename.setText('')
        self.ui.lineEdit.setText('')
        
    '''自动生成货单号'''
    def slotGenNumber(self):       
        self.ui.lineEdit_number.setText( QString(str(datetime.now())))
    '''添加到进出货记录项到货单列表'''    
    def slotAddToList(self):
        #try:
        record = InOutRecord()
        strid = self.ui.lineEdit_articleid.text()
        if strid == '' :
            return
        record.articleid = int(strid)
        record.model = self.ui.lineEdit_articlename.text()
        record.count = float(self.ui.lineEdit_count.text())
        if self.ui.radioButton_out.isChecked():
            record.count = -record.count
        record.detail = self.ui.textEdit_detail.toPlainText()
        record.price = float(self.ui.lineEdit_price.text())
        record.time = self.ui.dateEdit.text()
        '''检查是否已有同类物品(同id,同价格的物品在列表中)'''
        sameRecord = None
        for rec in self.recordList:
            if rec.articleid == record.articleid and rec.price == record.price:
                sameRecord = rec
        if sameRecord == None:
            self.recordList.append(record)
        else:
            res = QMessageBox.warning(self, u'警告', u'货单中已有此同价物品,是否进行合并?\n是--合并\n 否: 不合并但添加\n 取消--不合并也不添加',
                                 QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if res == QMessageBox.Yes:
                sameRecord.count = record.count + sameRecord.count
            elif res == QMessageBox.No:
                self.recordList.append(record)
            else:
                return   
        self.slotUpdateList()
        # except:
        #print 'add error!'    
    def slotSubmit(self):
        number = self.ui.lineEdit_number.text()
        if number == '':
            QMessageBox.warning(self, u'error', u'货单号不能为空')
            return
        
        '''修改记录中的货单号和日期'''
        for rec in self.recordList:
            rec.time = self.ui.dateEdit.text()
            rec.number = number
                        
        if not dbInOutRecord().addRecords(self.recordList):
            QMessageBox.warning(self, u'error', u'入库失败,请重新再试')
        else:
            QMessageBox.information(self, u'error', u'库存记录已更新')
            self.recordList = []
            self.slotUpdateList()
         
    def slotUpdateList(self):
        model = QStandardItemModel(len(self.recordList), 5)
        i = 0
        for record in self.recordList:
            model.setItem(i, 0, QStandardItem('%d'%record.articleid))
            model.setItem(i, 1, QStandardItem(record.model))
            model.setItem(i, 2, QStandardItem('%f'%record.count))
            model.setItem(i, 3, QStandardItem('%f'%record.price))
            model.setItem(i, 4, QStandardItem(record.detail))
            i = i+1  
        self.ui.tableView.setModel(model)
        labels = QStringList()
        labels.append(u'物品id')        
        labels.append(u'物品名称')        
        labels.append(u'数量')        
        labels.append(u'单价')        
        labels.append(u'说明')
        model.setHorizontalHeaderLabels(labels)
        for i in range(model.rowCount()):
            self.ui.tableView.setRowHeight(i, 20)
        self.ui.tableView.setColumnWidth(4, 250)
                
    def slotChooseArticle(self):
        item = self.ui.treeWidget.currentItem()
        if item.text(2) == '':
            self.ui.pushButton_addtolist.setEnabled(False)
            return
        self.ui.lineEdit_articlename.setText(item.text(0))
        self.ui.lineEdit_articleid.setText(item.text(3))
        self.ui.pushButton_addtolist.setEnabled(True)
    def slotCancel(self):
        self.close()
            
    #更新treeview控件    
    def __initListView(self):       
        strListHeader = QStringList()
        strListHeader.append(u'分类')
        strListHeader.append(u'封装')
        strListHeader.append(u'备注')
        strListHeader.append(u'')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()
        listTypes1 = dbArticleType().getType1() 
        '''插入类别1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)
            item.setText(3, str(t1.id))            
            listType2 = dbArticleType().getType2(t1.id)
            '''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setText(3, str(t2.id))
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''插入物品型号'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, ac.packaging)
                    item3.setText(2, ac.detail)
                    item3.setText(3, str(ac.id))
                    item2.addChild(item3)
            self.ui.treeWidget.addTopLevelItem(item)
            
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgInOutArticle()
    window.show()
    appp.exec_()
