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
from ims.model import dbSysUser
from ims.model.dbInoutRecord import *
from ims.model.dbArticleType import *
from ims.model.dbArticle import *
from ims.DlgLogin import DlgLogin
import ims


class DlgIMSMain(QMainWindow): 
    
    def __init__(self):
        super(DlgIMSMain, self).__init__(None)
        #����û���½��Ϣ
        window_login = DlgLogin(self)
        window_login.setModal(True)
        #ȡ����½
        if window_login.exec_() != QDialog.Accepted:
            sys.exit(0)
        if ims.model.dbSysUser.g_current_user is None:
            sys.exit(0)
        self.setWindowTitle(u'ut������ϵͳ--��ӭʹ��-%s'%ims.model.dbSysUser.g_current_user.username)
        self.tabWidget = QTabWidget(self)
        self.tableViewRemain = QTableView(self)
        self.tabWidget.addTab(self.tableViewRemain, u'����б�')
        '''��������¼'''
        self.dlgRecordSearch = DlgRecordSearch(self)
        self.tabWidget.addTab(self.dlgRecordSearch, u'��������¼')
        self.tabWidget.addTab(DlgClient(self), u'�ͻ��б�')

        '''��Ʒ�б�'''        
        spliterH = QSplitter(Qt.Horizontal, self)       
        self.treeArticle = QTreeWidget(self)       
        spliterH.addWidget(self.treeArticle)

        spliterH.addWidget(self.tabWidget)
        spliterH.setLineWidth(0)
        spliterH.setLineWidth(1)
        spliterH.setStretchFactor(0, 30)
        spliterH.setStretchFactor(1, 100)
        self.setCentralWidget(spliterH)

        self.setMinimumSize(800, 600)
        self.__initMenu()
        self.__initToolbar()
        self.__initTreeCtrl_Article()
        self.__updateArticleCountList()
        self.__udpateArticleTreeView()     
        self.treeArticle.itemSelectionChanged.connect(self.__updateArticleCountList)


    '''������Ʒ������'''
    def __initTreeCtrl_Article(self):               
        strListHeader = QStringList()
        strListHeader.append(u'���Ϸ���')
        #strListHeader.append(u'��װ')
        #strListHeader.append(u'��ע')
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
        '''���һ����ʾ���п�����'''
        item = QTreeWidgetItem()
        item.setText(0,u'��ʾ����')
        item.setText(1,u'-1')
        self.treeArticle.addTopLevelItem(item)

        listTypes1 = dbArticleType().getType1() 
        '''�������1'''       
        for t1 in listTypes1:
            item = QTreeWidgetItem()
            #print t1
            item.setText(0, t1.text)                
            item.setBackgroundColor(0, Qt.green)       
            listType2 = dbArticleType().getType2(t1.id)
            '''�������2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)                
                item2.setBackgroundColor(0, Qt.green)
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''������Ʒ�ͺ�'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, str(ac.id))
                    item2.addChild(item3)
                    
            self.treeArticle.addTopLevelItem(item)
           
    '''��ʼ���˵�'''          
    def __initMenu(self):
        self.action_in      = QAction(QIcon("images/shopping.png"),u"����", self)
        self.action_out     = QAction(QIcon("images/sale.png"), u"����", self)
        self.action_article = QAction(QIcon("images/shipping.png"), u"��������", self)
        self.action_client  = QAction(QIcon("images/26.png"),u"�ͻ�ͨѶ¼", self)
        self.action_backup  = QAction(QIcon("images/timezone.png"), u'�������ݿ�',self)
        self.action_chart   = QAction(QIcon("images/chart.png"), u"ͳ������", self)
        self.action_exit    = QAction(QIcon("images/Restricted 1.png"),u'�˳�ϵͳ', self)
        self.action_export_remain = QAction(u'��������б�',self)
        self.action_export_articl = QAction(u'������Ʒ�б�',self)
        self.action_export_record = QAction(u'����������¼�б�', self)
        self.action_about         = QAction(u'����', self)
        self.action_change_pass   = QAction(u'�޸�����', self)
        self.action_admin         = QAction(u'�ʻ�����', self)

        self.action_client.triggered.connect(self.slotDlgClient)
        self.action_exit.triggered.connect(self.close)
        self.action_in.triggered.connect(self.slotIn)
        self.action_out.triggered.connect(self.slotOut)
        self.action_article.triggered.connect(self.slotArticle)
        self.action_about.triggered.connect(self.slotAbout)
        self.action_backup.triggered.connect(self.slotBackup)

        self.action_export_remain.triggered.connect(self.slotExportRemain)
        self.action_export_record.triggered.connect(self.slotExportRecord)
        self.action_change_pass.triggered.connect(self.slotChangePassword)
        self.action_admin.triggered.connect(self.slotAdmin)

        menubar = self.menuBar()
        menufile = QMenu(u"�ļ�",self)
        menufile.addAction(self.action_article)
        menufile.addAction(self.action_client)
        menufile.addSeparator()
        menufile.addAction(self.action_exit)

        menuTools = QMenu(u'����ת������', self)
        menuTools.addAction(self.action_export_remain)
        menuTools.addAction(self.action_export_articl)
        menuTools.addAction(self.action_export_record)
        menuTools.addSeparator()
        menuTools.addAction(self.action_backup)

        menuUser = QMenu(u'�ʻ�����',self)
        menuUser.addAction(self.action_change_pass)
        menuUser.addSeparator()
        menuUser.addAction(self.action_admin)

        menubar.addMenu(menufile)
        menubar.addMenu(menuTools)
        menubar.addMenu(menuUser)
        menubar.addAction(self.action_about)
        if not ims.model.dbSysUser.g_current_user.is_enable_write_all():
            self.action_in.setEnabled(False)
            self.action_out.setEnabled(False)

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



    #��������б�
    def slotExportRemain(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        import ims.FunctionTools
        ims.FunctionTools.ExportTableWidgetData(self.tableViewRemain, filePath)
        QMessageBox.information(self, u'info', u'�ѵ�����%s'%filePath)

    #����������¼
    def slotExportRecord(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        import ims.FunctionTools
        ims.FunctionTools.ExportTableWidgetData(self.dlgRecordSearch.ui.tableView, filePath)
        QMessageBox.information(self, u'info', u'�ѵ�����%s'%filePath)

    def slotAbout(self):
        QMessageBox.about(self,u'������ϵͳ',
                          u'''UT������ϵͳ,����python2.7��pyqt4.8����,\n��Ȩ����,��ӭʹ��''')

    def slotAdmin(self):
        res = QInputDialog.getText(self, u'ϵͳ����', u'���������Ա����', QLineEdit.Password)
        if not res[0]: return
        #if res[1] != u'ut123654': return
        from ims.DlgSysUserAdmin import DlgSysUserAdmin
        dlg = DlgSysUserAdmin(self)
        dlg.setModal(True)
        dlg.exec_()

    def __getArticleCountListLabels(self):
        labels = QStringList()
        labels.append(u'id')
        labels.append(u'��Ʒ�ͺ�')
        labels.append(u'���')
        labels.append(u'��װ')
        labels.append(u'Ʒ��')
        labels.append(u'��ϸ˵��')
        return labels

    '''�������ݿ�,�����ݿ��ļ����Ƶ�����λ��'''
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
            QMessageBox.information(self, 'Successed!', u'���ݿ��ѳɹ����ݵ�\n%s'%dstPath)
        except Exception,e:
            print e
            QMessageBox.critical(self, 'Successed!', u'���ݿⱸ��ʧ��%s'%e)


    '''
    ������Ʒ����б�
    '''
    def __updateArticleCountList(self):
        item = self.treeArticle.currentItem()
        '''����������Ʒ�Ŀ��'''
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
        model = QStandardItemModel(len(remainlist),5, self)
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

    def slotChangePass(self):
        pass
    def slotLogout(self):
        pass

    '''�ͻ���Ϣ����'''
    def slotDlgClient(self):
        #print 'slot dlg client'
        
        dlg = DlgClient(self)
        dlg.setModal(True)
        dlg.exec_()
    #����
    def slotIn(self):
        dlg = DlgInOutArticle(self, True)
        dlg.setModal(True)
        dlg.exec_()

    '''����'''
    def slotOut(self):
        dlg = DlgInOutArticle(self, False)
        dlg.setModal(True)
        dlg.exec_()

    #��Ʒ����
    def slotArticle(self):
        dlg = DlgArticle(self)
        dlg.setModal(True)
        dlg.exec_()
        self.__udpateArticleTreeView()

    def slotChangePassword(self):
        res = QInputDialog.getText(self, u'������������', u'�޸�����', QLineEdit.PasswordEchoOnEdit)
        print '====res = ',res
        if not res[1]: return
        cur_user = ims.model.dbSysUser.g_current_user
        new_password = u'%s'%res[0]

        if not ims.model.dbSysUser.dbSysUser().modifyPassword(cur_user.username, new_password):
            QMessageBox.critical(self, u'error', u'�޸�����ʧ��')
        else:
            QMessageBox.information(self, u'error', u'�����Ѹ���')




 #������
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT������ϵͳ')
    appp.setWindowIcon(QIcon("images/14.png"))

    #������ݿ��Ƿ������
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '���ݿ����Ӵ���')
        sys.exit(0)
    #��ʾ������
    window = DlgIMSMain()

    window.show()
    
    appp.exec_()


