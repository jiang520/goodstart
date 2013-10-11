#encoding=gb2312
__author__ = 'jiang'


import sys
import sys
from ims.model.dbSysUser import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.ui.uiDlgSysUserAdmin import  Ui_Dialog
class DlgSysUserAdmin(QDialog):
    def __init__(self,parent, bUsedForChooseClient=False):
        super(QDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.groupBox.setHidden(True)
        self.__update_userlist()

        self.ui.comboBox_usertype.addItem(u'管理员')
        self.ui.comboBox_usertype.addItem(u'游客')
        self.ui.pushButton_add.clicked.connect(self.slotAdd)
        self.ui.pushButton_modify.clicked.connect(self.slotModify)
        self.ui.pushButton_del.clicked.connect(self.slotDel)
        self.ui.pushButton_cancel.clicked.connect(self.slotCancel)


    def __update_userlist(self):
        userlist = dbSysUser().get_all_users()
        if userlist == None: return
        model = QStandardItemModel(len(userlist), 3, self)
        for i in range(len(userlist)):
            userinfo = userlist[i]
            model.setItem(i, 0, QStandardItem(u'%d'%userinfo.id))
            model.setItem(i, 1, QStandardItem(u'%s'%userinfo.username))
            model.setItem(i, 2, QStandardItem(u'%s'%userinfo.usertype))
        strHeaders = QStringList()
        strHeaders.append(u'ID')
        strHeaders.append(u'用户名')
        strHeaders.append(u'用户类型')

        model.setHorizontalHeaderLabels(strHeaders)
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(2, 180)

    def slotAdd(self):
        self.ui.groupBox.show()
        self.ui.pushButton_ok.setText(u'添加')

    def slotModify(self):
        self.ui.groupBox.show()
        self.ui.pushButton_ok.setText(u'修改')
        pass
    def slotDel(self):
        model = self.ui.tableView.model()

    def slotOk(self):
        if self.ui.pushButton_ok.text()==u'添加':
            user = SysUser()
            user.username = u'%s'%self.ui.lineEdit_username.text()
            user.password = u'%s'%self.ui.lineEdit_password.text()
            user.usertype = u'%s'%self.ui.comboBox_usertype.currentText()
            if dbSysUser().addUser(user):
                self.ui.groupBox.hide()
                self.__update_userlist()
            else:
                QMessageBox.critical(self,u'error',u'Add failed')
        else:
            user = SysUser()
            user.username = u'%s'%self.ui.lineEdit_username.text()
            user.password = u'%s'%self.ui.lineEdit_password.text()
            user.usertype = u'%s'%self.ui.comboBox_usertype.currentText()
            if dbSysUser().modifyUser(user):
                self.ui.groupBox.hide()
                self.__update_userlist()
            else:
                QMessageBox.critical(self,u'error',u'Add failed')

    def slotCancel(self):
        self.ui.groupBox.hide()


if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgSysUserAdmin(None)
    window.show()
    appp.exec_()