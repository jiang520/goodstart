# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgLogin.ui'
#
# Created: Sat Oct 12 00:02:50 2013
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
        Dialog.resize(400, 224)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 20, 291, 141))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox_username = QtGui.QComboBox(self.groupBox)
        self.comboBox_username.setGeometry(QtCore.QRect(40, 30, 200, 31))
        self.comboBox_username.setEditable(True)
        self.comboBox_username.setObjectName(_fromUtf8("comboBox_username"))
        self.lineEdit_pass = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pass.setGeometry(QtCore.QRect(40, 70, 200, 30))
        self.lineEdit_pass.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_pass.setObjectName(_fromUtf8("lineEdit_pass"))
        self.checkBox_recordpass = QtGui.QCheckBox(self.groupBox)
        self.checkBox_recordpass.setGeometry(QtCore.QRect(60, 110, 71, 16))
        self.checkBox_recordpass.setObjectName(_fromUtf8("checkBox_recordpass"))
        self.checkBox_autoload = QtGui.QCheckBox(self.groupBox)
        self.checkBox_autoload.setGeometry(QtCore.QRect(140, 110, 71, 16))
        self.checkBox_autoload.setObjectName(_fromUtf8("checkBox_autoload"))
        self.pushButton_load = QtGui.QPushButton(Dialog)
        self.pushButton_load.setGeometry(QtCore.QRect(100, 170, 151, 41))
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.commandLinkButton_register = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton_register.setGeometry(QtCore.QRect(260, 170, 111, 41))
        self.commandLinkButton_register.setObjectName(_fromUtf8("commandLinkButton_register"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox_recordpass.setText(_translate("Dialog", "记住密码", None))
        self.checkBox_autoload.setText(_translate("Dialog", "自动登录", None))
        self.pushButton_load.setText(_translate("Dialog", "登        录", None))
        self.commandLinkButton_register.setText(_translate("Dialog", "注册", None))

