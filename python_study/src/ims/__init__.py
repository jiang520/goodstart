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
from ims.DlgStock import DlgStock
from ims.model import dbSysUser
from ims.model.dbInoutRecord import *
from ims.model.dbArticleType import *
from ims.model.dbArticle import *
from ims.DlgLogin import DlgLogin
import ims


class DlgIMSMain(QMainWindow): 
    
    def __init__(self):
        super(DlgIMSMain, self).__init__(None)
        #检查用户登陆信息
        window_login = DlgLogin(self)
        window_login.setModal(True)
        #取消登陆
        if window_login.exec_() != QDialog.Accepted:
            sys.exit(0)
        if ims.model.dbSysUser.g_current_user is None:
            sys.exit(0)
        self.setWindowTitle(u'ut库存管理系统--欢迎使用-%s'%ims.model.dbSysUser.g_current_user.username)
        self.tabWidget = QTabWidget(self)
        self.dlgStock = DlgStock(self)
        self.tabWidget.addTab(self.dlgStock, u'库存列表')
        '''进出货记录'''
        self.dlgRecordSearch = DlgRecordSearch(self)
        self.tabWidget.addTab(self.dlgRecordSearch, u'进出货记录')
        self.tabWidget.addTab(DlgClient(self), u'客户列表')

        '''物品列表'''        
        spliterH = QSplitter(Qt.Horizontal, self)       
        self.treeArticle = QTreeWidget(self)       
        spliterH.addWidget(self.treeArticle)
        spliterH.addWidget(self.tabWidget)
        spliterH.setStretchFactor(0, 40)
        spliterH.setStretchFactor(1, 100)
        self.setCentralWidget(spliterH)

        self.setMinimumSize(800, 600)
        self.resize(800, 600)
        self.__initMenu()
        self.__initToolbar()
        self.__initTreeCtrl_Article()
        self.__udpateArticleTreeView()     
        self.treeArticle.itemSelectionChanged.connect(self.slotSelecteArticle)

    def slotSelecteArticle(self):
        pass
    '''更新物品分类树'''
    def __initTreeCtrl_Article(self):               
        strListHeader = QStringList()
        strListHeader.append(u'物料分类')
        self.treeArticle.setHeaderLabels(strListHeader)
        self.treeArticle.setStyleSheet( "QTreeView::item:hover{background-color:rgb(0,255,0,50)} "
                                          "QTreeView:item{border-bottom:1px solid #999999;border-right:1px solid #999999}"
                                          "QTreeView::item:selected{background-color:rgb(255,0,0,100)}");
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
            item.setBackgroundColor(0, Qt.green)       
            listType2 = dbArticleType().getType2(t1.id)
            '''插入类别2 '''
            for t2 in listType2:
                #print '-',t2.text
                item2 = QTreeWidgetItem()
                item2.setText(0, t2.text)                
                item2.setBackgroundColor(0, Qt.green)
                item.addChild(item2)
                articles = dbArticle().getArticlesByTypeId(t2.id)
                '''插入物品型号'''
                for ac in articles:
                    item3 = QTreeWidgetItem()
                    item3.setText(0, ac.model)
                    item3.setText(1, str(ac.id))
                    item2.addChild(item3)
                    
            self.treeArticle.addTopLevelItem(item)
           
    '''初始化菜单'''          
    def __initMenu(self):
        self.action_in      = QAction(QIcon("images/shopping.png"),u"进货", self)
        self.action_out     = QAction(QIcon("images/sale.png"), u"出货", self)
        self.action_article = QAction(QIcon("images/shipping.png"), u"物料整理", self)
        self.action_client  = QAction(QIcon("images/26.png"),u"客户通讯录", self)
        self.action_backup  = QAction(QIcon("images/timezone.png"), u'备份数据库',self)
        self.action_chart   = QAction(QIcon("images/chart.png"), u"统计曲线", self)
        self.action_exit    = QAction(QIcon("images/Restricted 1.png"),u'退出系统', self)
        self.action_export_remain = QAction(u'导出库存列表',self)
        self.action_export_articl = QAction(u'导出物品列表',self)
        self.action_export_record = QAction(u'导出出库库记录列表', self)
        self.action_about         = QAction(u'关于', self)
        self.action_change_pass   = QAction(u'修改密码', self)
        self.action_admin         = QAction(u'帐户管理', self)

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
        menufile = QMenu(u"文件",self)
        menufile.addAction(self.action_article)
        menufile.addAction(self.action_client)
        menufile.addSeparator()
        menufile.addAction(self.action_exit)

        menuTools = QMenu(u'数据转换工具', self)
        menuTools.addAction(self.action_export_remain)
        menuTools.addAction(self.action_export_articl)
        menuTools.addAction(self.action_export_record)

        menuUser = QMenu(u'帐户设置',self)
        menuUser.addAction(self.action_change_pass)
        menuUser.addSeparator()
        menuUser.addAction(self.action_admin)

        menuSystem = QMenu(u'系统设置',self)
        menuSystem.addAction(self.action_backup)
        action_auto_backup = QAction(u'自动备份数据库', self)
        menuSystem.addAction(action_auto_backup)
        menuSystem.addAction(QAction(u'保存登陆密码',self))

        menubar.addMenu(menufile)
        menubar.addMenu(menuTools)
        menubar.addMenu(menuUser)
        menubar.addMenu(menuSystem)
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


    #导出库存列表
    def slotExportRemain(self):
        filePath = QFileDialog.getSaveFileName(self)
        if not filePath: return
        filePath.append('.txt')
        import ims.FunctionTools
        ims.FunctionTools.ExportTableWidgetData(self.tableViewRemain, filePath)
        QMessageBox.information(self, u'info', u'已导出到%s'%filePath)

    #导出出入库记录
    def slotExportRecord(self):
        filePath = u'%s'%QFileDialog.getSaveFileName(self)
        if filePath=='': return
        filePath = filePath.rstrip(u'.xls')
        filePath = filePath + (u'.xls')
        import ims.FunctionTools
        ims.FunctionTools.ExportTableWidgetDataToExcel(self.dlgRecordSearch.ui.tableView, filePath)
        QMessageBox.information(self, u'info', u'已导出到%s'%filePath)

    def slotAbout(self):
        QMessageBox.about(self,u'库存管理系统',
                          u'''UT库存管理系统,基于python2.7和pyqt4.8构建,\n版权所有,欢迎使用''')

    def slotAdmin(self):
        res = QInputDialog.getText(self, u'系统管理', u'请输入管理员密码', QLineEdit.Password)
        if not res[0]: return
        #if res[1] != u'ut123654': return
        from ims.DlgSysUserAdmin import DlgSysUserAdmin
        dlg = DlgSysUserAdmin(self)
        dlg.setModal(True)
        dlg.exec_()

    #'''备份数据库,将数据库文件复制到其他位置'''
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
            QMessageBox.information(self, 'Successed!', u'数据库已成功备份到\n%s'%dstPath)
        except Exception,e:
            print e
            QMessageBox.critical(self, 'Successed!', u'数据库备份失败%s'%e)




    def slotChangePass(self):
        pass
    def slotLogout(self):
        pass

    '''客户信息管理'''
    def slotDlgClient(self):
        #print 'slot dlg client'
        
        dlg = DlgClient(self)
        dlg.setModal(True)
        dlg.exec_()
    #进货
    def slotIn(self):
        dlg = DlgInOutArticle(self, True)
        dlg.setModal(True)
        dlg.exec_()

    '''出货'''
    def slotOut(self):
        dlg = DlgInOutArticle(self, False)
        dlg.setModal(True)
        dlg.exec_()

    #物品管理
    def slotArticle(self):
        dlg = DlgArticle(self)
        dlg.setModal(True)
        dlg.exec_()
        self.__udpateArticleTreeView()

    def slotChangePassword(self):
        res = QInputDialog.getText(self, u'请输入新密码', u'修改密码', QLineEdit.PasswordEchoOnEdit)
        print '====res = ',res
        if not res[1]: return
        cur_user = ims.model.dbSysUser.g_current_user
        new_password = u'%s'%res[0]

        if not ims.model.dbSysUser.dbSysUser().modifyPassword(cur_user.username, new_password):
            QMessageBox.critical(self, u'error', u'修改密码失败')
        else:
            QMessageBox.information(self, u'error', u'密码已更新')




 #主函数
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT库存管理系统')
    appp.setWindowIcon(QIcon("images/14.png"))

    #检查数据库是否可连接
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '数据库连接错误')
        sys.exit(0)
    #显示主窗口
    window = DlgIMSMain()

    window.show()
    
    appp.exec_()


