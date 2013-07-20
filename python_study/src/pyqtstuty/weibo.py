'''
Created on 2013-7-17

@author: jiang
'''
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import logging
import logging.config
from sina_weibo_main import  SinaWeibo 
import urllib2

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class MyQQ(QTabWidget):
    def __init__(self,parent=None):
        super(MyQQ,self).__init__(parent)
        self.setWindowTitle(u'΢������')
        y=self.frameGeometry().width()*2
        self.setGeometry(y-150, 100, 150, 400)
        logging.config.fileConfig('logging.conf')
        self.logger=logging.getLogger('chat')
        self.weibo=SinaWeibo()      #��������΢��API��һ���࣬�˽���˶���
        self.uid=self.weibo.uid        #��ȡ�ҵ�uid
        self.setWindowIcon(QIcon('image/sina.ico'))     #����ͼ��
    
        self.funList=[]
        self.total_friends=0
        next_cursor = -1
        while next_cursor != 0:
            timeline = self.weibo.api.followers(self.uid,'','','',next_cursor)
            if isinstance(timeline, tuple):
                next_cursor = timeline[1]
                self.total_friends += len(timeline[0])
                for line in timeline[0]:
                    #if line.__getattribute__('online_status')==1:     #�û�������״̬��0�������ߡ�1������
                        fid = line.__getattribute__("id")    #��ȡ��˿��uid
                        name = line.__getattribute__("screen_name")   #��ȡ��˿��name
                        profile_image_url=line.__getattribute__('profile_image_url')   #��ȡ��˿��ͷ��url
                        self.funList.append([fid, name])
                        re = urllib2.Request(r'%s' %profile_image_url)   
                        rs = urllib2.urlopen(re).read()
                        picname='data/%s' %fid
                        open(picname, 'wb').write(rs)     #���ط�˿��ͷ��
            else:
                next_cursor = 0
                self.total_friends += len(timeline)
                for line in timeline:
                    #if line.__getattribute__('online_status')==1:     #�û�������״̬��0�������ߡ�1������
                        fid = line.__getattribute__("id")
                        name = line.__getattribute__("screen_name")
                        profile_image_url=line.__getattribute__('profile_image_url')
                        self.funList.append([fid, name])
                        re = urllib2.Request(r'%s' %profile_image_url)
                        rs = urllib2.urlopen(re).read()
                        picname='data/%s' %fid
                        open(picname, 'wb').write(rs)
                        
        

        groupbox1=QGroupBox()
        vlayout1=QVBoxLayout(groupbox1)
        vlayout1.setMargin(10)
        vlayout1.setAlignment(Qt.AlignCenter)

        for fun in self.funList:
            myfun=QToolButton()
            self.connect(myfun, SIGNAL('clicked()'), self.communicate)   #�󶨵����Ӧ����
            myfun.setText(self.tr('%s' %fun[1]))
            myfun.setIcon(QIcon('data/%s' %fun[0]))      #���÷�˿ͷ��
            myfun.setIconSize(QSize(60, 60))
            myfun.setAutoRaise(True)
            myfun.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            vlayout1.addWidget(myfun)
        vlayout1.addStretch()
        
    
        toolButton2_1=QToolButton()
        toolButton2_1.setText(self.tr("���Լ�"))
        toolButton2_1.setIcon(QIcon("image/9.jpg"))
        toolButton2_1.setIconSize(QSize(60,60))
        toolButton2_1.setAutoRaise(True)
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.connect(toolButton2_1, SIGNAL('clicked()'), self.getIp)  #������Ӧ����


        toolButton3_1=QToolButton()
        toolButton3_1.setText(self.tr("���Լ�"))
        toolButton3_1.setIcon(QIcon("image/9.jpg"))
        toolButton3_1.setIconSize(QSize(60,60))
        toolButton3_1.setAutoRaise(True)
        toolButton3_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        groupbox2=QGroupBox()
        vlayout2=QVBoxLayout(groupbox2)
        vlayout2.setMargin(10)
        vlayout2.setAlignment(Qt.AlignCenter)
        vlayout2.addWidget(toolButton2_1)

        groupbox3=QGroupBox()
        vlayout3=QVBoxLayout(groupbox3)
        vlayout3.setMargin(10)
        vlayout3.setAlignment(Qt.AlignCenter)
        vlayout3.addWidget(toolButton3_1)
        
        toolbox1 = QToolBox()
        toolbox1.addItem(groupbox1,self.tr("�ҵķ�˿[%s]" %self.total_friends))
        toolbox1.addItem(groupbox2,self.tr("�ҵĹ�ע[0]"))
        toolbox1.addItem(groupbox3,self.tr("������"))
        toolbox1.setItemIcon(0, QIcon('image/fan.png'))
        toolbox1.setItemIcon(1, QIcon('image/care.png'))
        toolbox1.setItemIcon(2, QIcon('image/black.png'))
        toolbox2=QToolBox()
        
        self.addTab(toolbox1, self.tr('�ҵ�����'))
        self.addTab(toolbox2, self.tr('�ҵ�΢Ⱥ'))
        self.setTabIcon(0, QIcon('image/chat.png'))
        self.setTabIcon(1, QIcon('image/weiqun.jpg'))
        
        
    def communicate(self):
        QMessageBox.information(self,self.tr("������....."),  self.tr("������.......!"))
        
    def getIp(self):
        city_info=urllib2.urlopen('http://pv.sohu.com/cityjson').read()
        ip=city_info.split('=')[1].split(',')[0].split(':')[1]   #��ȡ�ҵ�IP��ַ
        QMessageBox.information(self, self.tr('�ҵĵ�ַ'), self.tr('�ҵ�IP%s' %ip))

if __name__=='__main__':
    app=QApplication(sys.argv)
    myqq=MyQQ()
    myqq.show()
    app.exec_()
