# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgInOutArticle.ui'
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
        Dialog.resize(596, 511)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_articlename = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_articlename.sizePolicy().hasHeightForWidth())
        self.lineEdit_articlename.setSizePolicy(sizePolicy)
        self.lineEdit_articlename.setObjectName(_fromUtf8("lineEdit_articlename"))
        self.horizontalLayout_8.addWidget(self.lineEdit_articlename)
        self.pushButton_selectArticle = QtGui.QPushButton(self.groupBox)
        self.pushButton_selectArticle.setFlat(False)
        self.pushButton_selectArticle.setObjectName(_fromUtf8("pushButton_selectArticle"))
        self.horizontalLayout_8.addWidget(self.pushButton_selectArticle)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_articleid = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_articleid.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_articleid.sizePolicy().hasHeightForWidth())
        self.lineEdit_articleid.setSizePolicy(sizePolicy)
        self.lineEdit_articleid.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_articleid.setObjectName(_fromUtf8("lineEdit_articleid"))
        self.horizontalLayout_8.addWidget(self.lineEdit_articleid)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lineEdit_remain = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_remain.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_remain.sizePolicy().hasHeightForWidth())
        self.lineEdit_remain.setSizePolicy(sizePolicy)
        self.lineEdit_remain.setObjectName(_fromUtf8("lineEdit_remain"))
        self.horizontalLayout_8.addWidget(self.lineEdit_remain)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_client = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_client.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_client.sizePolicy().hasHeightForWidth())
        self.lineEdit_client.setSizePolicy(sizePolicy)
        self.lineEdit_client.setObjectName(_fromUtf8("lineEdit_client"))
        self.horizontalLayout_3.addWidget(self.lineEdit_client)
        self.pushButton_selectclient = QtGui.QPushButton(self.groupBox)
        self.pushButton_selectclient.setFlat(False)
        self.pushButton_selectclient.setObjectName(_fromUtf8("pushButton_selectclient"))
        self.horizontalLayout_3.addWidget(self.pushButton_selectclient)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_count = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_count.setSizePolicy(sizePolicy)
        self.lineEdit_count.setObjectName(_fromUtf8("lineEdit_count"))
        self.horizontalLayout_2.addWidget(self.lineEdit_count)
        self.label_price = QtGui.QLabel(self.groupBox)
        self.label_price.setObjectName(_fromUtf8("label_price"))
        self.horizontalLayout_2.addWidget(self.label_price)
        self.lineEdit_price = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_price.sizePolicy().hasHeightForWidth())
        self.lineEdit_price.setSizePolicy(sizePolicy)
        self.lineEdit_price.setObjectName(_fromUtf8("lineEdit_price"))
        self.horizontalLayout_2.addWidget(self.lineEdit_price)
        self.label_total = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_total.sizePolicy().hasHeightForWidth())
        self.label_total.setSizePolicy(sizePolicy)
        self.label_total.setObjectName(_fromUtf8("label_total"))
        self.horizontalLayout_2.addWidget(self.label_total)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_in = QtGui.QRadioButton(self.groupBox)
        self.radioButton_in.setObjectName(_fromUtf8("radioButton_in"))
        self.horizontalLayout.addWidget(self.radioButton_in)
        self.radioButton_out = QtGui.QRadioButton(self.groupBox)
        self.radioButton_out.setObjectName(_fromUtf8("radioButton_out"))
        self.horizontalLayout.addWidget(self.radioButton_out)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.textEdit_detail = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_detail.sizePolicy().hasHeightForWidth())
        self.textEdit_detail.setSizePolicy(sizePolicy)
        self.textEdit_detail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit_detail.setObjectName(_fromUtf8("textEdit_detail"))
        self.horizontalLayout_4.addWidget(self.textEdit_detail)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_tips = QtGui.QLabel(self.groupBox)
        self.label_tips.setObjectName(_fromUtf8("label_tips"))
        self.horizontalLayout_6.addWidget(self.label_tips)
        self.pushButton_addtolist = QtGui.QPushButton(self.groupBox)
        self.pushButton_addtolist.setObjectName(_fromUtf8("pushButton_addtolist"))
        self.horizontalLayout_6.addWidget(self.pushButton_addtolist)
        self.pushButton_reset = QtGui.QPushButton(self.groupBox)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.horizontalLayout_6.addWidget(self.pushButton_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_number = QtGui.QLineEdit(Dialog)
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.horizontalLayout_7.addWidget(self.lineEdit_number)
        self.pushButton_gen = QtGui.QPushButton(Dialog)
        self.pushButton_gen.setObjectName(_fromUtf8("pushButton_gen"))
        self.horizontalLayout_7.addWidget(self.pushButton_gen)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_7.addWidget(self.dateEdit)
        self.pushButton_print = QtGui.QPushButton(Dialog)
        self.pushButton_print.setObjectName(_fromUtf8("pushButton_print"))
        self.horizontalLayout_7.addWidget(self.pushButton_print)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.tableView = QtGui.QTableView(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton_Submit = QtGui.QPushButton(Dialog)
        self.pushButton_Submit.setObjectName(_fromUtf8("pushButton_Submit"))
        self.horizontalLayout_5.addWidget(self.pushButton_Submit)
        self.pushButton_clear = QtGui.QPushButton(Dialog)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.horizontalLayout_5.addWidget(self.pushButton_clear)
        self.pushButton_Cancel = QtGui.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.horizontalLayout_5.addWidget(self.pushButton_Cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "物品", None))
        self.label_6.setText(_translate("Dialog", "物品型号:", None))
        self.pushButton_selectArticle.setText(_translate("Dialog", "选择物品", None))
        self.label_8.setText(_translate("Dialog", "物品系统ID:", None))
        self.label_10.setText(_translate("Dialog", "当前库存量:", None))
        self.label_9.setText(_translate("Dialog", "客    户:", None))
        self.pushButton_selectclient.setText(_translate("Dialog", "选择客户", None))
        self.label.setText(_translate("Dialog", "数    量:", None))
        self.label_price.setText(_translate("Dialog", "单    价:", None))
        self.label_total.setText(_translate("Dialog", "总金额", None))
        self.radioButton_in.setText(_translate("Dialog", "进货", None))
        self.radioButton_out.setText(_translate("Dialog", "出货", None))
        self.label_3.setText(_translate("Dialog", "说明:", None))
        self.label_tips.setText(_translate("Dialog", "        this display errors", None))
        self.pushButton_addtolist.setText(_translate("Dialog", "添加到进货单", None))
        self.pushButton_reset.setText(_translate("Dialog", "重置", None))
        self.label_4.setText(_translate("Dialog", "货单号", None))
        self.pushButton_gen.setText(_translate("Dialog", "自动生成", None))
        self.label_5.setText(_translate("Dialog", "日期:", None))
        self.pushButton_print.setText(_translate("Dialog", "打印货单", None))
        self.pushButton_Submit.setText(_translate("Dialog", "提交入库", None))
        self.pushButton_clear.setText(_translate("Dialog", "清空重来", None))
        self.pushButton_Cancel.setText(_translate("Dialog", "取消", None))

