#encoding=gb2312
'''
Created on 2013-6-6

@author: jiang
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from json.decoder import errmsg
import urllib2
from locale import str
from ims.DlgClient import DlgClient
from ims.DlgArticle import DlgArticle
from ims.model.dbInoutRecord import *
from ims.model.dbArticleType import *
from ims.model.dbArticle import *

class DlgIMSMain(QMainWindow): 
    
    def __init__(self):
        super(DlgIMSMain, self).__init__(None)
        tabWidget = QTabWidget(self)
        self.tableViewRemain = QTableView()
        layout = QVBoxLayout()
        layout.addWidget(self.tableViewRemain)
        groupbox = QGroupBox(u'当前物料库存')
        groupbox.setLayout(layout)       
        tabWidget.addTab(groupbox, u'库存列表') 
        
        '''进出货记录'''
        self.tableInoutRecord = QTableView(self)
        layout = QVBoxLayout()               
        layout.addWidget(self.tableInoutRecord)
        
        groupbox = QGroupBox(u'最近进出货记录')
        groupbox.setLayout(layout)
        tabWidget.addTab(groupbox, u'进出货记录')    
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
        self.setMinimumSize(800, 600)
        self.__initRecordTable()
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
        
        self.tableViewRemain.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableViewRemain.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableViewRemain.setSelectionMode(QTableWidget.SingleSelection)
        self.tableViewRemain.setAlternatingRowColors(True)
        
        self.tableInoutRecord.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableInoutRecord.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableInoutRecord.setSelectionMode(QTableWidget.SingleSelection)
        self.tableInoutRecord.setAlternatingRowColors(True)
        
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
            listType2 = dbArticleType().getType2(t1.id)
            '''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''插入物品型号'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, str(ac.id))
                    item2.addChild(item3)
            self.treeArticle.addTopLevelItem(item)
    '''
        更新进出货记录列表
    '''    
    def __initRecordTable(self):
        recordlist = dbInOutRecord().getRecord(0, 50)                
        model = QStandardItemModel(len(recordlist), 6)
        i = 0
        for item in recordlist:
            print item
            model.setItem(i, 0, QStandardItem(QString(str(item.id))))
            print item.time
            model.setItem(i, 1, QStandardItem(QString('%s'%item.time)))
            model.setItem(i, 2, QStandardItem(QString( item.count < 0  and u'出库' or u'入库')))
            model.setItem(i, 3, QStandardItem(QString(str(item.count))))            
            model.setItem(i, 4, QStandardItem(QString(str(item.price))))
            print 'detail=', item.detail
            #model.setItem(i, 5, QStandardItem(QString(str(item.detail))))
            self.tableInoutRecord.setRowHeight(i,10)  
            i = i+1                 
        self.tableInoutRecord.setModel(model)
        for i in range(model.rowCount(parent=QModelIndex())):
            self.tableInoutRecord.setRowHeight(i, 20)
        
    '''初始化菜单'''          
    def __initMenu(self):
        menubar = self.menuBar()
        #menufile = menubar.addMenu("filde")
        menufile = QMenu(u"文件",self)
        self.action_setting = QAction(u'设置',self)
        menufile.addAction(self.action_setting)
        #menufile.addAction(s)
    
        self.action_in      = QAction(u"进货", self)
        self.action_out     = QAction(u"出货", self)
        self.action_record  = QAction(u'进出货记录查询',self)
        self.action_client  = QAction(u"客户管理", self)        
        self.action_article = QAction(u"物品管理", self)
        self.action_exit    = QAction(u'退出系统', self)
        self.action_backup  = QAction(u'备份数据库',self)
        
        menufile.addAction(self.action_in)
        menufile.addAction(self.action_out)
        menufile.addSeparator()
        menufile.addAction(self.action_record)
        menufile.addSeparator()
        menufile.addAction(self.action_article)
        menufile.addAction(self.action_client)
        
        menufile.addSeparator()
        menufile.addAction(self.action_exit)   
                
        menubar.addMenu(menufile)                
        toolbar = QToolBar(self)      
        toolbar.setFixedHeight(33)
        toolbar.addAction(self.action_in)
        toolbar.addAction(self.action_out)
        
        toolbar.addSeparator()
        toolbar.addAction(self.action_record)
        toolbar.addSeparator()
        toolbar.addAction(self.action_client)
        toolbar.addSeparator()
        toolbar.addAction(self.action_article)
        toolbar.addSeparator()
        toolbar.addAction(self.action_backup)     
        toolbar.addSeparator()
        toolbar.addAction(self.action_exit)
        
        
        self.action_client.triggered.connect(self.slotDlgClient)     
        self.action_exit.triggered.connect(self.slotExitSystem)     
        self.action_in.triggered.connect(self.slotInOut)           
        self.action_out.triggered.connect(self.slotInOut)
        self.action_article.triggered.connect(self.slotArticle)
        self.addToolBar(toolbar)        
        menubar.addMenu("edit")
        menubar.addMenu("help")
    '''
        更新物品库存列表
    '''
    def __updateArticleCountList(self):
        item = self.treeArticle.currentItem()
        if item==None or item.text(1)=="-1" :
            remainlist = dbArticle().getAllArticleRemainList()
        elif item.text(1)=='':
            return
        else:
            article_id = int( item.text(1))
            #print article_id
            remainlist = dbArticle().getSpecArticleRemainList(article_id)
        #print remainlist
        model = QStandardItemModel(len(remainlist),5)
        labels = QStringList()
        labels.append(u'id')
        labels.append(u'物品型号')
        labels.append(u'库存')
        labels.append(u'封装')
        labels.append(u'品牌')        
        labels.append(u'详细说明')
        model.setHorizontalHeaderLabels(labels)
        row = 0
        for item in remainlist:
            #print item
            model.setItem(row, 0, QStandardItem(QString(str(item[0]) )) )            
            model.setItem(row, 1, QStandardItem(QString(item[1] )) )         
            str2 = (not item[2]) and str(0) or "%d"%item[2]
            #print str2 
            model.setItem(row, 2, QStandardItem(QString(str2) ) )
            model.setItem(row, 3, QStandardItem(QString(item[3] )) )
            model.setItem(row, 4, QStandardItem(QString(item[4] )) )
            model.setItem(row, 5, QStandardItem(QString(item[5] )) )
            row = row+1    
        self.tableViewRemain.setModel(model)
        for i in range(model.rowCount()):
            self.tableViewRemain.setRowHeight(i, 20)
        
    def slotExitSystem(self):
        print 'slot exit system'
        self.close()
        
    def slotDlgClient(self):
        print 'slot dlg client'
        
        dlg = DlgClient()
        dlg.setModal(True)
        dlg.exec_()
        
    '''查找一个上下的图片文件,把文件名放到listwidget中,'''
    def slotInOut(self):
        import DlgInOutArticle
        dlg = DlgInOutArticle.DlgInOutArticle()
        dlg.setModal(True)
        dlg.exec_()
     
                
    def slotArticle(self):
        import DlgArticle
        dlg = DlgArticle.DlgArticle()
        dlg.setModal(True)
        dlg.exec_()
    '''
    select the next image
    '''   
    def slotnext(self):
        row = self.listwidget.currentRow()
        if row + 1 >= self.listwidget.count():
            return
        self.listwidget.setCurrentRow(row+1)
        
    def slotpre(self):
        row = self.listwidget.currentRow()
        if row -1 < 0:
            return
        self.listwidget.setCurrentRow(row-1)
'''主函数
'''        
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgIMSMain()
    window.show()
    appp.exec_()
