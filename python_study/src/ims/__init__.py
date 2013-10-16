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
import ims


 #主函数
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT库存管理系统')
    appp.setWindowIcon(QIcon(u"images/14.png"))
    #检查数据库是否可连接
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '数据库连接错误')
        sys.exit(0)

    #显示主窗口
    window = DlgIMSMain(None)
    window.show()
    appp.exec_()


