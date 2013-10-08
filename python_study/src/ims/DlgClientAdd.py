#encoding=gb2312
'''
Created on 2013-10-4

@author: jiang
'''
from ui import uiDlgArticle
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.model.dbClient import *
from ims.ui.uiDlgClientAdd import *
from ims.ui import uiDlgClientAdd
class DlgClientAdd(QDialog):
    __oldclientInfo = None

    '''初始化窗口'''
    def __init__(self,parent, oldClinet=None):
        super(DlgClientAdd,self).__init__(parent)                
        self.ui = uiDlgClientAdd.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_cancel.clicked.connect(self.__slotCancel)
        self.ui.pushButton_ok.clicked.connect(self.__slotOk)
        if oldClinet != None:
            self.__oldclientInfo = oldClinet
            self.ui.lineEdit_address.setText(oldClinet.address)
            self.ui.lineEdit_boss.setText(oldClinet.boss)
            self.ui.lineEdit_mobile.setText(oldClinet.mobile)
            self.ui.lineEdit_name.setText(oldClinet.name)
            self.ui.lineEdit_phone.setText(oldClinet.phone)
            self.ui.textEdit_detail.setText(oldClinet.detail)
            self.setWindowTitle(u'修改客户信息[id=%d'%self.__oldclientInfo.id)
        else:
            self.setWindowTitle(u'添加客户信息')

    ''' 点击ok进行修改或添加客户信息'''
    def __slotOk(self):
        client = Client()
        client.address= u'%s'%self.ui.lineEdit_address.text()
        client.boss   = u'%s'%self.ui.lineEdit_boss.text()
        client.detail = u'%s'%self.ui.textEdit_detail.toPlainText()
        client.mobile = u'%s'%self.ui.lineEdit_mobile.text()
        client.name   = u'%s'%self.ui.lineEdit_name.text()
        client.phone  = u'%s'%self.ui.lineEdit_phone.text()
        #校样客户信息是否合法,客户姓名必须不能为空
        client.name = client.name.lstrip()
        client.name = client.name.rstrip()

        if client.name == '':
            QMessageBox.critical(self, u'error', u'公司名称/单位名称不能为空')
            return

        if self.__oldclientInfo == None:
            #添加客户信息'''
            if not dbClient().insert(client):
                QMessageBox.critical(self, u'error', u'添加客户项失败!')
            else:
                self.close()
        else:
            #修改客户信息'''
            if not dbClient().modify(self.__oldclientInfo.id, client):
                QMessageBox.critical(self, u'error', u'修改客户信息失败!')
            else:
                self.close()

    ''' 退出窗口 '''
    def __slotCancel(self):
        self.close()
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgClientAdd(None)
    window.setModal(True)
    window.show()
    sys.exit(appp.exec_())