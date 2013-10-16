#encoding=gb2312
from ims.model.dbArticle import dbArticle

__author__ = 'Administrator'
from PyQt4.QtGui import *
import sys
import ims
from ims.model.dbArticle import *
from ims.model.dbArticleType import *
from ims.ui.uiDlgStock import *
from ims.model.dbInoutRecord import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.FunctionTools import *

class DlgStock(QDialog):
    '''
    classdocs
    '''
    def __init__(self,parent=None):
        super(QDialog,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.setSortingEnabled(True)

        self.ui.pushButton_apply.clicked.connect(self.slotApply)
        self.ui.pushButton_reset.clicked.connect(self.slotReset)
        self.ui.pushButton_export.clicked.connect(self.slotExport)
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.slotContextMenu)

        self.__article_id = None
        self.__updateArticleCountList()

    def setFilterArticleId(self,article_id):
        self.__article_id = article_id
        self.slotApply()

    def slotContextMenu(self):
        action_export = QAction(u'导出',self)
        action_export.triggered.connect(self.slotExport)

        menu = QMenu(u'pop', self)
        menu.addAction(action_export)

        menu.exec_(QCursor.pos())

    def slotExport(self):
        ExportTableToExcel(self.ui.tableView)

    def slotApply(self):
        self.__updateArticleCountList()

    def slotReset(self):
        pass

    def setArticleIdFilter(self, article_id):
        self.__article_id = article_id
        self.__updateArticleCountList()

    #更新物品库存列表
    def __updateArticleCountList(self):
        #是否匹配物品模式
        if self.ui.checkBox.isChecked():
            modelname = u'%s'%self.ui.lineEdit_model.text()
        else:
            modelname = None
        remainlist = dbArticle().getArticleRemainList(self.__article_id, modelname)
        model = QStandardItemModel(len(remainlist),5, self)
        labels = [u'id',u'大类名',u'小类名', u'物品型号', u'库存', u'最新入库单价', u'封装', u'品牌', u'详细说明']
        model.setHorizontalHeaderLabels(QStringList(labels))
        #用于查询最近入库单价的数据库对象
        dbRecord = dbInOutRecord()
        dbType = dbArticleType()
        for row in range(len(remainlist)):
            item = remainlist[row]
            model.setItem(row, 0, QStandardItem(QString(str(item.article.id) )) )
            type_str = dbType.getArticleTypeInfo(item.article.typeid)
            if type_str:
                model.setItem(row, 1, QStandardItem(QString(type_str[0])) )
                model.setItem(row, 2, QStandardItem(QString(type_str[1] )) )
            model.setItem(row, 3, QStandardItem(QString(item.article.model )) )
            model.setItem(row, 4, QStandardItem(QString('%f'%item.remainCount) ) )
            lastPrice = dbRecord.getLastUnitPrice(item.article.id)
            model.setItem(row, 5, QStandardItem(QString( lastPrice and u'%f'%lastPrice or u'' ) ))
            model.setItem(row, 6, QStandardItem(QString(item.article.packaging )) )
            model.setItem(row, 7, QStandardItem(QString(item.article.pingpai )) )
            model.setItem(row, 8, QStandardItem(QString(item.article.detail )) )
        self.ui.tableView.setModel(model)
        self.ui.tableView.verticalHeader().setHidden(True)
        self.ui.tableView.setColumnWidth(0, 40)
        self.ui.tableView.setColumnWidth(5, 230)
        for i in range(model.rowCount()):
            self.ui.tableView.setRowHeight(i, 20)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = DlgStock(None)
    window.show()
    app.exec_()