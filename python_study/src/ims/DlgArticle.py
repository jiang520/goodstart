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
class DlgArticle(QDialog):
    
    def __init__(self):
        super(DlgArticle,self).__init__(None)                
        self.ui = uiDlgArticle.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle(u'添加物品信息')
        self.__initListView()
        self.__initType1list()
        self.ui.pushButton_addtype1.clicked.connect(self.slotAddType1)
        self.ui.pushButton_addtype2.clicked.connect(self.slotAddType2)
        self.ui.pushButton_add.clicked.connect(self.slotAddArticle)
        self.ui.pushButton_cancel.clicked.connect(self.slotCancel)
        self.ui.comboBox_type1.currentIndexChanged[int].connect(self.slotType1changed)
    def slotType1changed(self):
        print 'type 1 changed '
        self.__initType2list()
         
    def slotAddArticle(self):
        article = Article()
        res = self.ui.comboBox_type2.itemData(self.ui.comboBox_type2.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        article.typeid = int(res[0])
        article.detail = self.ui.lineEdit_detail.text()
        article.function = self.ui.lineEdit_function.text()
        article.model = self.ui.lineEdit_model.text()
        article.packaging = self.ui.lineEdit_pkg.text()
        if not dbArticle().add(article):
            QMessageBox.warning(self, u'add', 'failed')
    
    def slotTypeChoosed(self):
        items =  self.ui.treeWidget.selectedItems()
        if len(items) <1:
            return
        item0 =items[0]# QTreeWidgetItem()
        print item0.text(1)
        self.ui.comboBox_type.clear()
        self.ui.comboBox_type.addItem(item0.text(1))
    
    #添加类别1    
    def slotAddType1(self):
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"Application name" ),
                    QString(u"Please enter your name") ,
                    QLineEdit.Normal);
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        #print newtype.text
        newtype.parentid  = 0
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'error', u'添加类别1失败')        
        self.__initType1list()
        self.__initListView()
        
    #添加类别2    
    def slotAddType2(self):
        #先获取父类别id
        res = self.ui.comboBox_type1.itemData(self.ui.comboBox_type1.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        parentid = int(res[0])
        #msg = QMessageBox.information(self, u'input', u'input')
        text = QInputDialog.getText(self,
                    QString(u"Application name" ),
                    QString(u"Please enter your name") ,
                    QLineEdit.Normal);
        newtype = ArticleType()
        newtype.text = unicode(text[0])
        newtype.parentid = parentid
        if not dbArticleType().insert(newtype):
            QMessageBox.warning(self, u'doo', u'添加类别失败')        
        self.__initType2list()
        self.__initListView()    
    
    #更新类别1的列表    
    def __initType1list(self):
        self.ui.comboBox_type1.clear()
        listTypes = dbArticleType().getType1()
        for atype in listTypes:
            str = u'%s'%atype.text
            self.ui.comboBox_type1.addItem(str,atype.id)
        self.__initType2list()
        
    '''#更新类别2的列表   ''' 
    def __initType2list(self):
        self.ui.pushButton_add.setEnabled(False)
        self.ui.comboBox_type2.clear()
        vtype1_id = self.ui.comboBox_type1.itemData(self.ui.comboBox_type1.currentIndex())
        res = vtype1_id.toInt()
        print res
        if not res[1]:
            print 'return'
            return        
        listTypes = dbArticleType().getType2(res[0])
        for atype in listTypes:
            str = u'%s'%atype.text
            print str
            self.ui.comboBox_type2.addItem(str,atype.id)
        self.ui.pushButton_add.setEnabled(self.ui.comboBox_type2.count() > 0)
    '''更新treeview控件'''    
    def __initListView(self):       
        strListHeader = QStringList()
        strListHeader.append(u'分类')
        strListHeader.append(u'封装')
        strListHeader.append(u'备注')
        strListHeader.append(u'')
        self.ui.treeWidget.setHeaderLabels(strListHeader)
        self.ui.treeWidget.clear()
        listTypes1 = dbArticleType().getType1() 
        '''插入类别1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            print t1
            item.setText(0, t1.text)
            item.setText(3, str(t1.id))            
            listType2 = dbArticleType().getType2(t1.id)
            '''插入类别2 '''
            for t2 in listType2:
                print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)
                item2.setText(3, str(t2.id))
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''插入物品型号'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, ac.packaging)
                    item3.setText(2, ac.detail)
                    item3.setText(3, str(ac.id))
                    item2.addChild(item3)
            self.ui.treeWidget.addTopLevelItem(item)
    def slotDelItem(self):
        pass
        
    '''点击退出'''
    def slotCancel(self):
        self.close()

if __name__ == '__main__':
    appp = QApplication(sys.argv)
    window = DlgArticle()
    window.setModal(True)
    window.show()
    appp.exec_()