# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgLogin.ui'
#
# Created: Sun Oct 13 20:54:30 2013
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
        Dialog.resize(542, 291)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 133, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_username = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_username.sizePolicy().hasHeightForWidth())
        self.comboBox_username.setSizePolicy(sizePolicy)
        self.comboBox_username.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox_username.setEditable(True)
        self.comboBox_username.setObjectName(_fromUtf8("comboBox_username"))
        self.verticalLayout.addWidget(self.comboBox_username)
        self.lineEdit_pass = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_pass.sizePolicy().hasHeightForWidth())
        self.lineEdit_pass.setSizePolicy(sizePolicy)
        self.lineEdit_pass.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_pass.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_pass.setObjectName(_fromUtf8("lineEdit_pass"))
        self.verticalLayout.addWidget(self.lineEdit_pass)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_recordpass = QtGui.QCheckBox(self.widget)
        self.checkBox_recordpass.setObjectName(_fromUtf8("checkBox_recordpass"))
        self.horizontalLayout_2.addWidget(self.checkBox_recordpass)
        self.checkBox_autoload = QtGui.QCheckBox(self.widget)
        self.checkBox_autoload.setObjectName(_fromUtf8("checkBox_autoload"))
        self.horizontalLayout_2.addWidget(self.checkBox_autoload)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_load = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox_recordpass.setText(_translate("Dialog", "记住密码", None))
        self.checkBox_autoload.setText(_translate("Dialog", "自动登录", None))
        self.pushButton_load.setText(_translate("Dialog", "登        录", None))

