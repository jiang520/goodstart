#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from ims.DlgArticleChange import DlgArticleChange
from ui.uiDlgArticle import Ui_Dialog
import sys
import ims
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.model.dbArticleType import dbArticleType
from ims.model.dbArticle import dbArticle
from ims.model.dbArticleType import ArticleType
class DlgArticle(QDialog):
    """

    """
    def __init__(self, parent=None,  bForChoose=False):
        '''
        @note初始化窗口,物品选择窗口时双击直接选中物品
        @param bForChoose 指定此窗口是否是物品选择窗口
        '''
        super(DlgArticle,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(u'物品信息')
        self.ui.treeWidget.setMaximumWidth(150)

        #连接信号和糟
        #用于选择时,双击选中物品,否则弹出物品信息修改窗口
        self.__bForChoose = bForChoose
        if self.__bForChoose:
            self.ui.tableView.doubleClicked.connect(self.slotChoosed)
        else:
            self.ui.tableView.doubleClicked.connect(self.slotModifyArticle)

        self.ui.pushButton_add.clicked.connect(self.slotAddArticle)
        self.ui.pushButton_export.clicked.connect(self.slotExport)
        self.ui.pushButton_2.clicked.connect(self.slotDelArticle)
        self.ui.treeWidget.setSortingEnabled(False)
        self.ui.treeWidget.currentItemChanged.connect(self.slotArticleItemChanged)
        self.ui.treeWidget.itemPressed[QTreeWidgetItem, int].connect(self.slotContextMenu)
        self.ui.treeWidget.setStyleSheet( "QTreeView::item:hover{background-color:rgb(0,255,0,50)} "
                                          "QTreeView:item{border-bottom:1px solid #999999;border-right:1px solid #999999}"
                                          "QTreeView::item:selected{background-color:rgb(255,0,0,100)}")

        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.slotTableMenu)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.__updateArticleTree()
        self.__updateArticleList()

        #'''如果此窗口用于选择物品'''
        if bForChoose:
            #'''初始即展开所有项目'''
            self.ui.treeWidget.expandAll()
            #'''双击选中'''
            self.ui.treeWidget.doubleClicked.connect(self.slotChoosed)
            #'''或者点击ok按钮进行选中'''
            self.ui.pushButton_ok.show()
            self.ui.pushButton_ok.clicked.connect(self.slotChoosed)
        else:
            self.ui.pushButton_ok.hide()

    #物品表格菜单,提供导出,修改,删除功能
    def slotTableMenu(self):
        model = self.ui.tableView.model()
        if model.rowCount() <= 0: return
        action_export = QAction(u'导出', self)
        action_del = QAction(u'删除', self)
        action_modify = QAction(u'修改', self)
        action_del.triggered.connect(self.slotDelArticle)
        action_modify.triggered.connect(self.slotModifyArticle)
        action_export.triggered.connect(self.slotExport)
        gUser = ims.model.dbSysUser.g_current_user
        #非管理员用户
        if None==gUser or not gUser.is_enable_write_all():
            action_modify.setEnabled(False)
            action_del.setEnabled(False)
        menu = QMenu()
        menu.addAction(action_modify)
        menu.addAction(action_del)
        menu.addSeparator()
        menu.addAction(action_export)
        menu.exec_(QCursor().pos())

    #'''选中一项物品'''
    def slotChoosed(self):
        article_id = self.__get_selected_article_id()
        if article_id is None: return
        self.__articleSelected = dbArticle().getById(article_id)
        self.accept()

    #返回选中的物品
    def getSelectedArticle(self):
        return  self.__articleSelected
        

    #'''右键弹出菜单'''
    def slotContextMenu(self, item, col):
        if qApp.mouseButtons() == Qt.LeftButton: return
        rightMenu = QMenu(u"right")
        action_addType      = QAction(QString(u'新增'), self)
        action_renameType   = QAction(QString(u'改名'), self)
        action_delType      = QAction(QString(u'删除'), self)
        action_addChild     = QAction(QString(u'新增子类'), self)
        action_addArticle   = QAction(QString(u'新增物品'), self)
        action_refresh      = QAction(QString(u'刷新'), self)
         #'''连接事件'''
        action_addType.triggered.connect(self.slotAddType)
        action_renameType.triggered.connect(self.slotRenameType)
        action_delType.triggered.connect(self.slotDelType)
        action_addChild.triggered.connect(self.slotAddChildType)
        action_addArticle.triggered.connect(self.slotAddArticle)
        action_refresh.triggered.connect(self.__updateArticleTree)

        user = ims.model.dbSysUser.g_current_user
        if user==None or not user.is_enable_write_all():
            action_delType.setEnabled(False)
            action_addType.setEnabled(False)
            action_addArticle.setEnabled(False)
            action_renameType.setEnabled(False)
            action_addChild.setEnabled(False)
        #获取当前选中节点内容
        item = self.ui.treeWidget.currentItem()
        item_data = self.__getItemIdDepth__(item)
        if not item_data: return
        #显示所有--节点的弹出菜单
        if item_data[0]==-1:
            rightMenu.addAction(action_addType)
        else:
            #显示大类型的弹出菜单
            rightMenu.addAction(action_addType)
            rightMenu.addAction(action_renameType)
            rightMenu.addAction(action_delType)
            if item_data[1]==1:
                rightMenu.addAction(action_addChild)
            else:
                rightMenu.addAction(action_addArticle)
        rightMenu.addSeparator()
        rightMenu.addAction(action_refresh)
        #'''显示菜单'''
        rightMenu.exec_(QCursor().pos())
    
    #'''获取指定节点的 数据'''
    def __getItemIdDepth__(self,item):
        res = item.data(0, Qt.UserRole).toInt()
        if not res[1]: return None
        articleId = res[0]
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]: return None
        depth = res[0]
        return (articleId, depth)


    #'''DELETE键删除物品节点,类别节点'''
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            #tree控制有焦点时,删除类别,否则删除物品项
            if self.focusWidget() == self.ui.tableView:
                self.slotDelArticle()
                return
            elif self.focusWidget() == self.ui.treeWidget:
                self.slotDelType()
                return
        return QDialog.keyPressEvent(self, event) 
         
    #'''添加物品分类'''
    def slotAddType(self):
        #权限检查
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        if itemData == None : return
        if itemData[1] == 1:
            #如果深度为1,则父类别id为0
            parentid = 0
        else:
            #否则求父节点的类别id
            item_parent = item.parent()
            data_parent = self.__getItemIdDepth__(item_parent)
            if itemData == None: return
            parentid = data_parent[0]
        #获取类别名称
        text = QInputDialog.getText(self, u'新增类别',u'请输入一个新的类别名称')
        if not text[1]: return
        if text[0]=="": return
        newtype = ArticleType()
        newtype.text = u'%s'%text[0]
        newtype.parentid = parentid
        #执行数据库操作
        if not dbArticleType().insert(newtype):
            QMessageBox.critical(self, u'出错了',u'添加类别失败,请重试')
        else:
            self.__updateArticleTree()

    #为一级节点添加子类型
    def slotAddChildType(self):
        #权限检查
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        parentid = itemData[0]
        if parentid <=0: return
        #获取类别名称
        text = QInputDialog.getText(self, u'新增类别',u'请输入一个新的类别名称')
        if not text[1]: return
        if text[0]=="": return
        newtype = ArticleType()
        newtype.text = u'%s'%text[0]
        newtype.parentid = parentid
        #执行数据库操作
        if not dbArticleType().insert(newtype):
            QMessageBox.critical(self, u'出错了',u'添加类别失败,请重试')
        else:
            self.__updateArticleTree()



    #'''删除物品分类'''
    def slotDelType(self):
        user = ims.model.dbSysUser.g_current_user
        if user==None or not user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item is None: return
        #需先删除所有子类别
        itemdata  = self.__getItemIdDepth__(item)
        if itemdata is None: return
        type_id = itemdata[0]
        depth = itemdata[1]
        print depth
        if depth != 2 and depth != 1: return
        if depth == 2:
            #检查2级类别下对应的是否有相关的物品信息
            article_list = dbArticle().getArticlesByTypeId(type_id)
            if article_list != None and len(article_list) > 0:
                QMessageBox.critical(self, u'error', u'需先删除该类别下所有物品!')
                return
        else:
            #1级类别检查下面是否有子类别
            if item.childCount() > 0:
                QMessageBox.critical(self, u'error', u'需先删除所有子类别')
                return
        #删除警告
        if QMessageBox.Yes != QMessageBox.warning(self, u'warning', u'确定删除此项吗', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
            return
        #删除类别
        if dbArticleType().delete(type_id):
            self.__updateArticleTree()
        else:
            QMessageBox.critical(self, u'出错了', u'删除出错,请重试')


    #'''对物品类型节点改名'''
    def slotRenameType(self):
        user = ims.model.dbSysUser.g_current_user
        if None==user or not user.is_enable_write_all():return

        item = self.ui.treeWidget.currentItem()
        if not item : return
        res = self.__getItemIdDepth__(item)
        if not res : return
        id , depth = res
        if depth == 3: return
        text = QInputDialog.getText(self,
                    QString(u"新增类别名" ),
                    QString(u"请输入一个类别名称") ,
                    QLineEdit.Normal,
                    QString(item.text(0)));
        if not text[1]: return
        if not dbArticleType().rename(id, text[0]):
            QMessageBox.critical(self, u'error', u'重命名失败')
            return
        item.setText(0, text[0])
    #导出物品列表
    def slotExport(self):
        import  FunctionTools
        FunctionTools.ExportTableToExcel(self.ui.tableView)
        
        
    #'''物品列表中选择一项时'''
    def slotArticleItemChanged(self):
        item = self.ui.treeWidget.currentItem()
        if not item : return
        #获取节点的深度,id信息
        res = self.__getItemIdDepth__(item)
        if not res:
            print 'item data is error'
            return
        #'''如果未选中物品节点,则不做任何操作'''
        if res[1] != 2 and res[0]!=-1:
            #print 'item data-depth !=3'
            return
        self.__updateArticleList()

    #添加物品信息
    def slotAddArticle(self):
        user = ims.model.dbSysUser.g_current_user
        if None==user or not user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        dlg = DlgArticleChange(self)
        if item != None and item.parent() != None:
            strType2 = item.text(0)
            strType1 = item.parent().text(0)
        dlg.setModal(True)
        dlg.exec_()

    #返回当前选择的物品id,用于删除,修改物品信息
    def __get_selected_article_id(self):
        cur_index = self.ui.tableView.currentIndex()
        data = self.ui.tableView.model().index(cur_index.row(), 0).data()
        res = data.toInt()
        if not res[1]: return
        return  res[0]

    #'''修改物料信息到数据库'''
    def slotModifyArticle(self):
        #权限检查
        user = ims.model.dbSysUser.g_current_user
        if None==user or not user.is_enable_write_all():return
        article_id = self.__get_selected_article_id()
        if article_id is None: return
        article = dbArticle().getById(article_id)
        dlg = DlgArticleChange(self, article)
        dlg.setModal(True)
        dlg.exec_()
        self.__updateArticleList()

    #删除物品信息
    def slotDelArticle(self):
        article_id = self.__get_selected_article_id()
        res = QMessageBox.warning(self, u'危险操作', u'确认从数据库中删除当前选中的物品信息?', QMessageBox.Yes|QMessageBox.No)
        if res != QMessageBox.Yes: return
        if dbArticle().delete(article_id):
            self.__updateArticleList()
        else:
            QMessageBox.critical(self, u'出错了', u'删除操作执行出错')
    

    #'''更新treeview控件'''
    def __updateArticleTree(self):
        strListHeader = QStringList()
        strListHeader.append(u'分类/型号')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()

        listTypes1 = dbArticleType().getType1()
        #'''插入类别1'''
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)
            item.setData(0, Qt.UserRole,  t1.id)
            item.setData(0, Qt.UserRole+1, 1)
            listType2 = dbArticleType().getType2(t1.id)
            self.ui.treeWidget.addTopLevelItem(item)
            #'''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setData(0, Qt.UserRole+0, t2.id)#id
                item2.setData(0, Qt.UserRole+1, 2)#深度
                item.addChild(item2)
        #插入一个显示所有的项
        item = QTreeWidgetItem()
        item.setText(0, u'--[显示所有]--')
        item.setData(0, Qt.UserRole, -1)
        item.setData(0, Qt.UserRole+1, 1)
        self.ui.treeWidget.insertTopLevelItem(0, item)

    #更新物品表格中的物品列表
    def __updateArticleList(self):
        item = self.ui.treeWidget.currentItem()
        type_id = None
        if item != None:
            res = item.data(0, Qt.UserRole).toInt()
            if None != res[1]:
                type_id = res[0]
        if type_id != None:
            if type_id == -1:#id 为-1的项用来<显示所有物品列表>
                article_list = dbArticle().getAll()
            else:
                article_list = dbArticle().getArticlesByTypeId(type_id)
        else:
            article_list = []
        labels = [u'ID',u'型号/品名',u'单位',u'封装',u'功能',u'品牌',u'说明']
        model = QStandardItemModel(len(article_list), len(labels), self)
        model.setHorizontalHeaderLabels(QStringList(labels))
        #更新物品列表
        for i in range( len(article_list) ):
            article = article_list[i]
            model.setItem(i, 0, QStandardItem(QString(unicode(article.id))))
            model.setItem(i, 1, QStandardItem(QString(unicode(article.model))))
            model.setItem(i, 2, QStandardItem(QString(unicode(article.unit))))
            model.setItem(i, 3, QStandardItem(QString(unicode(article.packaging))))
            model.setItem(i, 4, QStandardItem(QString(unicode(article.function))))
            model.setItem(i, 4, QStandardItem(QString(unicode(article.pingpai))))
            model.setItem(i, 4, QStandardItem(QString(unicode(article.detail))))
        self.ui.tableView.setModel(model)
        for i in range( len(article_list)): self.ui.tableView.setRowHeight(i, 20)
        self.ui.tableView.setColumnWidth(0, 20)
        self.ui.tableView.setColumnWidth(2, 40)

if __name__ == '__main__':
    import ims
    #ims.ui.ui2py.pyqt_ui_2_py()
    user = ims.model.dbSysUser.SysUser()
    user.usertype = u"管理员"
    from ims.model.dbSysUser import g_current_user
    g_current_user = user
    appp = QApplication(sys.argv)
    window = DlgArticle(None)
    window.setModal(True)
    window.show()
    appp.exec_()