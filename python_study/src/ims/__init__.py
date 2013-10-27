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
 #������
if __name__ == '__main__':
    appp = QApplication(sys.argv)
    appp.setApplicationName(u'UT������ϵͳ')
    appp.setApplicationVersion(u'0.4.0.0')
    appp.setWindowIcon(QIcon(u"images/stock.png"))
    #������ݿ��Ƿ������
    if dbActicleIMS.getInstance().getConnection() is None:
        QMessageBox.critical(None, u'Error', '���ݿ����Ӵ���')
        sys.exit(0)
    #��ʼ�����������ļ�·��
    g_configfile.setFilePath('%s\\config.ini'%os.getcwd())
    g_configfile.addUserName('admin')
    g_configfile.addUserName('jiang')
    g_configfile.addClientTypes('������')
    g_configfile.addClientTypes('һ��������')
    g_configfile.addClientTypes('ҽԺ')

    #��¼���
    dlg = DlgLogin(None)
    dlg.setModal(True)
    if dlg.exec_()!=QDialog.Accepted:
        sys.exit(0)
    #��ʾ������
    window = DlgIMSMain(None)
    window.show()
    appp.exec_()


