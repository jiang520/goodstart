# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgClientAdd.ui'
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_name = QtGui.QLineEdit(Dialog)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.horizontalLayout_3.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_address = QtGui.QLineEdit(Dialog)
        self.lineEdit_address.setObjectName(_fromUtf8("lineEdit_address"))
        self.horizontalLayout_2.addWidget(self.lineEdit_address)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_boss = QtGui.QLineEdit(Dialog)
        self.lineEdit_boss.setObjectName(_fromUtf8("lineEdit_boss"))
        self.horizontalLayout_4.addWidget(self.lineEdit_boss)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_phone = QtGui.QLineEdit(Dialog)
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.horizontalLayout.addWidget(self.lineEdit_phone)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_mobile = QtGui.QLineEdit(Dialog)
        self.lineEdit_mobile.setObjectName(_fromUtf8("lineEdit_mobile"))
        self.horizontalLayout.addWidget(self.lineEdit_mobile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit_detail = QtGui.QTextEdit(Dialog)
        self.textEdit_detail.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit_detail.setObjectName(_fromUtf8("textEdit_detail"))
        self.verticalLayout.addWidget(self.textEdit_detail)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout_5.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_5.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "公司/单位名称:", None))
        self.label_6.setText(_translate("Dialog", "地  址:", None))
        self.label_3.setText(_translate("Dialog", "联系人:", None))
        self.label_2.setText(_translate("Dialog", "电  话:", None))
        self.label_4.setText(_translate("Dialog", "手机:", None))
        self.label_5.setText(_translate("Dialog", "备注:", None))
        self.pushButton_ok.setText(_translate("Dialog", "提交", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))

