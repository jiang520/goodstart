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
    ����������,���������������Ϣ
    """

    def __init__(self, parent, bIn=False):
        """��ʼ���캯��"""
        self.__recordList = []
        self.__client = None
        self.__article = None
        super(DlgInOutArticle,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(600, 480)
        if bIn:
            '''����ǽ���'''
            self.setWindowTitle(u'����')
            self.ui.radioButton_out.setChecked(False)
            self.ui.radioButton_in.setChecked(True)
            self.ui.pushButton_addtolist.setText(u'��ӵ���ⵥ')
        else:
            '''����ǳ���'''
            self.setWindowTitle(u'����')
            self.ui.radioButton_out.setChecked(True)
            self.ui.radioButton_in.setChecked(False)
            self.ui.pushButton_addtolist.setText(u'��ӵ�������')
        '''�������û������л������,��ֹͬһ�������ֳ���������������'''
        self.ui.radioButton_in.setEnabled(False)
        self.ui.radioButton_out.setEnabled(False)
        self.ui.lineEdit_count.setText(u'1')
        self.ui.comboBox_price.setEditText(u'1.0')
        self.ui.label_unit.setText(u'')
        self.ui.label_tips.setText(u'')

        self.ui.lineEdit_articlename.setEnabled(False)
        self.ui.lineEdit_count.setMaxLength(10)
        self.ui.textEdit_detail.setAcceptRichText(False)
        #�Զ������ܽ��
        self.ui.lineEdit_count.textChanged.connect(self.slotUpdateTotal)
        self.ui.comboBox_price.editTextChanged.connect(self.slotUpdateTotal)
        self.ui.dateEdit.setDate(QDate.currentDate())        
        #�����¼���ؼ�
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

    '''��ʼ�����������б�ؼ�'''
    def __initTableWidget(self):
        self.ui.tableView.setLineWidth(50)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        '''
        ���ó������Ʒ�����Ҽ��˵�
        '''
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.slotTreeWidgetContextMenu)
        self.ui.tableView.setToolTip(u'��DELETE��ɾ��')
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDeleteRecordItem()
            return
        return QDialog.keyPressEvent(event)
    '''
    �ӻ�����ɾ����Ŀ
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

    ''' ��ջ����б���'''
    def slotClearlist(self):
        if QMessageBox.warning(self, u'ɾ����ʾ', u'ȷ����ջ�������ô?�㽫��Ҫ������Ӽ�¼!', QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            self.__recordList = []
            self.slotUpdateList()
    '''�Զ���������ܽ��ؼ��е�����'''
    def slotUpdateTotal(self):
        try:
            count = float(self.ui.lineEdit_count.text())
            price = float(self.ui.lineEdit_price.text())
            total = count*price
            self.ui.lineEdit.setText('%f'%total)
        except:
            self.ui.lineEdit.setText('')
    '''��������'''
    def slotReset(self):
        self.ui.lineEdit_articlename.setText('')
        self.ui.lineEdit_count.setText('1.0')
        self.ui.lineEdit_price.setText('1.0')

    '''�����������û�ѡ����Ʒ,����ʾ�������'''
    def slotArticleMs(self):
        dlg = DlgArticle(self, True)
        dlg.setModal(True)
        '''δѡ���κ���Ʒ'''
        if QDialog.Accepted != dlg.exec_():
            #print 'not accepted'
            return
        self.__article = dlg.getSelectedArticle()
        if self.__article == None: return
        #�����������ȷ����Ʒ��Ϣ
        self.ui.lineEdit_articlename.setText(self.__article.model)
        self.ui.label_unit.setText(self.__article.unit)
        remainList = dbArticle().getSpecArticleRemainList(self.__article.id)
        if len(remainList) > 0:
            remainInfo = remainList[0]
            self.ui.lineEdit_remain.setText('%f'%remainInfo.remainCount)
        else:
            self.ui.lineEdit_remain.setText(u'0')
        #���¼۸��б�
        priceList = dbInOutRecord().getSpecArticlePriceList(self.__article.id)
        self.ui.comboBox_price.clear()
        for price in priceList: self.ui.comboBox_price.addItem(u'%.2f'%price)
        self.ui.comboBox_price.setCurrentIndex(0)
        self.ui.comboBox_price.setEditable(True)

       
    '''�����������û�ѡ��ͻ�����'''
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
    �Ҽ������˵�,����ɾ��
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
        action_del = QAction(u'ɾ��', self)
        action_del.triggered.connect(self.slotDeleteRecordItem)
        menuPop.addAction(action_del)
        menuPop.exec_(QCursor.pos())
        
    '''
    �Զ����ɻ�����
    '''
    def slotGenNumber(self):       
        self.ui.lineEdit_number.setText( QString(str(datetime.now())))

    '''
    ��ӵ���������¼������б�
    '''
    def slotAddToList(self):
        if self.__article is None:
            self.ui.label_tips.setText(u'''<span style='color:#ff0000'>δѡ�������Ʒ�ͺ�</span>''')
            return
        record = InOutRecord()
        record.articleid = self.__article.id
        record.model = self.__article.model
        record.count = float(self.ui.lineEdit_count.text())
        '''����ǳ���'''
        if self.ui.radioButton_out.isChecked():
            record.count = -record.count
            '''�����ͳ�����'''
            remainCount = float(self.ui.lineEdit_remain.text())
            if remainCount <= 0 or record.count < -remainCount:
                self.ui.label_tips.setText(u'''<span style='color:#ff0000'>���������������</span>''')
                return
        record.detail = u'%s'%self.ui.textEdit_detail.toPlainText()
        record.price  = float(self.ui.comboBox_price.currentText())
        record.time = self.ui.dateEdit.text()
        if self.__client != None:
            record.clientid = self.__client.id
        '''����Ƿ�����ͬ����Ʒ(ͬid,ͬ�۸����Ʒ���б���)'''
        sameRecord = None
        for rec in self.__recordList:
            if rec.articleid == record.articleid:
                sameRecord = rec
        if sameRecord == None:
            self.__recordList.append(record)
        else:
            res = QMessageBox.warning(self, u'����', u'���������д���Ʒ,�Ƿ���кϲ�?',
                                 QMessageBox.Yes|QMessageBox.No)
            if res == QMessageBox.Yes:
                sameRecord.count = record.count + sameRecord.count
            else:
                return
        '''������ⵥ�е���Ʒ�б�'''
        self.slotUpdateList()

    '''#�ύ���'''
    def slotSubmit(self):
        number = self.ui.lineEdit_number.text()
        if number == '':
            QMessageBox.warning(self, u'error', u'�����Ų���Ϊ��')
            return
        '''�����г������Ʒ�б���Ϊ��'''
        if len(self.__recordList) <= 0:
            return
        '''�޸ļ�¼�еĻ����ź�����'''
        for rec in self.__recordList:
            rec.time = self.ui.dateEdit.text()
            rec.number = number
                        
        if not dbInOutRecord().addRecords(self.__recordList):
            QMessageBox.warning(self, u'error', u'���ʧ��,����������')
        else:
            QMessageBox.information(self, u'error', u'����¼�Ѹ���')
            self.__recordList = []
            self.slotUpdateList()
    '''
    ������Ʒ�б�
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
        '''���ñ���ͷ'''
        labels = QStringList()
        labels.append(u'��Ʒid')        
        labels.append(u'��Ʒ����')        
        labels.append(u'����')        
        labels.append(u'����')        
        labels.append(u'˵��')
        model.setHorizontalHeaderLabels(labels)
        '''�����и�'''
        for i in range(model.rowCount()):
            self.ui.tableView.setRowHeight(i, 20)
        '''�����п�'''
        self.ui.tableView.setColumnWidth(0, 50)
        self.ui.tableView.setColumnWidth(4, 250)
        #�������,�ύ��ť�Ŀ�����
        self.ui.pushButton_Submit.setEnabled(len(self.__recordList) > 0)
        self.ui.pushButton_clear.setEnabled(len(self.__recordList) > 0)


    '''�����������û�ѡ����Ʒ�ͺ�'''
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
