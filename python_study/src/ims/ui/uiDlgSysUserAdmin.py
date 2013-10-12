# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgSysUserAdmin.ui'
#
# Created: Sat Oct 12 16:39:30 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 334)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_add = QtGui.QPushButton(Dialog)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout_5.addWidget(self.pushButton_add)
        self.pushButton_modify = QtGui.QPushButton(Dialog)
        self.pushButton_modify.setObjectName(_fromUtf8("pushButton_modify"))
        self.horizontalLayout_5.addWidget(self.pushButton_modify)
        self.pushButton_del = QtGui.QPushButton(Dialog)
        self.pushButton_del.setObjectName(_fromUtf8("pushButton_del"))
        self.horizontalLayout_5.addWidget(self.pushButton_del)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tableView = QtGui.QTableView(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_username = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_username.setSizePolicy(sizePolicy)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.label_tip_username = QtGui.QLabel(self.groupBox)
        self.label_tip_username.setText(_fromUtf8(""))
        self.label_tip_username.setObjectName(_fromUtf8("label_tip_username"))
        self.horizontalLayout.addWidget(self.label_tip_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.label_tip_password = QtGui.QLabel(self.groupBox)
        self.label_tip_password.setText(_fromUtf8(""))
        self.label_tip_password.setObjectName(_fromUtf8("label_tip_password"))
        self.horizontalLayout_2.addWidget(self.label_tip_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_usertype = QtGui.QComboBox(self.groupBox)
        self.comboBox_usertype.setObjectName(_fromUtf8("comboBox_usertype"))
        self.horizontalLayout_3.addWidget(self.comboBox_usertype)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_ok = QtGui.QPushButton(self.groupBox)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout_4.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(self.groupBox)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_4.addWidget(self.pushButton_cancel)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_add.setText(_translate("Dialog", "新增用户", None))
        self.pushButton_modify.setText(_translate("Dialog", "修改", None))
        self.pushButton_del.setText(_translate("Dialog", "删除", None))
        self.groupBox.setTitle(_translate("Dialog", "用户信息", None))
        self.label.setText(_translate("Dialog", "帐 户 名:", None))
        self.label_2.setText(_translate("Dialog", "密    码:", None))
        self.label_3.setText(_translate("Dialog", "用户类型:", None))
        self.pushButton_ok.setText(_translate("Dialog", "提交", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))
        self.label_4.setText(_translate("Dialog", "              ", None))

