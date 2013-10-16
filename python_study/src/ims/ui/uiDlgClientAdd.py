# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgClientAdd.ui'
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
        Dialog.resize(462, 300)
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
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_phone = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phone.sizePolicy().hasHeightForWidth())
        self.lineEdit_phone.setSizePolicy(sizePolicy)
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.horizontalLayout_4.addWidget(self.lineEdit_phone)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.comboBox_clienttype = QtGui.QComboBox(Dialog)
        self.comboBox_clienttype.setMinimumSize(QtCore.QSize(135, 0))
        self.comboBox_clienttype.setEditable(True)
        self.comboBox_clienttype.setObjectName(_fromUtf8("comboBox_clienttype"))
        self.horizontalLayout_6.addWidget(self.comboBox_clienttype)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_boss = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_boss.sizePolicy().hasHeightForWidth())
        self.lineEdit_boss.setSizePolicy(sizePolicy)
        self.lineEdit_boss.setObjectName(_fromUtf8("lineEdit_boss"))
        self.horizontalLayout.addWidget(self.lineEdit_boss)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_mobile = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_mobile.sizePolicy().hasHeightForWidth())
        self.lineEdit_mobile.setSizePolicy(sizePolicy)
        self.lineEdit_mobile.setObjectName(_fromUtf8("lineEdit_mobile"))
        self.horizontalLayout.addWidget(self.lineEdit_mobile)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
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
        self.label.setText(_translate("Dialog", "公司名称:", None))
        self.label_6.setText(_translate("Dialog", "地    址:", None))
        self.label_2.setText(_translate("Dialog", "电    话:", None))
        self.label_7.setText(_translate("Dialog", "客户类型:", None))
        self.label_3.setText(_translate("Dialog", "联 系 人:", None))
        self.label_4.setText(_translate("Dialog", "手机:", None))
        self.label_5.setText(_translate("Dialog", "备注:", None))
        self.pushButton_ok.setText(_translate("Dialog", "提交", None))
        self.pushButton_cancel.setText(_translate("Dialog", "取消", None))

