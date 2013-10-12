#encoding=gb2312
__author__ = 'jiang'


import sys
import sys
from ims.model.dbSysUser import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.ui.uiDlgSysUserAdmin import  Ui_Dialog
class DlgSysUserAdmin(QDialog):
    def __init__(self,parent=None):
        super(QDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.groupBox.setHidden(True)
        self.ui.comboBox_usertype.addItem(u'����Ա')
        self.ui.comboBox_usertype.addItem(u'�ο�')
        self.ui.pushButton_add.clicked.connect(self.slotAdd)
        self.ui.pushButton_modify.clicked.connect(self.slotModify)
        self.ui.pushButton_del.clicked.connect(self.slotDel)
        self.ui.pushButton_cancel.clicked.connect(self.slotCancel)
        self.ui.pushButton_ok.clicked.connect(self.slotOk)
        self.__initTableView()
        self.__update_userlist()
    #��ʼ�����ؼ�����ʽ
    def __initTableView(self):
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
    #�����û��б�
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
        strHeaders.append(u'�û���')
        strHeaders.append(u'�û�����')

        model.setHorizontalHeaderLabels(strHeaders)
        self.ui.tableView.setModel(model)
        self.ui.tableView.setColumnWidth(2, 180)
        for i in range(len(userlist)):
            self.ui.tableView.setRowHeight(i, 20)
    #���'����û�'��ť
    def slotAdd(self):
        self.ui.groupBox.show()
        self.ui.pushButton_ok.setText(u'���')
        self.ui.lineEdit_username.setText(u'')
        self.ui.lineEdit_password.setText(u'')
    #���'�޸��û�'��ť
    def slotModify(self):
        cur_index = self.ui.tableView.currentIndex()
        if cur_index is None: return
        if cur_index.row() < 0 : return
        model = self.ui.tableView.model()
        name_data = u'%s'%model.index(cur_index.row(), 1).data().toString()
        type_data = u'%s'%model.index(cur_index.row(), 2).data().toString()
        self.__oldUserInfo = SysUser()
        self.__oldUserInfo.username = name_data
        self.__oldUserInfo.usertype = type_data
        self.ui.tableView.setEnabled(False)
        self.ui.pushButton_add.setEnabled(False)
        self.ui.pushButton_modify.setEnabled(False)
        self.ui.pushButton_del.setEnabled(False)
        self.ui.groupBox.show()
        self.ui.lineEdit_username.setText(self.__oldUserInfo.username)
        self.ui.comboBox_usertype.setEditText(self.__oldUserInfo.usertype)
        self.ui.pushButton_ok.setText(u'�޸�')

    #���'ɾ���û�'��ť
    def slotDel(self):
        cur_index = self.ui.tableView.currentIndex()
        if cur_index is None: return
        if cur_index.row() < 0: return
        model = self.ui.tableView.model()
        name_data = model.index(cur_index.row(), 1).data()
        print name_data
        data = name_data.toString()
        if not dbSysUser().deleteUser(u'%s'%data):
            QMessageBox.critical(self, u'error', u'ɾ���û�ʧ��')
        else:
            self.__update_userlist()


    #����ȷ�����޸Ļ����һ���û�
    def slotOk(self):
        user = SysUser()
        user.username = u'%s'%self.ui.lineEdit_username.text()
        user.password = u'%s'%self.ui.lineEdit_password.text()
        user.usertype = u'%s'%self.ui.comboBox_usertype.currentText()
        if  len(user.username)<1:
            self.ui.lineEdit_username.setFocus()
            return
        if len(user.password)<4:
            QMessageBox.critical(self, u'error', u'���벻��С��4λ')
            self.ui.lineEdit_password.setFocus()
            return

        if self.ui.pushButton_ok.text()==u'���':
            if dbSysUser().addUser(user):
                self.ui.groupBox.hide()
                self.__update_userlist()
            else:
                QMessageBox.critical(self,u'error',u'Add failed')
        else:

            if dbSysUser().modifyUser(self.__oldUserInfo.username, user):
                self.ui.groupBox.hide()
                self.__update_userlist()
            else:
                QMessageBox.critical(self,u'error',u'Add failed')
        self.ui.tableView.setEnabled(True)

    #ȡ�����/�޸��û���Ϣ
    def slotCancel(self):
        self.ui.groupBox.hide()
        self.ui.tableView.setEnabled(True)
        self.ui.pushButton_add.setEnabled(True)
        self.ui.pushButton_modify.setEnabled(True)
        self.ui.pushButton_del.setEnabled(True)


if __name__ == "__main__":
    appp = QApplication(sys.argv)
    window = DlgSysUserAdmin(None)
    window.show()
    appp.exec_()