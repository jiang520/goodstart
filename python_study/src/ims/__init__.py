#encoding=gb2312
'''
Created on 2013-6-6
@author: jiang
'''

import sys
#from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ims.DlgIMSMain import DlgIMSMain
from ims.DlgLogin import *
from ims.model.dbActicleIMS import *
from ims.model.SysConfigFile import g_configfile
import ims
import os
 #主函数
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT库存管理系统')
    appp.setApplicationVersion(u'0.4.0.0')
    appp.setWindowIcon(QIcon(u"images/stock.png"))
    #检查数据库是否可连接
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '数据库连接错误')
        sys.exit(0)
    #初始化设置配置文件路径
    g_configfile.setFilePath('%s\\config.ini'%os.getcwd())
    g_configfile.addUserName('admin')
    g_configfile.addUserName('jiang')
    g_configfile.addClientTypes('供货商')
    g_configfile.addClientTypes('一级经销商')
    g_configfile.addClientTypes('医院')

    #登录检查
    dlg = DlgLogin(None)
    dlg.setModal(True)
    if dlg.exec_()!=QDialog.Accepted:
        sys.exit(0)
    #显示主窗口
    window = DlgIMSMain(None)
    window.show()
    appp.exec_()


