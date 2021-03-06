#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''

from PyQt4.QtGui import *
from PyQt4.Qt import  *
import sys
from ims.DlgIMSMain import DlgIMSMain
from ims.model.dbSysUser import *
from ims.model.SysConfigFile import *
from ims.ui.uiDlgLogin import *
import ims
from ims.model.SysConfigFile import g_configfile

class DlgLogin(QDialog):
    '''
    classdocs
    '''
    def __init__(self,parent=None, bUsedForChooseClient=False):
        super(QDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.setWindowTitle(u'欢迎使用')
        self.__initUserNameList()
        self.ui.pushButton_load.setDefault(True)
        self.ui.lineEdit_pass.setEchoMode(QLineEdit.Password)
        self.ui.checkBox_autoload.hide()
        self.ui.checkBox_recordpass.hide()
        #self.ui.commandLinkButton_register.clicked.connect(self.slotRegister)
        self.ui.pushButton_load.clicked.connect(self.slotLogin)
        self.setStyleSheet(u"QDialog{ border-image : url('images/bkgnd.jpg')}" );
        self.setFixedSize(500, 320)

    #初始化用户名列表
    def __initUserNameList(self):
        font = QFont()
        font.setFamily(u'微软雅黑')
        font.setPixelSize(13)
        font.setBold(True)
        self.ui.comboBox_username.setFont(font)
        self.ui.lineEdit_pass.setFont(font)

        usernames = g_configfile.getUserList()
        for name in usernames:
            self.ui.comboBox_username.insertItem(0, name)
        self.ui.lineEdit_pass.setText(u'5950ut')
    def slotRegister(self):
        QMessageBox.critical(self, u'error', u'暂时不提供注册')
        pass

    def slotLogin(self):
        strUserName = u'%s'%self.ui.comboBox_username.currentText()
        strPass     = u'%s'%self.ui.lineEdit_pass.text()
        if strUserName == '':
            self.ui.comboBox_username.setFocus()
            return
        if strPass == '':
            self.ui.lineEdit_pass.setFocus()
            return
        userinfo = SysUser()
        userinfo.username = strUserName
        userinfo.password = strPass
        g_configfile.addUserName(userinfo.username)
        res = dbSysUser().isValidUser(userinfo)
        if not res:
            QMessageBox.critical(self, u'info', u'帐户或密码输误错误')
            self.ui.lineEdit_pass.setFocus()
        else:
            ims.model.dbSysUser.g_current_user = dbSysUser().get_user_by_username(userinfo.username)
            self.accept()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = DlgLogin(None)
    window.show()
    app.exec_()