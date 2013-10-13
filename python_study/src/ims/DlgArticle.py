#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from ims.DlgArticleChange import DlgArticleChange
from ui import uiDlgArticle
import sys
import ims
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.model.dbArticleType import dbArticleType
from ims.model.dbArticle import dbArticle
from ims.model.dbArticleType import ArticleType
from ims.model.dbArticle import Article
from ims.ui.uiDlgArticle import Ui_Dialog
class DlgArticle(QDialog):   
    """

    """
    '''
    @note初始化窗口,物品选择窗口时双击直接选中物品
    @param bForChoose 指定此窗口是否是物品选择窗口
    '''
    def __init__(self, parent=None,  bForChoose=False):
        super(DlgArticle,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(u'物品信息')
        self.ui.treeWidget.setMaximumWidth(150)
        self.__updateArticleTree()
        self.__updateArticleList()

        #连接信号和糟
        #用于选择时,双击选中物品,否则弹出物品信息修改窗口
        self.__bForChoose = bForChoose
        if self.__bForChoose:
            self.ui.tableView.doubleClicked.connect(self.slotChoosed)
        else:
            self.ui.tableView.doubleClicked.connect(self.slotModifyArticle)

        self.ui.pushButton_add.clicked.connect(self.slotAddArticle)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.slotDelArticle)
        self.ui.treeWidget.currentItemChanged.connect(self.slotArticleItemChanged)
        self.ui.treeWidget.itemPressed[QTreeWidgetItem, int].connect(self.slotContextMenu)
        self.ui.treeWidget.setStyleSheet( "QTreeView::item:hover{background-color:rgb(0,255,0,50)} "
                                          "QTreeView:item{border-bottom:1px solid #999999;border-right:1px solid #999999}"
                                          "QTreeView::item:selected{background-color:rgb(255,0,0,100)}");
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)

        '''如果此窗口用于选择物品'''        
        if bForChoose:
            '''初始即展开所有项目'''
            self.ui.treeWidget.expandAll()
            '''双击选中'''
            self.ui.treeWidget.doubleClicked.connect(self.slotChoosed)
            '''或者点击ok按钮进行选中'''
            self.ui.pushButton_ok.show()
            self.ui.pushButton_ok.clicked.connect(self.slotChoosed)
        else:
            self.ui.pushButton_ok.hide()

    '''选中一项物品'''
    def slotChoosed(self):
        article_id = self.__get_selected_article_id()
        if article_id is None: return
        self.__articleSelected = dbArticle().getById(article_id)
        self.accept()

    #返回选中的物品
    def getSelectedArticle(self):
        return  self.__articleSelected
        
    '''切换物品编辑状态'''
    def setEditing(self, bEditing):
        if not bEditing:
            self.ui.groupBox.hide()
        else:
            self.ui.groupBox.show()
            self.slotArticleItemChanged()
    '''右键弹出菜单'''
    def slotContextMenu(self, item, col):
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        if qApp.mouseButtons() == Qt.LeftButton: return
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]:return
        depth = res[0]                
        rightMenu = QMenu(u"right")
        action_add      = QAction(QString(u'新增'), self)
        action_rename   = QAction(QString(u'改名'), self)
        action_del      = QAction(QString(u'删除'), self)
        action_edit     = QAction(QString(u'编辑'), self)
        action_addchild = QAction(QString(u'新增子项'), self)
        '''产生菜单,物品节点和类别节点对应菜单不一样'''
        if depth != 3:
            rightMenu.addAction(action_rename)
            rightMenu.addAction(action_del)
            rightMenu.addSeparator() 
            rightMenu.addAction(action_add)
            rightMenu.addSeparator()
            rightMenu.addAction(action_addchild)
        else:
            rightMenu.addAction(action_edit)
            rightMenu.addAction(action_del)
            rightMenu.addSeparator()
            rightMenu.addAction(action_add)
        '''连接事件'''
        action_addchild.triggered.connect(self.slotAddChild)
        action_add.triggered.connect(self.slotAdd)
        action_rename.triggered.connect(self.slotRename)
        action_del.triggered.connect(self.slotDel)
        action_edit.triggered[bool].connect(self.slotEdit)
        '''显示菜单'''
        rightMenu.exec_(QCursor.pos()) 
    
    '''获取指定节点的 数据'''
    def __getItemIdDepth__(self,item):
        res = item.data(0, Qt.UserRole).toInt()
        if not res[1]: return None
        articleId = res[0]
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]: return None
        depth = res[0]
        return (articleId, depth)

    '''添加子项'''
    def slotAddChild(self):
        item = self.ui.treeWidget.currentItem()        
        if not item: return
        res = self.__getItemIdDepth__(item)
        if not res :return
        (id,depth) = res
        if depth >= 3: return
        text = QInputDialog.getText(self,
                    QString(u"新增类别名" ),
                    QString(u"请输入一个类别名称") ,
                    QLineEdit.Normal);
        if not text[1]: return
        for i in range(item.childCount()):
            if text[0]==item.child(i).text(0):
                #print text[0],item.child(i).text(0)
                QMessageBox.critical(self, u'error', u'已存在同名节点')
                return
        if depth == 1:
            newtype = ArticleType()
            newtype.parentid = id
            newtype.text = text[0]
            dbArticleType().insert(newtype)
            self.__updateArticleTree()
        else:
            article = Article()
            article.typeid = id
            article.model = text[0]
            if not dbArticle().add(article): return
            articleAdded = dbArticle().getByTypeAndModel(id, text[0])
            if not articleAdded: return
            newItem = QTreeWidgetItem()
            newItem.setText(0, articleAdded.model)
            newItem.setData(0, Qt.UserRole, articleAdded.id)
            newItem.setData(0, Qt.UserRole+1, 3)
            item.addChild(newItem)
    '''添加物品类型1/2'''
    def __AddType(self, parentid):
        text = QInputDialog.getText(self,
                    QString(u"新增类别名" ),
                    QString(u"请输入一个类别名称") ,
                    QLineEdit.Normal)
        if not text[1]: return        
        newtype = ArticleType()
        newtype.parentid = parentid
        newtype.text = text[0]
        if dbArticleType().insert(newtype):
            self.__updateArticleTree()
        else:
            QMessageBox.critical(self, u'error', u'添加失败')

    '''添加物品'''
    def __AddArticle(self, parentid, parentitem):
        text = QInputDialog.getText(self,
                   QString(u"新增物品型号" ),
                   QString(u"请输入物品型号") ,
                   QLineEdit.Normal)
        if not text[1]: return
        if text[0]=='':return
        article = Article()
        article.typeid = parentid
        article.model = text[0]
        if not dbArticle().add(article):
            QMessageBox.critical(self, u'error', u'添加物品失败')
        else:
            article = dbArticle().getByTypeAndModel(parentid, text[0])
            item = QTreeWidgetItem()
            item.setText(0, text[0])
            item.setData(0, Qt.UserRole, article.id)
            item.setData(0, Qt.UserRole+1, 3)
            parentitem.addChild(item)

    '''DELETE键删除物品节点,类别节点'''
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDelArticle()
            return
        return QDialog.keyPressEvent(self, event) 
         
    '''添加物品分类'''
    def slotAddType(self):
        #权限检查
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        if itemData == None : return       
        if itemData[1] != 2:return
        dlg = DlgArticleChange(self)
        dlg.setModal(True)
        dlg.exec_()



    '''删除物品分类'''        
    def slotDelType(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()        
        if  item.child(0) :
            QMessageBox.critical(self, u'error', u'需先删除所有子项!')
            return
        if QMessageBox.Yes != QMessageBox.warning(self, u'warning', u'确定删除此项吗', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
            return                
        res = self.__getItemIdDepth__(item)
        if not res : return
        id , depth = res
        #print 'depth = ',depth
        if depth ==1 :
            if dbArticleType().delete(id):
                self.__updateArticleTree()
        elif depth == 2:
            #print 'del type'
            if dbArticleType().delete(id):
                item.parent().removeChild(item)



    '''对物品类型节点改名'''
    def slotRename(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return

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
        
        
    '''物品列表中选择一项时'''   
    def slotArticleItemChanged(self):
        item = self.ui.treeWidget.currentItem()
        if not item : return
        #获取节点的深度,id信息
        res = self.__getItemIdDepth__(item)
        if not res:
            print 'item data is error'
            return
        '''如果未选中物品节点,则不做任何操作'''
        if res[1] != 2:
            #print 'item data-depth !=3'
            return
        self.__updateArticleList()
        
    '''类别1更新了,就更新类别2列表'''   
    def slotType1changed(self):
        #print 'type 1 changed '
        self.__initType2list()

    def slotAddArticle(self):
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        dlg = DlgArticleChange(self)
        dlg.setModal(True)
        dlg.exec_()

    def __get_selected_article_id(self):
        cur_index = self.ui.tableView.currentIndex()
        data = self.ui.tableView.model().index(cur_index.row(), 0).data()
        res = data.toInt()
        if not res[1]: return
        return  res[0]

    '''修改物料信息到数据库'''
    def slotModifyArticle(self):
        #权限检查
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
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
    
    #添加类别1    
    def slotAddType1(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"新增类别名" ),
                    QString(u"请输入一个类别名称") ,
                    QLineEdit.Normal);
        if text[0] == '': return
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        #print newtype.text
        newtype.parentid  = 0
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'error', u'添加类别1失败')        
        self.__initType1list()
        self.__updateArticleTree()
        
    '''添加类别2'''    
    def slotAddType2(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return

        '''先获取父类别id'''
        res = self.ui.comboBox_type1.itemData(self.ui.comboBox_type1.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        parentid = int(res[0])
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"新增类别名" ),
                    QString(u"请输入一个类别名称") ,
                    QLineEdit.Normal);
        if text[0] == '':return
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        newtype.parentid = parentid
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'doo', u'添加类别失败')        
        self.__initType2list()
        self.__updateArticleTree()



    '''更新treeview控件'''    
    def __updateArticleTree(self):
        strListHeader = QStringList()
        strListHeader.append(u'分类/型号')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()
        listTypes1 = dbArticleType().getType1() 
        '''插入类别1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)
            item.setData(0, Qt.UserRole,  t1.id)
            item.setData(0, Qt.UserRole+1, 1)            
            listType2 = dbArticleType().getType2(t1.id)
            self.ui.treeWidget.addTopLevelItem(item)
            '''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setData(0, Qt.UserRole+0, t2.id)#id
                item2.setData(0, Qt.UserRole+1, 2)#深度
                item.addChild(item2)

    #更新物品表格中的物品列表
    def __updateArticleList(self):
        item = self.ui.treeWidget.currentItem()
        type_id = None
        if item != None:
            res = item.data(0, Qt.UserRole).toInt()
            if None != res[1]:
                type_id = res[0]
        if type_id != None:
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
    ims.model.dbSysUser.g_current_user = user
    appp = QApplication(sys.argv)
    window = DlgArticle(None)
    window.setModal(True)
    window.show()
    appp.exec_()