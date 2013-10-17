#encoding=gb2312
'''
Created on 2013-10-4

@author: jiang
'''
from ui import uiDlgArticle
import sys

from PyQt4.QtCore import *
from ims.ui.uiDlgClientAdd import *
from PyQt4.QtGui import *
from ims.model.dbClient import *
from ims.ui import uiDlgClientAdd
from ims.model.SysConfigFile import *
class DlgClientAdd(QDialog):
    __oldclientInfo = None

    '''��ʼ������'''
    def __init__(self,parent, oldClinet=None):
        super(DlgClientAdd,self).__init__(parent)                
        self.ui = uiDlgClientAdd.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_cancel.clicked.connect(self.__slotCancel)
        self.ui.pushButton_ok.clicked.connect(self.__slotOk)
        #��ʼ���ͻ������б�
        client_type_list = g_configfile.getClientTypesu()
        for name in client_type_list:  self.ui.comboBox_clienttype.addItem(name)

        #������޸Ŀͻ���Ϣ,�����ó�ֵ
        if oldClinet != None:
            self.__oldclientInfo = oldClinet
            self.ui.comboBox_clienttype.setEditText(oldClinet.type)
            self.ui.lineEdit_address.setText(oldClinet.address)
            self.ui.lineEdit_boss.setText(oldClinet.boss)
            self.ui.lineEdit_mobile.setText(oldClinet.mobile)
            self.ui.lineEdit_name.setText(oldClinet.name)
            self.ui.lineEdit_phone.setText(oldClinet.phone)
            self.ui.textEdit_detail.setText(oldClinet.detail)
            self.setWindowTitle(u'�޸Ŀͻ���Ϣ[id=%d'%self.__oldclientInfo.id)
        else:
            self.setWindowTitle(u'��ӿͻ���Ϣ')

    ''' ���ok�����޸Ļ���ӿͻ���Ϣ'''
    def __slotOk(self):
        client = Client()
        client.address= u'%s'%self.ui.lineEdit_address.text()
        client.boss   = u'%s'%self.ui.lineEdit_boss.text()
        client.detail = u'%s'%self.ui.textEdit_detail.toPlainText()
        client.mobile = u'%s'%self.ui.lineEdit_mobile.text()
        client.name   = u'%s'%self.ui.lineEdit_name.text()
        client.phone  = u'%s'%self.ui.lineEdit_phone.text()
        client.type   = u'%s'%self.ui.comboBox_clienttype.currentText()
        #У���ͻ���Ϣ�Ƿ�Ϸ�,�ͻ��������벻��Ϊ��
        client.name = client.name.lstrip()
        client.name = client.name.rstrip()
        #��ӿͻ�����
        g_configfile.addClientTypes(client.type)
        #�ͻ����Ʋ���Ϊ��
        if client.name == '':
            QMessageBox.critical(self, u'error', u'��˾����/��λ���Ʋ���Ϊ��')
            self.ui.lineEdit_name.setFocus()
            return
        if self.__oldclientInfo == None:
            #��ӿͻ���Ϣ'''
            if not dbClient().insert(client):
                QMessageBox.critical(self, u'error', u'��ӿͻ���ʧ��!')
            else:
                self.close()
        else:
            #�޸Ŀͻ���Ϣ'''
            if not dbClient().modify(self.__oldclientInfo.id, client):
                QMessageBox.critical(self, u'error', u'�޸Ŀͻ���Ϣʧ��!')
            else:
                self.close()

    ''' �˳����� '''
    def __slotCancel(self):
        self.close()
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgClientAdd(None)
    window.setModal(True)
    window.show()
    sys.exit(appp.exec_())