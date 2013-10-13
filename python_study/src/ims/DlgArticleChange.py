#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from ui import uiDlgArticle
import sys
import ims
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.model.dbArticleType import dbArticleType
from ims.model.dbArticle import dbArticle
from ims.model.dbArticleType import ArticleType
from ims.model.dbArticle import Article
from ims.ui.uiDlgArticleChange import Ui_Dialog
class DlgArticleChange(QDialog):
    """

    """
    def __init__(self, parent=None,  oldArticle=None):
        super(DlgArticleChange,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(u'添加删除物品信息')
        #初始化单位下拉框
        self.ui.comboBox_unit.addItem(u'个')
        self.ui.comboBox_unit.addItem(u'圈')
        self.ui.comboBox_unit.addItem(u'套')
        self.ui.comboBox_unit.addItem(u'件')
        self.ui.comboBox_unit.addItem(u'片')
        self.ui.comboBox_unit.setEditable(True)

        self.__oldArticle = oldArticle
        if self.__oldArticle is None:
            self.ui.plainTextEdit_detail.setPlainText('')
            self.ui.lineEdit_function.setText('')
            self.ui.lineEdit_pp.setText('')
            self.ui.pushButton_add.setText(u'添加')
        else:
            self.ui.plainTextEdit_detail.setPlainText(self.__oldArticle.detail)
            self.ui.lineEdit_model.setText(self.__oldArticle.model)
            self.ui.lineEdit_function.setText(self.__oldArticle.function)
            self.ui.lineEdit_pkg.setText(self.__oldArticle.packaging)
            self.ui.lineEdit_pp.setText(self.__oldArticle.pingpai)
            self.ui.pushButton_add.setText(u'修改')

        #连接信号和糟
        self.ui.pushButton_addtype1.clicked.connect(self.slotAddType1)
        self.ui.pushButton_addtype2.clicked.connect(self.slotAddType2)
        self.ui.pushButton_add.clicked.connect(self.slotOk)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.__initType1list()
        self.__initType2list()

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



        
    '''修改物料信息到数据库'''
    def slotOk(self):
        #权限检查
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():return

        article = Article()
        res = self.ui.comboBox_type2.itemData(self.ui.comboBox_type2.currentIndex()).toInt()
        if not res[1]:
            print 'invadate combobox item data'
            return 
        article.typeid      = int(res[0])
        article.detail      = u'%s'%self.ui.plainTextEdit_detail.toPlainText()
        article.function    = u'%s'%self.ui.lineEdit_function.text()
        article.model       = u'%s'%self.ui.lineEdit_model.text()
        article.packaging   = u'%s'%self.ui.lineEdit_pkg.text()
        article.pingpai     = u'%s'%self.ui.lineEdit_pp.text()
        #型号名必须不能为空
        if article.model == '':
            self.ui.label_tips.setText(u"<span style='color:#ff0000'>型号不能为空</span>")
            self.ui.lineEdit_model.setFocus()
            return

        if self.__oldArticle != None:
            #修改物品信息,id使用旧的物品id
            article.id = self.__oldArticle.id
            if not dbArticle().modify(article):
                QMessageBox.warning(self, u'出错了', u'修改物品信息失败')
                return
            else:
                self.close()
        else:
            #添加物品到库存中
            if not dbArticle().add(article):
                QMessageBox.warning(self, u'出错了', u'修改物品信息失败')
                return
            else:
                #询问是否继续添加
                res = QMessageBox.information(self,u'提示', u'添加物品信息成功,是否继续添加?',QMessageBox.Yes|QMessageBox.No)
                if res != QMessageBox.Yes:
                    self.close


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
    
    '''更新类别1的列表'''    
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



if __name__ == '__main__':
    import ims
    user = ims.model.dbSysUser.SysUser()
    user.usertype = u"管理员"
    ims.model.dbSysUser.g_current_user = user
    appp = QApplication(sys.argv)
    window = DlgArticleChange(None)
    window.setModal(True)
    window.show()
    appp.exec_()