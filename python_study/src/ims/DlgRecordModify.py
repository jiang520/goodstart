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
        self.ui.lineEdit_articlename.setEnabled(False)
        #�����ź����
        self.ui.pushButton_new.clicked.connect(self.slotSelectArticle)
        self.ui.pushButton_addtolist.clicked.connect(self.slotModifyRecord)
        self.ui.pushButton_selectclient.clicked.connect(self.slotSelectClient)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.ui.pushButton_reset.clicked.connect(self.slotReset)
        self.__article = None
        self.__client = None
        self.__oldRecord = oldRecord
        self.setRecord(oldRecord)
    '''��������ѡ����Ʒ��Ϣ'''
    def slotSelectArticle(self):
        dlg = DlgArticle(self, True)
        dlg.setModal(True)
        if QDialog.Accepted!=dlg.exec_():
            return
        self.__article = dlg.getSelectedArticle()
        self.ui.lineEdit_articlename.setText(self.__article.model)

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
        articleInfo = dbArticle().getById(oldRecord.articleid)
        #��Ʒ��Ϣ��ʼֵ
        if articleInfo!=None:
            self.ui.lineEdit_articlename.setText(articleInfo.model)
        else:
            self.ui.lineEdit_articlename.setText('')
        self.ui.lineEdit_count.setText('%f'%abs(oldRecord.count))
        self.ui.lineEdit_price.setText('%.2f'%oldRecord.price)
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

    #������������Ϣ��Ϣ
    def slotModifyRecord(self):
        record = InOutRecord()
        record.id = self.__oldRecord.id
        #����޸�����Ʒid
        if self.__article != None: record.articleid = self.__article.id
        #����޸��˿ͻ�id
        if self.__client != None: record.clientid = self.__client.id
        #У���۸�����������Ƿ���ȷ
        str_count = u'%s'%self.ui.lineEdit_count.text()
        str_count = str_count.strip()
        str_price = u'%s'%self.ui.lineEdit_price.text()
        str_price = str_price.strip()
        if str_count=='':
            self.ui.label_tips.setText(u'''<span style='color:#ff0000'>δ��������</span>''')
            return
        if str_price =='':
            self.ui.label_tips.setText(u'''<span style='color:#ff0000'>δ����۸�</span>''')
            return
        #��������ת��
        try:
            record.count     = float(str_count)
            record.price     = float(str_price)
            record.detail    = u'%s'%self.ui.textEdit_detail.toPlainText()
            record.time      = self.ui.dateEdit.text()
            record.number    = u'%s'%self.ui.lineEdit_number.text()
        except Exception,e:
            QMessageBox.critical(self, u'��������',u'���������ʽ����,������������%s'%e)
            return
        #�ύ�����ݿ���и���
        if not dbInOutRecord().modify(record):
            QMessageBox.critical(self, u'error', u'���³�����¼ʧ��,������')
        else:
            self.accept()

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgRecordModify(None)
    window.show()
    appp.exec_()