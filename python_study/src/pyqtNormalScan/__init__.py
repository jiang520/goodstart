#encoding=gb2312

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent):
        super(MainWindow, self).__init__(parent)
        self.resize(1024, 768)
        self.action_exit = QAction(u"�˳�����", self)
        
        self.__initToolbarAndMenu()
       
        self.tableview = QTableView()
        self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)        
        self.setCentralWidget(self.tableview)
        
        self.action_exit.triggered.connect(self.close)
        self.action_tr.triggered.connect(self.slotGenTransmit)
        self.action_rec.triggered.connect(self.slotGenRec)
        self.action_rec_mov.triggered.connect(self.slotGenRec_mov)
        self.action_rec_gl.triggered.connect(self.slotGenRec_gl)
        self.slotGenTransmit()
        
    def __initToolbarAndMenu(self):
        menubar = self.menuBar()
        menufile = menubar.addMenu(u"�ļ�")
        menufile.addAction(self.action_exit)
        menuview = menubar.addMenu(u"��ͼ")
        self.action_showHheader = QAction(u"��ʾ��ͷ",self)
        self.action_showVheader = QAction(u"��ʾ��ͷ",self)
        self.action_showVheader.setCheckable(True)
        self.action_showHheader.setCheckable(True)
        menuview.addAction(self.action_showVheader)
        menuview.addAction(self.action_showHheader)
        menuedit = menubar.addMenu(u"�������")
        menuedit.addAction(QAction("receive",self))
        self.menuHv = menubar.addMenu(u"��ѹ����")
        self.__initHVSwithMenu()       
        
        menubar.addAction(self.action_exit)
        self.toobar0 = QToolBar("toobar0",self)
        self.editCell    = QLineEdit(u"80", self)
        self.editSubCell = QLineEdit(u"16", self)
        self.editChannel = QLineEdit(u"32", self)
        self.editCell.setMaximumWidth(35)
        self.editSubCell.setMaximumWidth(35)
        self.editChannel.setMaximumWidth(35)
        self.toobar0.addWidget(QLabel(u" ̽ͷ��Ԫ��:", self))
        self.toobar0.addWidget(self.editCell)
        self.toobar0.addWidget(QLabel(u" ����Ԫ��:",self))
        self.toobar0.addWidget(self.editSubCell)
        self.toobar0.addWidget(QLabel(u" ͨ����:", self))
        self.toobar0.addWidget(self.editChannel)
        self.checkLock = QCheckBox(u"lock", self)
        self.toobar0.addWidget(self.checkLock)
        self.checkLock.toggled.connect(self.slotCheckConfig)
        self.toobar0.addSeparator()
        self.action_showVheader.setChecked(True)
        self.action_showHheader.setChecked(True)
        #self.toobar0.addAction(self.action_showVheader)
        #self.toobar0.addAction(self.action_showHheader)
        self.action_showVheader.toggled.connect(self.slotShowRowHeader)
        self.action_showHheader.toggled.connect(self.slotShowColHeader)
        
        self.toobar1 = QToolBar("toobar1")
        self.addToolBar(self.toobar1)
        self.addToolBar(self.toobar0)
        self.toobar0.setMinimumHeight(30)
        self.toobar1.addAction(self.action_exit)
        self.toobar1.addSeparator()
        self.action_tr = QAction(QString.fromUtf8(u"����"),self)
        self.action_rec= QAction(QString.fromUtf8(u"����"),self)
        self.action_rec_mov = QAction(QString.fromUtf8(u"�����ƶ�"),self)
        self.action_rec_gl = QAction(QString.fromUtf8(u"���ɽ���"), self)
        
        
        self.toobar1.addAction(self.action_tr)
        self.toobar1.addAction(self.action_rec)
        self.toobar1.addAction(self.action_rec_mov)
        self.toobar1.addAction(self.action_rec_gl)
        
    def __initHVSwithMenu(self):
        self.action_hv1 = QAction(u"��ѹ����1",self)
        self.action_hv2 = QAction(u"��ѹ����2",self)
        self.action_hv3 = QAction(u"��ѹ����3", self)
        self.menuHv.addAction(self.action_hv1)
        self.menuHv.addAction(self.action_hv2)
        self.menuHv.addAction(self.action_hv3)        
        print 'connect'
        self.action_hv1.triggered.connect(self.slotGetHv1)
        
    def slotShowRowHeader(self):
        bShow = self.action_showVheader.isChecked()
        if bShow:
            self.tableview.verticalHeader().show()
        else:
            self.tableview.verticalHeader().hide()
    def slotShowColHeader(self):
        bShow = self.action_showHheader.isChecked()
        if bShow:
            self.tableview.horizontalHeader().show()
        else:
            self.tableview.horizontalHeader().hide()
    def slotCheckConfig(self):
        bLocked = self.checkLock.isChecked()
        self.editCell.setEnabled(not bLocked)
        self.editSubCell.setEnabled(not bLocked)
        self.editChannel.setEnabled(not bLocked)
            
    def slotGenTransmit(self):
        import TransmitAndRec
        modal = TransmitAndRec.getTr(self)        
        self.tableview.setModel(modal)       
        self.setCellSize(35, 20)
            
    def slotGetHv1(self):
        import hvswitch
        print '=======get hv 1'
        model = hvswitch.gethv1(80,80,self)
        self.tableview.setModel(model)
        self.setCellSize(15, 20)
        
    def setCellSize(self,width,height):
        model = self.tableview.model()        
        for x in range(model.columnCount()):
            self.tableview.setColumnWidth(x, width)
        for y in range(model.rowCount()):
            self.tableview.setRowHeight(y, height)       
    def slotGenRec(self):
        pass
    def slotGenRec_mov(self):
        pass
    def slotGenRec_gl(self):
        pass
    
if __name__=="__main__":
    app =  QtGui.QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    app.exec_()