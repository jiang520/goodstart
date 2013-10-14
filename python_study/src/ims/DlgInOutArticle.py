#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.ui.uiDlgInOutArticle import *
from ims.model.dbArticleType import *
from ims.model.dbArticle import *
from ims.model.dbInoutRecord import *
from ims.DlgArticle import DlgArticle
from ims.DlgClientAdd import DlgClientAdd
from ims.DlgClient import DlgClient
import time
from datetime import *

class DlgInOutArticle(QDialog):
    """
    进出货窗口,用于输入进出货信息
    """

    def __init__(self, parent, bIn=False):
        """初始构造函数"""
        self.__recordList = []
        self.__client = None
        self.__article = None
        super(DlgInOutArticle,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(600, 480)
        if bIn:
            '''如果是进货'''
            self.setWindowTitle(u'进货')
            self.ui.radioButton_out.setChecked(False)
            self.ui.radioButton_in.setChecked(True)
            self.ui.pushButton_addtolist.setText(u'添加到入库单')
        else:
            '''如果是出货'''
            self.setWindowTitle(u'出货')
            self.ui.radioButton_out.setChecked(True)
            self.ui.radioButton_in.setChecked(False)
            self.ui.pushButton_addtolist.setText(u'添加到出货单')
        '''不允许用户自由切换出入库,防止同一货单中又出货又入库的现象发生'''
        self.ui.radioButton_in.setEnabled(False)
        self.ui.radioButton_out.setEnabled(False)
        self.ui.lineEdit_count.setText(u'1')
        self.ui.comboBox_price.setEditText(u'1.0')
        self.ui.label_unit.setText(u'')
        self.ui.label_tips.setText(u'')

        self.ui.lineEdit_articlename.setEnabled(False)
        self.ui.lineEdit_count.setMaxLength(10)
        self.ui.textEdit_detail.setAcceptRichText(False)
        #自动计算总金额
        self.ui.lineEdit_count.textChanged.connect(self.slotUpdateTotal)
        self.ui.comboBox_price.editTextChanged.connect(self.slotUpdateTotal)
        self.ui.dateEdit.setDate(QDate.currentDate())        
        #连接事件与控件
        self.ui.pushButton_addtolist.clicked.connect(self.slotAddToList)
        self.ui.pushButton_Submit.clicked.connect(self.slotSubmit)
        self.ui.pushButton_gen.clicked.connect(self.slotGenNumber)
        self.ui.pushButton_reset.clicked.connect(self.slotReset)
        self.ui.pushButton_clear.clicked.connect(self.slotClearlist)
        self.ui.pushButton_Cancel.clicked.connect(self.close)
        self.ui.pushButton_selectArticle.clicked.connect(self.slotArticleMs)
        self.ui.pushButton_selectclient.clicked.connect(self.slotSelectClient)

        self.slotUpdateTotal()
        self.__initTableWidget()
        self.slotUpdateList()
        self.slotGenNumber()

    '''初始化货单内容列表控件'''
    def __initTableWidget(self):
        self.ui.tableView.setLineWidth(50)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        '''
        设置出入库物品表格的右键菜单
        '''
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.slotTreeWidgetContextMenu)
        self.ui.tableView.setToolTip(u'按DELETE键删除')
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDeleteRecordItem()
            return
        return QDialog.keyPressEvent(event)
    '''
    从货单中删除项目
    '''
    def slotDeleteRecordItem(self):
        self.ui.tableView.setFocus()
        curIndex = self.ui.tableView.currentIndex()
        row = curIndex.row()
        if row < 0 or row >=len(self.__recordList):
            print 'current index == none'
            return
        self.__recordList.pop(row)
        self.slotUpdateList()

    ''' 清空货单列表项'''
    def slotClearlist(self):
        if QMessageBox.warning(self, u'删除提示', u'确定清空货单子项么?你将需要重新添加记录!', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            self.__recordList = []
            self.slotUpdateList()
    '''自动计算更新总金额控件中的内容'''
    def slotUpdateTotal(self):
        try:
            count = float(self.ui.lineEdit_count.text())
            price = float(self.ui.lineEdit_price.text())
            total = count*price
            self.ui.lineEdit.setText('%f'%total)
        except:
            self.ui.lineEdit.setText('')
    '''重置输入'''
    def slotReset(self):
        self.ui.lineEdit_articlename.setText('')
        self.ui.lineEdit_count.setText('1.0')
        self.ui.lineEdit_price.setText('1.0')

    '''弹出窗口让用户选择物品,并显示库存数量'''
    def slotArticleMs(self):
        dlg = DlgArticle(self, True)
        dlg.setModal(True)
        '''未选中任何物品'''
        if QDialog.Accepted != dlg.exec_():
            #print 'not accepted'
            return
        self.__article = dlg.getSelectedArticle()
        if self.__article == None: return
        #如果返回了正确的物品信息
        self.ui.lineEdit_articlename.setText(self.__article.model)
        self.ui.label_unit.setText(self.__article.unit)
        remainList = dbArticle().getSpecArticleRemainList(self.__article.id)
        if len(remainList) > 0:
            remainInfo = remainList[0]
            self.ui.lineEdit_remain.setText('%f'%remainInfo.remainCount)
        else:
            self.ui.lineEdit_remain.setText(u'0')
        #更新价格列表
        priceList = dbInOutRecord().getSpecArticlePriceList(self.__article.id)
        self.ui.comboBox_price.clear()
        for price in priceList: self.ui.comboBox_price.addItem(u'%.2f'%price)
        self.ui.comboBox_price.setCurrentIndex(0)
        self.ui.comboBox_price.setEditable(True)

       
    '''弹出窗口让用户选择客户对象'''
    def slotSelectClient(self):
        dlg = DlgClient(self, True)
        dlg.setModal(True)
        if QDialog.Accepted != dlg.exec_():
            return
        self.__client = dlg.getChooseClient()
        if self.__client == None:
            print 'Choose none client'
            return
        else:
            self.ui.lineEdit_client.setText('[%d]%s'%(self.__client.id,self.__client.name))
    '''
    右键弹出菜单,可以删除
    '''
    def slotTreeWidgetContextMenu(self):
        self.ui.tableView.setFocus()
        curIndex = self.ui.tableView.currentIndex()
        row = curIndex.row()
        print row
        if row < 0:
            print 'current index == none'
            return
        menuPop = QMenu()
        action_del = QAction(u'删除', self)
        action_del.triggered.connect(self.slotDeleteRecordItem)
        menuPop.addAction(action_del)
        menuPop.exec_(QCursor.pos())
        
    '''
    自动生成货单号
    '''
    def slotGenNumber(self):       
        self.ui.lineEdit_number.setText( QString(str(datetime.now())))

    '''
    添加到进出货记录项到货单列表
    '''
    def slotAddToList(self):
        if self.__article is None:
            self.ui.label_tips.setText(u'''<span style='color:#ff0000'>未选择具体物品型号</span>''')
            return
        record = InOutRecord()
        record.articleid = self.__article.id
        record.model = self.__article.model
        record.count = float(self.ui.lineEdit_count.text())
        '''如果是出货'''
        if self.ui.radioButton_out.isChecked():
            record.count = -record.count
            '''检查库存和出货量'''
            remainCount = float(self.ui.lineEdit_remain.text())
            if remainCount <= 0 or record.count < -remainCount:
                self.ui.label_tips.setText(u'''<span style='color:#ff0000'>出货数量超出库存</span>''')
                return
        record.detail = u'%s'%self.ui.textEdit_detail.toPlainText()
        record.price  = float(self.ui.comboBox_price.currentText())
        record.time = self.ui.dateEdit.text()
        if self.__client != None:
            record.clientid = self.__client.id
        '''检查是否已有同类物品(同id,同价格的物品在列表中)'''
        sameRecord = None
        for rec in self.__recordList:
            if rec.articleid == record.articleid:
                sameRecord = rec
        if sameRecord == None:
            self.__recordList.append(record)
        else:
            res = QMessageBox.warning(self, u'警告', u'货单中已有此物品,是否进行合并?',
                                 QMessageBox.Yes|QMessageBox.No)
            if res == QMessageBox.Yes:
                sameRecord.count = record.count + sameRecord.count
            else:
                return
        '''更新入库单中的物品列表'''
        self.slotUpdateList()

    '''#提交入库'''
    def slotSubmit(self):
        number = self.ui.lineEdit_number.text()
        if number == '':
            QMessageBox.warning(self, u'error', u'货单号不能为空')
            return
        '''货单中出入库物品列表不能为空'''
        if len(self.__recordList) <= 0:
            return
        '''修改记录中的货单号和日期'''
        for rec in self.__recordList:
            rec.time = self.ui.dateEdit.text()
            rec.number = number
                        
        if not dbInOutRecord().addRecords(self.__recordList):
            QMessageBox.warning(self, u'error', u'入库失败,请重新再试')
        else:
            QMessageBox.information(self, u'error', u'库存记录已更新')
            self.__recordList = []
            self.slotUpdateList()
    '''
    更新物品列表
    '''
    def slotUpdateList(self):
        model = QStandardItemModel(len(self.__recordList), 5, self)
        i = 0
        for record in self.__recordList:
            model.setItem(i, 0, QStandardItem('%d'%record.articleid))
            model.setItem(i, 1, QStandardItem(record.model))
            model.setItem(i, 2, QStandardItem('%f'%record.count))
            model.setItem(i, 3, QStandardItem('%f'%record.price))
            model.setItem(i, 4, QStandardItem(record.detail))
            i = i+1  
        self.ui.tableView.setModel(model)
        '''设置表格表头'''
        labels = QStringList()
        labels.append(u'物品id')        
        labels.append(u'物品名称')        
        labels.append(u'数量')        
        labels.append(u'单价')        
        labels.append(u'说明')
        model.setHorizontalHeaderLabels(labels)
        '''设置行高'''
        for i in range(model.rowCount()):
            self.ui.tableView.setRowHeight(i, 20)
        '''设置列宽'''
        self.ui.tableView.setColumnWidth(0, 50)
        self.ui.tableView.setColumnWidth(4, 250)
        #设置清空,提交按钮的可用性
        self.ui.pushButton_Submit.setEnabled(len(self.__recordList) > 0)
        self.ui.pushButton_clear.setEnabled(len(self.__recordList) > 0)


    '''弹出窗口让用户选择物品型号'''
    def slotChooseArticle(self):
        item = self.ui.treeWidget.currentItem()
        if item == None: return
        itemData = item.data(0, Qt.UserRole)
        if itemData == None: return
        articleid,bTrans = itemData.toInt()
        if not bTrans: return
        self.ui.lineEdit_articlename.setText(item.text(0))
        self.ui.lineEdit_articleid.setText(str(articleid))
        remainInfo = dbArticle().getSpecArticleRemainList(articleid)
        if remainInfo != None and len(remainInfo) > 0:
            self.ui.lineEdit_remain.setText('%f'%remainInfo[0].remainCount)       

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgInOutArticle(None)
    window.show()
    appp.exec_()
