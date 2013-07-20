# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormImage.ui'
#
# Created: Thu Jun 06 17:11:30 2013
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

class Ui_FormImage(object):
    def setupUi(self, FormImage):
        FormImage.setObjectName(_fromUtf8("FormImage"))
        FormImage.resize(400, 300)

        self.retranslateUi(FormImage)
        QtCore.QMetaObject.connectSlotsByName(FormImage)

    def retranslateUi(self, FormImage):
        FormImage.setWindowTitle(_translate("FormImage", "Form", None))

