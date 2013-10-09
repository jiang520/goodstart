#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from ims.model.dbClient import *
from ims.ui.uiDlgRecordModify import *
from ims.model.dbArticle import dbArticle
from ims.DlgClient import DlgClient
from ims.DlgArticle import DlgArticle
from ims.model.dbInoutRecord import *
class DlgRecordModify(QDialog):
    '''
    classdocs
    '''
    def __init__(self,parent, oldRecord):
        '''
        Constructor
        '''

        super(QDialog,self).__init__(parent)
        self.__client = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(450,300)
        self.setWindowTitle(u'�޸Ľ�������Ϣ')
        '''�������޸Ľ�����ѡ��'''
        self.ui.radioButton_out.setEnabled(False)            
        self.ui.radioButton_in.setEnabled(False)
        #���ý��
        self.ui.label_tips.setText('')
        self.ui.lineEdit_articleid.setEnabled(False)
        self.ui.lineEdit_articlename.setEnabled(False)
        #�����ź����
        self.ui.pushButton_new.clicked.connect(self.slotSelectArticle)
        self.ui.pushButton_addtolist.clicked.connect(self.slotModifyRecord)
        self.ui.pushButton_selectclient.clicked.connect(self.slotSelectClient)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.ui.pushButton_reset.clicked.connect(self.slotReset)
        self.__oldRecord = oldRecord
        self.setRecord(oldRecord)
    '''��������ѡ����Ʒ��Ϣ'''
    def slotSelectArticle(self):
        dlg = DlgArticle(self, True)
        dlg.setModal(True)
        if QDialog.Accepted!=dlg.exec_():
            return
        article = dlg.getSelectedArticle()
        self.ui.lineEdit_articleid.setText(str(article.id))
        self.ui.lineEdit_articlename.setText(article.model)

    '''��������ѡ��ͻ�'''
    def slotSelectClient(self):
        dlg = DlgClient(self, True)
        dlg.setModal(True)
        if QDialog.Accepted != dlg.exec_():
            return
        self.__client = dlg.getChooseClient()
        self.ui.lineEdit_client.setText('[%d]%s'%(self.__client.id,self.__client.name))

    '''����Ϊ�޸�ǰ�Ľ��'''
    def slotReset(self):
        self.setRecord(self.__oldRecord)

    '''����������¼��Ϣ��ӳ��������'''
    def setRecord(self,oldRecord):
        self.ui.lineEdit_articleid.setText('%d'%oldRecord.articleid)
        articleInfo = dbArticle().getById(oldRecord.articleid)
        #��Ʒ��Ϣ��ʼֵ
        if articleInfo!=None:
            self.ui.lineEdit_articlename.setText(articleInfo.model)
        else:
            self.ui.lineEdit_articlename.setText('')
        self.ui.lineEdit_count.setText('%f'%abs(oldRecord.count))
        self.ui.lineEdit_price.setText('%f'%oldRecord.price)
        self.ui.textEdit_detail.setText(oldRecord.detail)
        self.ui.lineEdit_number.setText(QString(oldRecord.number))
        #�ͻ���Ϣ��ʼֵ
        self.__client = dbClient().getById(oldRecord.clientid)
        if self.__client:
            self.ui.lineEdit_client.setText(self.__client.name)
        #��������ʼֵ
        if oldRecord.count < 0:
            self.ui.radioButton_out.setChecked(True)            
            self.ui.radioButton_in.setChecked(False)
        else:        
            self.ui.radioButton_out.setChecked(True)            
            self.ui.radioButton_in.setChecked(False)
        #ʱ���ʼֵ
        dateStrList = oldRecord.time.split('/')
        if len(dateStrList)==3:
            date = QDate(int(dateStrList[0]), int(dateStrList[1]), int(dateStrList[2]))
            self.ui.dateEdit.setDate(date)

    def slotModifyRecord(self):
        record = InOutRecord()
        record.id = self.__oldRecord.id
        strid = self.ui.lineEdit_articleid.text()
        if strid == '' :
            self.ui.label_tips.setText(u'''<span style='color:#ff0000'>δѡ�������Ʒ�ͺ�</span>''')
            return
        record.articleid = int(strid)
        record.model = u'%s'%self.ui.lineEdit_articlename.text()
        record.count = float(self.ui.lineEdit_count.text())
        record.detail = u'%s'%self.ui.textEdit_detail.toPlainText()
        record.price = float(self.ui.lineEdit_price.text())
        record.time = self.ui.dateEdit.text()
        record.number = u'%s'%self.ui.lineEdit_number.text()
        if self.__client != None:
            record.clientid = self.__client.id

        if not dbInOutRecord().modify(record):
            QMessageBox.critical(self, u'error', u'���³�����¼ʧ��,������')
        else:
            self.accept()
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRecordModify(None)
    window.show()
    appp.exec_()