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


 #������
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT������ϵͳ')
    appp.setWindowIcon(QIcon(u"images/14.png"))
    #������ݿ��Ƿ������
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '���ݿ����Ӵ���')
        sys.exit(0)

    #��ʾ������
    window = DlgIMSMain(None)
    window.show()
    appp.exec_()


