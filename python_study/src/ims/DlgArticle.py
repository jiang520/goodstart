#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from ui import uiDlgArticle
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.model.dbArticleType import dbArticleType
from ims.model.dbArticle import dbArticle
from ims.model.dbArticleType import ArticleType
from ims.model.dbArticle import Article
from ims.ui.uiDlgArticle import Ui_Dialog
class DlgArticle(QDialog):   
    
    def __init__(self,parent,  bForChoose=False):
        super(DlgArticle,self).__init__(parent)                
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.__bForChoose = bForChoose
        self.__articleSelected = None
        self.ui.textEdit_detail.setText('')
        self.ui.lineEdit_function.setText('')
        self.ui.lineEdit_pp.setText('')
        self.setWindowTitle(u'��Ʒ��Ϣ')
        self.__initListView()
        self.__initType1list()
        #�����źź���
        self.ui.pushButton_addtype1.clicked.connect(self.slotAddType1)
        self.ui.pushButton_addtype2.clicked.connect(self.slotAddType2)
        self.ui.pushButton_add.clicked.connect(self.slotModifyArticle)
        self.ui.pushButton_cancel.clicked.connect(self.slotCancel)
        self.ui.comboBox_type1.currentIndexChanged[int].connect(self.slotType1changed)
        self.ui.treeWidget.currentItemChanged.connect(self.slotArticleItemChanged)
        self.ui.treeWidget.itemPressed[QTreeWidgetItem, int].connect(self.slotContextMenu)
        #self.ui.treeWidget.setStyleSheet(QString('''::item {border-bottom: 1px solid #777777;border-right:1px solid #777777;color:0xff3333;}'''))
        self.ui.treeWidget.setStyleSheet( "QTreeView::item:hover{background-color:rgb(0,255,0,50)} "
                                          "QTreeView:item{border-bottom:1px solid #999999;border-right:1px solid #999999}"
                                          "QTreeView::item:selected{background-color:rgb(255,0,0,100)}");

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
        '''ѡ��༭����ʾ/���ر༭��'''
        self.ui.checkBox_setedit.clicked[bool].connect(self.setEditing)
        self.setEditing(False)

    '''ѡ��һ����Ʒ'''
    def slotChoosed(self):
        item = self.ui.treeWidget.currentItem()
        if not item: return
        itemData = self.__getItemIdDepth__(item)
        if itemData != None and itemData[1]==3:
            self.__articleSelected = dbArticle().getById(itemData[0])
            self.accept()
    '''����ѡ�е���Ʒ��Ϣ'''
    def getSelectedArticle(self):
        return  self.__articleSelected
        
    ''
    def setEditing(self, bEditing):
        if not bEditing:
            self.ui.groupBox.hide()
        else:
            self.ui.groupBox.show()
            self.slotArticleItemChanged()
    '''�Ҽ������˵�'''
    def slotContextMenu(self, item, col):
        if qApp.mouseButtons() == Qt.LeftButton: return
        res = item.data(0, Qt.UserRole+1).toInt()
        if not res[1]:return
        depth = res[0]                
        rightMenu = QMenu(u"right")
        action_add      = QAction(QString(u'����'), self)
        action_rename   = QAction(QString(u'����'), self)
        action_del      = QAction(QString(u'ɾ��'), self)
        action_edit     = QAction(QString(u'�༭'), self)
        action_edit.setChecked(self.ui.checkBox_setedit.isChecked())
        action_addchild = QAction(QString(u'��������'), self)
        '''�����˵�'''
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
            self.__initListView()
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
            self.__initListView()
        else:
            QMessageBox.critical(self, u'error', u'���ʧ��')
            
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
         
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.slotDel()
            return
        return QDialog.keyPressEvent(self, event) 
         
    '''�����Ʒ����'''
    def slotAdd(self):
        item = self.ui.treeWidget.currentItem()
        if item == None:return
        itemData = self.__getItemIdDepth__(item)
        if itemData == None : return       
        if itemData[1]==1:
            parentid = 0
            self.__AddType(parentid)
        elif itemData[1] == 2:
            parentItemData = self.__getItemIdDepth__(item.parent())
            if parentItemData==None: return
            parentid = parentItemData[0]
            self.__AddType(parentid)
        else:
            parentItemData = self.__getItemIdDepth__(item.parent())
            if parentItemData==None: return
            parentid = parentItemData[0]
            self.__AddArticle(parentid, item.parent())        
            
    def slotEdit(self):
        bEditing = self.ui.checkBox_setedit.isChecked()
        self.ui.checkBox_setedit.setChecked(not bEditing)  
        self.setEditing(not bEditing)
    '''ɾ����Ʒ����'''        
    def slotDel(self):
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
                self.__initListView()
        elif depth == 2:
            #print 'del type'
            if dbArticleType().delete(id):
                item.parent().removeChild(item)
        else:
            '''depth = 3'''
            #print 'del article'
            if dbArticle().delete(id):       
                item.parent().removeChild(item)
            else:
                print 'del article faield'
                
    def slotRename(self):
        item = self.ui.treeWidget.currentItem()
        if not item : return
        res = self.__getItemIdDepth__(item)
        if not res : return
        id , depth = res
        text = QInputDialog.getText(self,
                    QString(u"���������" ),
                    QString(u"������һ���������") ,
                    QLineEdit.Normal,
                    QString(item.text(0)));                    
        if not text[1]: return       
        if depth == 3: return        
        if not dbArticleType().rename(id, text[0]):
            QMessageBox.critical(self, u'error', u'������ʧ��')
            return
        item.setText(0, text[0])                    
        
        
    '''��Ʒ�б���ѡ��һ��ʱ'''   
    def slotArticleItemChanged(self):
        self.ui.groupBox.setEnabled(False)
        item = self.ui.treeWidget.currentItem()        
        if not item : return
        #��ȡ�ڵ�����,id��Ϣ
        res = self.__getItemIdDepth__(item) 
        if not res: 
            print 'item data is error'
            return
        '''���δѡ����Ʒ�ڵ�,�����κβ���'''
        if res[1] != 3:
            #print 'item data-depth !=3'
            return
        '''���Ǳ༭״̬Ҳ�������Ҳ��������Ϣ'''
        if not self.ui.checkBox_setedit.isChecked():
            return
        articleid = res[0]
        #������Ʒ��Ϣ,�����µ��Ҳ��б���
        self.__articleSelected = dbArticle().getById(articleid)
        if not self.__articleSelected: return
        '''�����Ҳ��combobox �����б�ѡ����'''
        strType1 = item.parent().parent().text(0)
        strType2 = item.parent().text(0)
        for i in range(self.ui.comboBox_type1.count()):
            if self.ui.comboBox_type1.itemText(i) == strType1:
                self.ui.comboBox_type1.setCurrentIndex(i)
        self.__initType2list() 
        for i in range(self.ui.comboBox_type2.count()):
            if self.ui.comboBox_type2.itemText(i) == strType2:
                self.ui.comboBox_type2.setCurrentIndex(i)
        '''���±༭����Ϣ'''
        self.ui.lineEdit_function.setText(self.__articleSelected.function)
        self.ui.lineEdit_model.setText(self.__articleSelected.model)
        self.ui.lineEdit_pkg.setText(self.__articleSelected.packaging)
        self.ui.lineEdit_pp.setText(self.__articleSelected.pingpai)
        self.ui.textEdit_detail.setText(self.__articleSelected.detail)
        self.ui.groupBox.setEnabled(True)
        self.ui.pushButton_add.setEnabled(True)
        
    '''���1������,�͸������2�б�'''   
    def slotType1changed(self):
        #print 'type 1 changed '
        self.__initType2list()
        
    '''���������Ϣ�����ݿ�'''     
    def slotModifyArticle(self):
        article = Article()
        res = self.ui.comboBox_type2.itemData(self.ui.comboBox_type2.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        article.typeid      = int(res[0])
        article.detail      = u'%s'%self.ui.textEdit_detail.toPlainText()
        article.function    = u'%s'%self.ui.lineEdit_function.text()
        article.model       = u'%s'%self.ui.lineEdit_model.text()
        article.packaging   = u'%s'%self.ui.lineEdit_pkg.text()
        article.pingpai     = u'%s'%self.ui.lineEdit_pp.text()
        article.id          = u'%s'%self.__articleSelected.articleid
        if article.model == '':
            self.ui.label_tips.setText(u"<span style='color:#ff0000'>�ͺŲ���Ϊ��</span>")            
            self.ui.lineEdit_model.setFocus()
            return
        if not dbArticle().modify(article):
            QMessageBox.warning(self, u'add', 'failed')
            return
        self.__initListView()
    
    def slotTypeChoosed(self):
        items =  self.ui.treeWidget.selectedItems()
        if len(items) <1:
            return
        item0 =items[0]# QTreeWidgetItem()
        #print item0.text(1)
        self.ui.comboBox_type.clear()
        self.ui.comboBox_type.addItem(item0.text(1))
    
    #������1    
    def slotAddType1(self):
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
        self.__initListView()
        
    '''������2'''    
    def slotAddType2(self):
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
        self.__initListView()    
    
    '''�������1���б�'''    
    def __initType1list(self):
        self.ui.comboBox_type1.clear()
        listTypes = dbArticleType().getType1()
        for atype in listTypes:
            str = u'%s'%atype.text
            self.ui.comboBox_type1.addItem(str,atype.id)
        self.__initType2list()
        
    '''#�������2���б�   ''' 
    def __initType2list(self):
        self.ui.pushButton_add.setEnabled(False)
        self.ui.comboBox_type2.clear()
        vtype1_id = self.ui.comboBox_type1.itemData(self.ui.comboBox_type1.currentIndex())
        res = vtype1_id.toInt()
        #print res
        if not res[1]:
            #print 'return'
            return        
        listTypes = dbArticleType().getType2(res[0])
        for atype in listTypes:
            str = u'%s'%atype.text
            #print str
            self.ui.comboBox_type2.addItem(str,atype.id)
        self.ui.pushButton_add.setEnabled(self.ui.comboBox_type2.count() > 0)

    '''����treeview�ؼ�'''    
    def __initListView(self):       
        strListHeader = QStringList()
        strListHeader.append(u'����/�ͺ�')
        strListHeader.append(u'��װ')        
        strListHeader.append(u'Ʒ��')
        strListHeader.append(u'��ע')
        strListHeader.append(u'')
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
            '''�������2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setData(0, Qt.UserRole+0, t2.id)#id
                item2.setData(0, Qt.UserRole+1, 2)#���
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''������Ʒ�ͺ�'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setData(0, Qt.UserRole+0, ac.id)
                    item3.setData(0, Qt.UserRole+1, 3)
                    item3.setText(1, ac.packaging)
                    item3.setText(2, ac.pingpai)
                    item3.setText(3, ac.detail)
                    item2.addChild(item3)
            self.ui.treeWidget.addTopLevelItem(item)
  
        
    '''����˳�'''
    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgArticle(None)
    window.setModal(True)
    window.show()
    appp.exec_()