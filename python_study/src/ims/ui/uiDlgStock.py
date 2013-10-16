# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgStock.ui'
#
# Created: Wed Oct 16 16:58:06 2013
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
        Dialog.resize(610, 489)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.lineEdit_model = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_model.setObjectName(_fromUtf8("lineEdit_model"))
        self.horizontalLayout.addWidget(self.lineEdit_model)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_apply = QtGui.QPushButton(self.groupBox)
        self.pushButton_apply.setObjectName(_fromUtf8("pushButton_apply"))
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.pushButton_reset = QtGui.QPushButton(self.groupBox)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.horizontalLayout.addWidget(self.pushButton_reset)
        self.pushButton_export = QtGui.QPushButton(self.groupBox)
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.horizontalLayout.addWidget(self.pushButton_export)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "过滤器", None))
        self.checkBox.setText(_translate("Dialog", "模糊型号:", None))
        self.pushButton_apply.setText(_translate("Dialog", "应用", None))
        self.pushButton_reset.setText(_translate("Dialog", "重置", None))
        self.pushButton_export.setText(_translate("Dialog", "导出", None))

