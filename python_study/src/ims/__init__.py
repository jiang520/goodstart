#encoding=gb2312
'''
Created on 2013-6-6
@author: jiang
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.DlgClient import *
from ims.DlgArticle import DlgArticle
from ims.DlgRecordSearch import DlgRecordSearch
from ims.DlgInOutArticle import *
from ims.model.dbInoutRecord import *
from ims.model.dbArticleType import *
from ims.model.dbArticle import *


class DlgIMSMain(QMainWindow): 
    
    def __init__(self):
        super(DlgIMSMain, self).__init__(None)
        tabWidget = QTabWidget(self)
        
        self.tableViewRemain = QTableView()
        tabWidget.addTab(self.tableViewRemain, u'库存列表')
        
        '''进出货记录'''
        self.dlgRecordSearch = DlgRecordSearch()
        tabWidget.addTab(self.dlgRecordSearch, u'进出货记录')  
        tabWidget.addTab(DlgClient(self), u'客户列表')
          
        '''物品列表'''        
        spliterH = QSplitter(Qt.Horizontal, self)       
        self.treeArticle = QTreeWidget(self)       
        spliterH.addWidget(self.treeArticle)       
       
        spliterH.addWidget(tabWidget)
        spliterH.setLineWidth(0)
        spliterH.setLineWidth(1)
        spliterH.setStretchFactor(0, 30)
        spliterH.setStretchFactor(1, 100)
        self.setCentralWidget(spliterH)
        
        self.__initMenu()
        self.__initToolbar()
        self.setMinimumSize(800, 600)
        self.__initTreeCtrl_Article()
        self.__updateArticleCountList()
        self.__udpateArticleTreeView()     
        self.treeArticle.itemSelectionChanged.connect(self.__updateArticleCountList)
        
        
    '''更新物品分类树'''
    def __initTreeCtrl_Article(self):               
        strListHeader = QStringList()
        strListHeader.append(u'物料分类')
        #strListHeader.append(u'封装')
        #strListHeader.append(u'备注')
        self.treeArticle.setHeaderLabels(strListHeader)
        self.treeArticle.setStyleSheet( "QTreeView::item:hover{background-color:rgb(0,255,0,50)} "
                                          "QTreeView:item{border-bottom:1px solid #999999;border-right:1px solid #999999}"
                                          "QTreeView::item:selected{background-color:rgb(255,0,0,100)}");

        
        self.tableViewRemain.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableViewRemain.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableViewRemain.setSelectionMode(QTableWidget.SingleSelection)
        self.tableViewRemain.setAlternatingRowColors(True)

        
       
        
    def __udpateArticleTreeView(self):
        self.treeArticle.clear()
        '''添加一个显示所有库存的项'''
        item = QTreeWidgetItem()
        item.setText(0,u'显示所有')
        item.setText(1,u'-1')
        self.treeArticle.addTopLevelItem(item)
                 
        listTypes1 = dbArticleType().getType1() 
        '''插入类别1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)                
            item.setBackgroundColor(0, Qt.green)       
            listType2 = dbArticleType().getType2(t1.id)
            '''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)                
                item2.setBackgroundColor(0, Qt.green)
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''插入物品型号'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, str(ac.id))
                    item2.addChild(item3)
                    
            self.treeArticle.addTopLevelItem(item)
           
    '''初始化菜单'''          
    def __initMenu(self):
        self.action_in      = QAction(QIcon("images/shopping.png"),u"进货", self)
        self.action_out     = QAction(QIcon("images/sale.png"), u"出货", self)
        self.action_article = QAction(QIcon("images/shipping.png"), u"物料整理", self)
        self.action_client  = QAction(QIcon("images/26.png"),u"客户通讯录", self)
        self.action_backup  = QAction(QIcon("images/timezone.png"), u'备份数据库',self)
        self.action_chart   = QAction(QIcon("images/chart.png"), u"统计曲线", self)
        self.action_exit    = QAction(QIcon("images/Restricted 1.png"),u'退出系统', self)
        self.action_export_remain = QAction(u'导出库存列表',self)
        self.action_export_articl = QAction(u'导出物品列表',self)
        self.action_export_record = QAction(u'导出出库库记录列表', self)
        self.action_about         = QAction(u'关于', self)

        self.action_client.triggered.connect(self.slotDlgClient)
        self.action_exit.triggered.connect(self.close)
        self.action_in.triggered.connect(self.slotIn)
        self.action_out.triggered.connect(self.slotOut)
        self.action_article.triggered.connect(self.slotArticle)
        self.action_about.triggered.connect(self.slotAbout)
        self.action_backup.triggered.connect(self.slotBackup)

        self.action_export_remain.triggered.connect(self.slotExportRemain)
        self.action_export_record.triggered.connect(self.slotExportRecord)

        menubar = self.menuBar()
        menufile = QMenu(u"文件",self)
        menufile.addAction(self.action_article)
        menufile.addAction(self.action_client)
        menufile.addSeparator()
        menufile.addAction(self.action_exit)

        menuTools = QMenu(u'数据转换工具', self)
        menuTools.addAction(self.action_export_remain)
        menuTools.addAction(self.action_export_articl)
        menuTools.addAction(self.action_export_record)
        menuTools.addSeparator()
        menuTools.addAction(self.action_backup)
        menubar.addMenu(menufile)
        menubar.addMenu(menuTools)
        menubar.addAction(self.action_about)

    def __initToolbar(self):
        toolbar = QToolBar(self)
        #toolbar.setFixedHeight(70)
        toolbar.setIconSize(QSize(50,50))
        toolbar.addAction(self.action_in)
        toolbar.addAction(self.action_out)
        
        toolbar.addSeparator()
        toolbar.addAction(self.action_article)
        toolbar.addSeparator()
        toolbar.addAction(self.action_client)
        toolbar.addSeparator()
        toolbar.addAction(self.action_chart)
        toolbar.addSeparator()
        toolbar.addAction(self.action_exit)
        self.addToolBar(toolbar)

    '''导出指定的tablewiget的数据到文件中'''
    @staticmethod
    def __ExportTableWidgetData(tableWidget, filepath):
        if filepath == None or len(filepath) <= 0: return
        if tableWidget == None : return
        model = tableWidget.model()
        rowCount = model.rowCount()
        colCount = model.columnCount()
        import codecs
        fileExport = codecs.open(filepath, 'w', 'utf-8')
        for col in range(colCount):
            str = model.headerData(col, Qt.Horizontal)
            str = u'%s,'%str.toString()
            fileExport.write(str)
            fileExport.write(',')
        fileExport.write('\r\n')
        for row in range(rowCount):
            for col in range(colCount):
                index = model.index(row, col)
                data = model.data(index, Qt.DisplayRole)
                #print data.toString()
                fileExport.write(u'%s,'%data.toString())
            fileExport.write('\r\n')
        fileExport.close()

    #导出库存列表
    def slotExportRemain(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        self.__ExportTableWidgetData(self.tableViewRemain, filePath)
        QMessageBox.information(self, u'info', u'已导出到%s'%filePath)

    #导出出入库记录
    def slotExportRecord(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        self.__ExportTableWidgetData(self.dlgRecordSearch.ui.tableView, filePath)
        QMessageBox.information(self, u'info', u'已导出到%s'%filePath)

    def slotAbout(self):
        QMessageBox.about(self,u'库存管理系统',
                          u'''UT库存管理系统,基于python2.7和pyqt4.8构建,\n版权所有,欢迎使用''')


    def __getArticleCountListLabels(self):
        labels = QStringList()
        labels.append(u'id')
        labels.append(u'物品型号')
        labels.append(u'库存')
        labels.append(u'封装')
        labels.append(u'品牌')
        labels.append(u'详细说明')
        return labels

    '''备份数据库,将数据库文件复制到其他位置'''
    def slotBackup(self):
        dstPath = QFileDialog.getExistingDirectory(self)
        if dstPath == "" : return
        date = QDate.currentDate()
        dstPath = dstPath +('\\ims_database_%04d%02d%02d.db3'%(date.year(), date.month(), date.day()))
        import  shutil
        srcPath = dbActicleIMS.getInstance().getDatabaseFilePath()
        print 'copy [%s] to [%s]'%(srcPath, dstPath)
        try:
            shutil.copyfile(srcPath,dstPath)
            QMessageBox.information(self, 'Successed!', u'数据库已成功备份到\n%s'%dstPath)
        except Exception,e:
            print e
            QMessageBox.critical(self, 'Successed!', u'数据库备份失败%s'%e)


    '''
    更新物品库存列表
    '''
    def __updateArticleCountList(self):
        item = self.treeArticle.currentItem()
        '''查找所有物品的库存'''
        if item==None or item.text(1)=="-1" :
            remainlist = dbArticle().getAllArticleRemainList()
            self.dlgRecordSearch.setArticleIdFilter(None)
        elif item.text(1)=='':
            return
        else:
            article_id = int( item.text(1))
            remainlist = dbArticle().getSpecArticleRemainList(article_id)
            self.dlgRecordSearch.setArticleIdFilter(article_id)
        #print remainlist
        model = QStandardItemModel(len(remainlist),5)
        model.setHorizontalHeaderLabels(self.__getArticleCountListLabels())
        row = 0
        for item in remainlist:
            model.setItem(row, 0, QStandardItem(QString(str(item.article.id) )) )            
            model.setItem(row, 1, QStandardItem(QString(item.article.model )) )         
            model.setItem(row, 2, QStandardItem(QString('%f'%item.remainCount) ) )
            model.setItem(row, 3, QStandardItem(QString(item.article.packaging )) )
            model.setItem(row, 4, QStandardItem(QString(item.article.pingpai )) )
            model.setItem(row, 5, QStandardItem(QString(item.article.detail )) )
            row = row+1    
        self.tableViewRemain.setModel(model)
        self.tableViewRemain.verticalHeader().setHidden(True)
        self.tableViewRemain.setColumnWidth(0, 40)
        self.tableViewRemain.setColumnWidth(5, 230)
        for i in range(model.rowCount()):
            self.tableViewRemain.setRowHeight(i, 20)
        

    '''客户信息管理'''
    def slotDlgClient(self):
        #print 'slot dlg client'
        
        dlg = DlgClient(self)
        dlg.setModal(True)
        dlg.exec_()
    #进货
    def slotIn(self):
        dlg = DlgInOutArticle(self, True)
        dlg.setModal(True)
        dlg.exec_()

    '''出货'''
    def slotOut(self):
        dlg = DlgInOutArticle(self, False)
        dlg.setModal(True)
        dlg.exec_()

    #物品管理
    def slotArticle(self):
        dlg = DlgArticle(self)
        dlg.setModal(True)
        dlg.exec_()
        self.__udpateArticleTreeView()

 #主函数
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT库存管理系统')
    appp.setWindowIcon(QIcon("images/14.png"))
    window = DlgIMSMain()
    window.setWindowTitle(u'UT库存管理系统')
    window.show()
    appp.exec_()
