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
        self.ui.pushButton_export.clicked.connect(self.slotExport)
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
        

    '''�Ҽ������˵�'''
    def slotContextMenu(self, item, col):
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        if qApp.mouseButtons() == Qt.LeftButton: return
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]:return
        depth = res[0]                
        rightMenu = QMenu(u"right")
        action_addType      = QAction(QString(u'����'), self)
        action_renameType   = QAction(QString(u'����'), self)
        action_delType      = QAction(QString(u'ɾ��'), self)
        action_addChild     = QAction(QString(u'��������'), self)
        action_addArticle   = QAction(QString(u'������Ʒ'), self)
        #'''�����˵�,��Ʒ�ڵ�����ڵ��Ӧ�˵���һ��'''
        rightMenu.addAction(action_renameType)
        rightMenu.addAction(action_delType)
        rightMenu.addSeparator()
        rightMenu.addAction(action_addType)
        #һ���ڵ������������
        if depth ==1:
            rightMenu.addAction(action_addChild)
        else:
            rightMenu.addAction(action_addArticle)

        #'''�����¼�'''
        action_addType.triggered.connect(self.slotAddType)
        action_renameType.triggered.connect(self.slotRenameType)
        action_delType.triggered.connect(self.slotDelType)
        action_addChild.triggered.connect(self.slotAddChildType)
        action_addArticle.triggered.connect(self.slotAddArticle)
        #'''��ʾ�˵�'''
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


    #'''DELETE��ɾ����Ʒ�ڵ�,���ڵ�'''
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            #tree�����н���ʱ,ɾ�����,����ɾ����Ʒ��
            if self.focusWidget() == self.ui.tableView:
                self.slotDelArticle()
                return
            elif self.focusWidget() == self.ui.treeWidget:
                self.slotDelType()
                return
        return QDialog.keyPressEvent(self, event) 
         
    #'''�����Ʒ����'''
    def slotAddType(self):
        #Ȩ�޼��
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        if itemData == None : return
        if itemData[1] == 1:
            #������Ϊ1,�����idΪ0
            parentid = 0
        else:
            #�����󸸽ڵ�����id
            item_parent = item.parent()
            data_parent = self.__getItemIdDepth__(item_parent)
            if itemData == None: return
            parentid = data_parent[0]
        #��ȡ�������
        text = QInputDialog.getText(self, u'�������',u'������һ���µ��������')
        if not text[1]: return
        if text[0]=="": return
        newtype = ArticleType()
        newtype.text = u'%s'%text[0]
        newtype.parentid = parentid
        #ִ�����ݿ����
        if not dbArticleType().insert(newtype):
            QMessageBox.critical(u'������',u'������ʧ��,������')
        else:
            self.__updateArticleTree()

    #Ϊһ���ڵ����������
    def slotAddChildType(self):
        #Ȩ�޼��
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        parentid = itemData[0]
        if parentid <=0: return
        #��ȡ�������
        text = QInputDialog.getText(self, u'�������',u'������һ���µ��������')
        if not text[1]: return
        if text[0]=="": return
        newtype = ArticleType()
        newtype.text = u'%s'%text[0]
        newtype.parentid = parentid
        #ִ�����ݿ����
        if not dbArticleType().insert(newtype):
            QMessageBox.critical(u'������',u'������ʧ��,������')
        else:
            self.__updateArticleTree()



    #'''ɾ����Ʒ����'''
    def slotDelType(self):
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        if item is None: return
        #����ɾ�����������
        itemdata  = self.__getItemIdDepth__(item)
        if itemdata is None: return
        type_id = itemdata[0]
        depth = itemdata[1]
        print depth
        if depth != 2 and depth != 1: return
        if depth == 2:
            #���2������¶�Ӧ���Ƿ�����ص���Ʒ��Ϣ
            article_list = dbArticle().getArticlesByTypeId(type_id)
            if article_list != None and len(article_list) > 0:
                QMessageBox.critical(self, u'error', u'����ɾ���������������Ʒ!')
                return
        else:
            #1������������Ƿ��������
            if item.childCount() > 0:
                QMessageBox.critical(self, u'error', u'����ɾ�����������')
                return
        #ɾ������
        if QMessageBox.Yes != QMessageBox.warning(self, u'warning', u'ȷ��ɾ��������', QMessageBox.Yes|QMessageBox.No, QMessageBox.No):
            return
        #ɾ�����
        if dbArticleType().delete(type_id):
            self.__updateArticleTree()
        else:
            QMessageBox.critical(self, u'������', u'ɾ������,������')


    #'''����Ʒ���ͽڵ����'''
    def slotRenameType(self):
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
    #������Ʒ�б�
    def slotExport(self):
        import  FunctionTools
        FunctionTools.ExportTableToExcel(self.ui.tableView)
        
        
    #'''��Ʒ�б���ѡ��һ��ʱ'''
    def slotArticleItemChanged(self):
        item = self.ui.treeWidget.currentItem()
        if not item : return
        #��ȡ�ڵ�����,id��Ϣ
        res = self.__getItemIdDepth__(item)
        if not res:
            print 'item data is error'
            return
        #'''���δѡ����Ʒ�ڵ�,�����κβ���'''
        if res[1] != 2:
            #print 'item data-depth !=3'
            return
        self.__updateArticleList()

    #�����Ʒ��Ϣ
    def slotAddArticle(self):
        #if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return
        item = self.ui.treeWidget.currentItem()
        dlg = DlgArticleChange(self)
        if item != None and item.parent() != None:
            strType2 = item.text(0)
            strType1 = item.parent().text(0)
        dlg.setModal(True)
        dlg.exec_()

    #���ص�ǰѡ�����Ʒid,����ɾ��,�޸���Ʒ��Ϣ
    def __get_selected_article_id(self):
        cur_index = self.ui.tableView.currentIndex()
        data = self.ui.tableView.model().index(cur_index.row(), 0).data()
        res = data.toInt()
        if not res[1]: return
        return  res[0]

    #'''�޸�������Ϣ�����ݿ�'''
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
    

    #'''����treeview�ؼ�'''
    def __updateArticleTree(self):
        strListHeader = QStringList()
        strListHeader.append(u'����/�ͺ�')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()
        listTypes1 = dbArticleType().getType1() 
        #'''�������1'''
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)
            item.setData(0, Qt.UserRole,  t1.id)
            item.setData(0, Qt.UserRole+1, 1)            
            listType2 = dbArticleType().getType2(t1.id)
            self.ui.treeWidget.addTopLevelItem(item)
            #'''�������2 '''
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