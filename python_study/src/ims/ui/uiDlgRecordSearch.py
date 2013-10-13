# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgRecordSearch.ui'
#
# Created: Sun Oct 13 20:54:31 2013
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
        Dialog.resize(737, 564)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_date = QtGui.QCheckBox(self.groupBox)
        self.checkBox_date.setObjectName(_fromUtf8("checkBox_date"))
        self.horizontalLayout_2.addWidget(self.checkBox_date)
        self.dateEdit_start = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_start.setObjectName(_fromUtf8("dateEdit_start"))
        self.horizontalLayout_2.addWidget(self.dateEdit_start)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.dateEdit_end = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_end.setObjectName(_fromUtf8("dateEdit_end"))
        self.horizontalLayout_2.addWidget(self.dateEdit_end)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.checkBox_model = QtGui.QCheckBox(self.groupBox)
        self.checkBox_model.setObjectName(_fromUtf8("checkBox_model"))
        self.horizontalLayout_3.addWidget(self.checkBox_model)
        self.lineEdit_model = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_model.setObjectName(_fromUtf8("lineEdit_model"))
        self.horizontalLayout_3.addWidget(self.lineEdit_model)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.checkBox_number = QtGui.QCheckBox(self.groupBox)
        self.checkBox_number.setObjectName(_fromUtf8("checkBox_number"))
        self.horizontalLayout.addWidget(self.checkBox_number)
        self.lineEdit_number = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.horizontalLayout.addWidget(self.lineEdit_number)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_apply = QtGui.QPushButton(self.groupBox)
        self.pushButton_apply.setObjectName(_fromUtf8("pushButton_apply"))
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.pushButton_reset = QtGui.QPushButton(self.groupBox)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.horizontalLayout.addWidget(self.pushButton_reset)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = QtGui.QTableView(self.groupBox_2)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "过滤器", None))
        self.checkBox_date.setText(_translate("Dialog", "起止时间", None))
        self.label.setText(_translate("Dialog", "到:", None))
        self.checkBox_model.setText(_translate("Dialog", "模糊型号:", None))
        self.checkBox.setText(_translate("Dialog", "出入库", None))
        self.radioButton.setText(_translate("Dialog", "入库", None))
        self.radioButton_2.setText(_translate("Dialog", "出库", None))
        self.checkBox_number.setText(_translate("Dialog", "货单号", None))
        self.pushButton_apply.setText(_translate("Dialog", "应用", None))
        self.pushButton_reset.setText(_translate("Dialog", "重置", None))

