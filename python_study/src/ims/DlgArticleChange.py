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
        self.setWindowTitle(u'���ɾ����Ʒ��Ϣ')
        #��ʼ����λ������
        self.ui.comboBox_unit.addItem(u'��')
        self.ui.comboBox_unit.addItem(u'Ȧ')
        self.ui.comboBox_unit.addItem(u'��')
        self.ui.comboBox_unit.addItem(u'��')
        self.ui.comboBox_unit.addItem(u'Ƭ')
        self.ui.comboBox_unit.setEditable(True)

        self.__oldArticle = oldArticle
        if self.__oldArticle is None:
            self.ui.plainTextEdit_detail.setPlainText('')
            self.ui.lineEdit_function.setText('')
            self.ui.lineEdit_pp.setText('')
            self.ui.pushButton_add.setText(u'���')
        else:
            self.ui.plainTextEdit_detail.setPlainText(self.__oldArticle.detail)
            self.ui.lineEdit_model.setText(self.__oldArticle.model)
            self.ui.lineEdit_function.setText(self.__oldArticle.function)
            self.ui.lineEdit_pkg.setText(self.__oldArticle.packaging)
            self.ui.lineEdit_pp.setText(self.__oldArticle.pingpai)
            self.ui.pushButton_add.setText(u'�޸�')

        #�����źź���
        self.ui.pushButton_addtype1.clicked.connect(self.slotAddType1)
        self.ui.pushButton_addtype2.clicked.connect(self.slotAddType2)
        self.ui.pushButton_add.clicked.connect(self.slotOk)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.__initType1list()
        self.__initType2list()

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



        
    '''�޸�������Ϣ�����ݿ�'''
    def slotOk(self):
        #Ȩ�޼��
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
        #�ͺ������벻��Ϊ��
        if article.model == '':
            self.ui.label_tips.setText(u"<span style='color:#ff0000'>�ͺŲ���Ϊ��</span>")
            self.ui.lineEdit_model.setFocus()
            return

        if self.__oldArticle != None:
            #�޸���Ʒ��Ϣ,idʹ�þɵ���Ʒid
            article.id = self.__oldArticle.id
            if not dbArticle().modify(article):
                QMessageBox.warning(self, u'������', u'�޸���Ʒ��Ϣʧ��')
                return
            else:
                self.close()
        else:
            #�����Ʒ�������
            if not dbArticle().add(article):
                QMessageBox.warning(self, u'������', u'�޸���Ʒ��Ϣʧ��')
                return
            else:
                #ѯ���Ƿ�������
                res = QMessageBox.information(self,u'��ʾ', u'�����Ʒ��Ϣ�ɹ�,�Ƿ�������?',QMessageBox.Yes|QMessageBox.No)
                if res != QMessageBox.Yes:
                    self.close


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



if __name__ == '__main__':
    import ims
    user = ims.model.dbSysUser.SysUser()
    user.usertype = u"����Ա"
    ims.model.dbSysUser.g_current_user = user
    appp = QApplication(sys.argv)
    window = DlgArticleChange(None)
    window.setModal(True)
    window.show()
    appp.exec_()