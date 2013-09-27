# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgArticle.ui'
#
# Created: Fri Sep 27 17:31:29 2013
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
        Dialog.resize(599, 372)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_type = QtGui.QComboBox(self.groupBox)
        self.comboBox_type.setObjectName(_fromUtf8("comboBox_type"))
        self.gridLayout.addWidget(self.comboBox_type, 2, 1, 1, 1)
        self.pushButton_addtype = QtGui.QPushButton(self.groupBox)
        self.pushButton_addtype.setObjectName(_fromUtf8("pushButton_addtype"))
        self.gridLayout.addWidget(self.pushButton_addtype, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_pkg = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pkg.setObjectName(_fromUtf8("lineEdit_pkg"))
        self.gridLayout.addWidget(self.lineEdit_pkg, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEdit_function = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_function.setObjectName(_fromUtf8("lineEdit_function"))
        self.gridLayout.addWidget(self.lineEdit_function, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEdit_detail = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_detail.setObjectName(_fromUtf8("lineEdit_detail"))
        self.gridLayout.addWidget(self.lineEdit_detail, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_add = QtGui.QPushButton(Dialog)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "物品信息:", None))
        self.label.setText(_translate("Dialog", "唯一名称:", None))
        self.label_5.setText(_translate("Dialog", "已存在", None))
        self.label_2.setText(_translate("Dialog", "型号:", None))
        self.label_4.setText(_translate("Dialog", "非法输入", None))
        self.label_3.setText(_translate("Dialog", "类别:", None))
        self.pushButton_addtype.setText(_translate("Dialog", "新增类别", None))
        self.label_6.setText(_translate("Dialog", "封装:", None))
        self.label_7.setText(_translate("Dialog", "用途:", None))
        self.label_8.setText(_translate("Dialog", "备注:", None))
        self.lineEdit_detail.setText(_translate("Dialog", "详细:", None))
        self.pushButton_add.setText(_translate("Dialog", "添加并继续", None))
        self.pushButton_cancel.setText(_translate("Dialog", "退出", None))

