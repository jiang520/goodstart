# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgArticle.ui'
#
# Created: Mon Oct 07 22:48:47 2013
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
        Dialog.resize(599, 371)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(396, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_setedit = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_setedit.sizePolicy().hasHeightForWidth())
        self.checkBox_setedit.setSizePolicy(sizePolicy)
        self.checkBox_setedit.setObjectName(_fromUtf8("checkBox_setedit"))
        self.horizontalLayout.addWidget(self.checkBox_setedit)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ok.sizePolicy().hasHeightForWidth())
        self.pushButton_ok.setSizePolicy(sizePolicy)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_pkg = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pkg.setObjectName(_fromUtf8("lineEdit_pkg"))
        self.gridLayout.addWidget(self.lineEdit_pkg, 3, 1, 1, 1)
        self.pushButton_addtype1 = QtGui.QPushButton(self.groupBox)
        self.pushButton_addtype1.setObjectName(_fromUtf8("pushButton_addtype1"))
        self.gridLayout.addWidget(self.pushButton_addtype1, 0, 2, 1, 1)
        self.comboBox_type2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_type2.setObjectName(_fromUtf8("comboBox_type2"))
        self.gridLayout.addWidget(self.comboBox_type2, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.lineEdit_model = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_model.setObjectName(_fromUtf8("lineEdit_model"))
        self.gridLayout.addWidget(self.lineEdit_model, 2, 1, 1, 1)
        self.pushButton_add = QtGui.QPushButton(self.groupBox)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.gridLayout.addWidget(self.pushButton_add, 9, 1, 1, 1)
        self.comboBox_type1 = QtGui.QComboBox(self.groupBox)
        self.comboBox_type1.setObjectName(_fromUtf8("comboBox_type1"))
        self.gridLayout.addWidget(self.comboBox_type1, 0, 1, 1, 1)
        self.pushButton_addtype2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_addtype2.setObjectName(_fromUtf8("pushButton_addtype2"))
        self.gridLayout.addWidget(self.pushButton_addtype2, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_tips = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tips.sizePolicy().hasHeightForWidth())
        self.label_tips.setSizePolicy(sizePolicy)
        self.label_tips.setText(_fromUtf8(""))
        self.label_tips.setObjectName(_fromUtf8("label_tips"))
        self.gridLayout.addWidget(self.label_tips, 8, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_pp = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pp.setObjectName(_fromUtf8("lineEdit_pp"))
        self.gridLayout.addWidget(self.lineEdit_pp, 5, 1, 1, 1)
        self.lineEdit_function = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_function.setObjectName(_fromUtf8("lineEdit_function"))
        self.gridLayout.addWidget(self.lineEdit_function, 4, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 1, 1, 1)
        self.textEdit_detail = QtGui.QTextEdit(self.groupBox)
        self.textEdit_detail.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit_detail.setObjectName(_fromUtf8("textEdit_detail"))
        self.gridLayout.addWidget(self.textEdit_detail, 6, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox_setedit.setText(_translate("Dialog", "编辑", None))
        self.pushButton_ok.setText(_translate("Dialog", "选中", None))
        self.pushButton_cancel.setText(_translate("Dialog", "退出", None))
        self.treeWidget.setSortingEnabled(True)
        self.groupBox.setTitle(_translate("Dialog", "物品信息:", None))
        self.label.setText(_translate("Dialog", "大类名", None))
        self.pushButton_addtype1.setText(_translate("Dialog", "新增", None))
        self.pushButton_add.setText(_translate("Dialog", "修改", None))
        self.pushButton_addtype2.setText(_translate("Dialog", "新增", None))
        self.label_8.setText(_translate("Dialog", "备注:", None))
        self.label_2.setText(_translate("Dialog", "型号:", None))
        self.label_10.setText(_translate("Dialog", "品牌:", None))
        self.label_3.setText(_translate("Dialog", "用途:", None))
        self.label_6.setText(_translate("Dialog", "封装:", None))
        self.lineEdit_pp.setText(_translate("Dialog", "详细:", None))
        self.label_9.setText(_translate("Dialog", "小类名", None))

