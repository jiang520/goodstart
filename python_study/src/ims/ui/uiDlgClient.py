# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgClient.ui'
#
# Created: Mon Oct 07 22:48:48 2013
#      by: PyQt4 UI code generator 4.10.3
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
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_add = QtGui.QPushButton(Dialog)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_modify = QtGui.QPushButton(Dialog)
        self.pushButton_modify.setObjectName(_fromUtf8("pushButton_modify"))
        self.horizontalLayout.addWidget(self.pushButton_modify)
        self.pushButton_del = QtGui.QPushButton(Dialog)
        self.pushButton_del.setObjectName(_fromUtf8("pushButton_del"))
        self.horizontalLayout.addWidget(self.pushButton_del)
        self.pushButton_export = QtGui.QPushButton(Dialog)
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.horizontalLayout.addWidget(self.pushButton_export)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_add.setText(_translate("Dialog", "新增", None))
        self.pushButton_modify.setText(_translate("Dialog", "修改", None))
        self.pushButton_del.setText(_translate("Dialog", "移除", None))
        self.pushButton_export.setText(_translate("Dialog", "导出", None))

