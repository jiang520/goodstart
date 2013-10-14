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
    @note��ʼ������,��Ʒѡ�񴰿�ʱ˫��ֱ��ѡ����Ʒ
    @param bForChoose ָ���˴����Ƿ�����Ʒѡ�񴰿�
    '''
    def __init__(self, parent=None,  bForChoose=False):
        super(DlgArticle,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(u'��Ʒ��Ϣ')
        self.ui.treeWidget.setMaximumWidth(150)
        self.__updateArticleTree()
        self.__updateArticleList()

        #�����źź���
        #����ѡ��ʱ,˫��ѡ����Ʒ,���򵯳���Ʒ��Ϣ�޸Ĵ���
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

        '''����˴�������ѡ����Ʒ'''        
        if bForChoose:
            '''��ʼ��չ��������Ŀ'''
            self.ui.treeWidget.expandAll()
            '''˫��ѡ��'''
            self.ui.treeWidget.doubleClicked.connect(self.slotChoosed)
            '''���ߵ��ok��ť����ѡ��'''
            self.ui.pushButton_ok.show()
            self.ui.pushButton_ok.clicked.connect(self.slotChoosed)
        else:
            self.ui.pushButton_ok.hide()

    '''ѡ��һ����Ʒ'''
    def slotChoosed(self):
        article_id = self.__get_selected_article_id()
        if article_id is None: return
        self.__articleSelected = dbArticle().getById(article_id)
        self.accept()

    #����ѡ�е���Ʒ
    def getSelectedArticle(self):
        return  self.__articleSelected
        
    '''�л���Ʒ�༭״̬'''
    def setEditing(self, bEditing):
        if not bEditing:
            self.ui.groupBox.hide()
        else:
            self.ui.groupBox.show()
            self.slotArticleItemChanged()
    '''�Ҽ������˵�'''
    def slotContextMenu(self, item, col):
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        if qApp.mouseButtons() == Qt.LeftButton: return
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]:return
        depth = res[0]                
        rightMenu = QMenu(u"right")
        action_add      = QAction(QString(u'����'), self)
        action_rename   = QAction(QString(u'����'), self)
        action_del      = QAction(QString(u'ɾ��'), self)
        action_edit     = QAction(QString(u'�༭'), self)
        action_addchild = QAction(QString(u'��������'), self)
        '''�����˵�,��Ʒ�ڵ�����ڵ��Ӧ�˵���һ��'''
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
        '''�����¼�'''
        action_addchild.triggered.connect(self.slotAddChild)
        action_add.triggered.connect(self.slotAdd)
        action_rename.triggered.connect(self.slotRename)
        action_del.triggered.connect(self.slotDel)
        action_edit.triggered[bool].connect(self.slotEdit)
        '''��ʾ�˵�'''
        rightMenu.exec_(QCursor.pos()) 
    
    '''��ȡָ���ڵ�� ����'''
    def __getItemIdDepth__(self,item):
        res = item.data(0, Qt.UserRole).toInt()
        if not res[1]: return None
        articleId = res[0]
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]: return None
        depth = res[0]
        return (articleId, depth)

    '''�������'''
    def slotAddChild(self):
        item = self.ui.treeWidget.currentItem()        
        if not item: return
        res = self.__getItemIdDepth__(item)
        if not res :return
        (id,depth) = res
        if depth >= 3: return
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal);
        if not text[1]: return
        for i in range(item.childCount()):
            if text[0]==item.child(i).text(0):
                #print text[0],item.child(i).text(0)
                QMessageBox.critical(self, u'error', u'�Ѵ���ͬ���ڵ�')
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
    '''�����Ʒ����1/2'''
    def __AddType(self, parentid):
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal)
        if not text[1]: return        
        newtype = ArticleType()
        newtype.parentid = parentid
        newtype.text = text[0]
        if dbArticleType().insert(newtype):
            self.__updateArticleTree()
        else:
            QMessageBox.critical(self, u'error', u'���ʧ��')

    '''�����Ʒ'''
    def __AddArticle(self, parentid, parentitem):
        text = QInputDialog.getText(self,
                   QString(u"������Ʒ�ͺ�" ),
                   QString(u"��������Ʒ�ͺ�") ,
                   QLineEdit.Normal)
        if not text[1]: return
        if text[0]=='':return
        article = Article()
        article.typeid = parentid
        article.model = text[0]
        if not dbArticle().add(article):
            QMessageBox.critical(self, u'error', u'�����Ʒʧ��')
        else:
            article = dbArticle().getByTypeAndModel(parentid, text[0])
            item = QTreeWidgetItem()
            item.setText(0, text[0])
            item.setData(0, Qt.UserRole, article.id)
            item.setData(0, Qt.UserRole+1, 3)
            parentitem.addChild(item)

    '''DELETE��ɾ����Ʒ�ڵ�,���ڵ�'''
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDelArticle()
            return
        return QDialog.keyPressEvent(self, event) 
         
    '''�����Ʒ����'''
    def slotAddType(self):
        #Ȩ�޼��
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        if itemData == None : return       
        if itemData[1] != 2:return
        dlg = DlgArticleChange(self)
        dlg.setModal(True)
        dlg.exec_()



    '''ɾ����Ʒ����'''        
    def slotDelType(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()        
        if  item.child(0) :
            QMessageBox.critical(self, u'error', u'����ɾ����������!')
            return
        if QMessageBox.Yes != QMessageBox.warning(self, u'warning', u'ȷ��ɾ��������', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
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



    '''����Ʒ���ͽڵ����'''
    def slotRename(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return

        item = self.ui.treeWidget.currentItem()
        if not item : return
        res = self.__getItemIdDepth__(item)
        if not res : return
        id , depth = res
        if depth == 3: return
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal,
                    QString(item.text(0)));
        if not text[1]: return
        if not dbArticleType().rename(id, text[0]):
            QMessageBox.critical(self, u'error', u'������ʧ��')
            return
        item.setText(0, text[0])                    
        
        
    '''��Ʒ�б���ѡ��һ��ʱ'''   
    def slotArticleItemChanged(self):
        item = self.ui.treeWidget.currentItem()
        if not item : return
        #��ȡ�ڵ�����,id��Ϣ
        res = self.__getItemIdDepth__(item)
        if not res:
            print 'item data is error'
            return
        '''���δѡ����Ʒ�ڵ�,�����κβ���'''
        if res[1] != 2:
            #print 'item data-depth !=3'
            return
        self.__updateArticleList()
        
    '''���1������,�͸������2�б�'''   
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

    '''�޸�������Ϣ�����ݿ�'''
    def slotModifyArticle(self):
        #Ȩ�޼��
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        article_id = self.__get_selected_article_id()
        if article_id is None: return
        article = dbArticle().getById(article_id)
        dlg = DlgArticleChange(self, article)
        dlg.setModal(True)
        dlg.exec_()
        self.__updateArticleList()

    #ɾ����Ʒ��Ϣ
    def slotDelArticle(self):
        article_id = self.__get_selected_article_id()
        res = QMessageBox.warning(self, u'Σ�ղ���', u'ȷ�ϴ����ݿ���ɾ����ǰѡ�е���Ʒ��Ϣ?', QMessageBox.Yes|QMessageBox.No)
        if res != QMessageBox.Yes: return
        if dbArticle().delete(article_id):
            self.__updateArticleList()
        else:
            QMessageBox.critical(self, u'������', u'ɾ������ִ�г���')
    
    #������1    
    def slotAddType1(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal);
        if text[0] == '': return
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        #print newtype.text
        newtype.parentid  = 0
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'error', u'������1ʧ��')        
        self.__initType1list()
        self.__updateArticleTree()
        
    '''������2'''    
    def slotAddType2(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return

        '''�Ȼ�ȡ�����id'''
        res = self.ui.comboBox_type1.itemData(self.ui.comboBox_type1.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        parentid = int(res[0])
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal);
        if text[0] == '':return
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        newtype.parentid = parentid
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'doo', u'������ʧ��')        
        self.__initType2list()
        self.__updateArticleTree()



    '''����treeview�ؼ�'''    
    def __updateArticleTree(self):
        strListHeader = QStringList()
        strListHeader.append(u'����/�ͺ�')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()
        listTypes1 = dbArticleType().getType1() 
        '''�������1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)
            item.setData(0, Qt.UserRole,  t1.id)
            item.setData(0, Qt.UserRole+1, 1)            
            listType2 = dbArticleType().getType2(t1.id)
            self.ui.treeWidget.addTopLevelItem(item)
            '''�������2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setData(0, Qt.UserRole+0, t2.id)#id
                item2.setData(0, Qt.UserRole+1, 2)#���
                item.addChild(item2)

    #������Ʒ����е���Ʒ�б�
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
        labels = [u'ID',u'�ͺ�/Ʒ��',u'��λ',u'��װ',u'����',u'Ʒ��',u'˵��']
        model = QStandardItemModel(len(article_list), len(labels), self)
        model.setHorizontalHeaderLabels(QStringList(labels))
        #������Ʒ�б�
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
    user.usertype = u"����Ա"
    ims.model.dbSysUser.g_current_user = user
    appp = QApplication(sys.argv)
    window = DlgArticle(None)
    window.setModal(True)
    window.show()
    appp.exec_()