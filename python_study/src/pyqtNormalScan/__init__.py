#encoding=gb2312

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent):
        super(MainWindow, self).__init__(parent)
        self.resize(1024, 768)        
        self.__initToolbarAndMenu()       
        self.tableview = QTableView()
        self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)        
        self.setCentralWidget(self.tableview)
        
        self.action_rec.setCheckable(True)
        self.action_rec_gl.setCheckable(True)
        self.action_rec_mov.setCheckable(True)
        self.action_about.triggered.connect(self.slotAbout)
        self.action_exit.triggered.connect(self.close)
        self.action_tr.triggered.connect(self.slotGenTransmit)
        self.action_rec.triggered.connect(self.slotGenRec)
        self.action_rec_mov.triggered.connect(self.slotGenRec_mov)
        self.action_rec_gl.triggered.connect(self.slotGenRec_gl)
        self.slotGenTransmit()
        
    def __initToolbarAndMenu(self):
        menubar = self.menuBar()
        self.action_exit = QAction(u"退出程序", self)
        menufile = menubar.addMenu(u"文件")
        menufile.addAction(self.action_exit)
        menuview = menubar.addMenu(u"视图")
        self.action_showHheader = QAction(u"显示列头",self)
        self.action_showVheader = QAction(u"显示行头",self)
        self.action_showVheader.setCheckable(True)
        self.action_showHheader.setCheckable(True)
        menuview.addAction(self.action_showVheader)
        menuview.addAction(self.action_showHheader)
        self.menuTrRec = menubar.addMenu(u"发射接收")        
        self.menuHv = menubar.addMenu(u"高压开关")
        self.__initTrRecMenu()
        self.__initHVSwithMenu()   
        self.action_about = QAction(u"About", self)
        menubar.addAction(self.action_about)      
        
        self.__initToolbar0()
        self.__initToolbar1()
        self.toobar0.setMinimumHeight(30)
        
    def __initToolbar1(self):
        self.toobar1 = QToolBar("toobar1")
        self.addToolBar(self.toobar1)
        self.addToolBar(self.toobar0)
        self.toobar1.addAction(self.action_exit)
        self.toobar1.addSeparator()       
        self.toobar1.addAction(self.action_tr)
        self.toobar1.addAction(self.action_rec)
        self.toobar1.addAction(self.action_rec_mov)
        self.toobar1.addAction(self.action_rec_gl)
        
        
    def __initToolbar0(self):
        self.toobar0 = QToolBar("toobar0",self)
        self.editCell    = QLineEdit(u"80", self)
        self.editSubCell = QLineEdit(u"16", self)
        self.editChannel = QLineEdit(u"32", self)
        self.editCell.setMaximumWidth(35)
        self.editSubCell.setMaximumWidth(35)
        self.editChannel.setMaximumWidth(35)
        self.toobar0.addWidget(QLabel(u" 探头阵元数:", self))
        self.toobar0.addWidget(self.editCell)
        self.toobar0.addWidget(QLabel(u" 子阵元数:",self))
        self.toobar0.addWidget(self.editSubCell)
        self.toobar0.addWidget(QLabel(u" 通道数:", self))
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
        
    def __initTrRecMenu(self):
        self.action_tr = QAction(QString.fromUtf8(u"发射"),self)
        self.action_rec= QAction(QString.fromUtf8(u"接收"),self)
        self.action_rec_mov = QAction(QString.fromUtf8(u"接收移动"),self)
        self.action_rec_gl = QAction(QString.fromUtf8(u"归纳接收"), self)
        
        self.menuTrRec.addAction(self.action_tr)
        self.menuTrRec.addAction(self.action_rec)
        self.menuTrRec.addAction(self.action_rec_mov)
        self.menuTrRec.addAction(self.action_rec_gl)
        
    def __initHVSwithMenu(self):
        self.action_hv1 = QAction(u"高压开关1",self)
        self.action_hv2 = QAction(u"高压开关2",self)
        self.action_hv3 = QAction(u"高压开关3", self)
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
        '''
        import TransmitAndRec
        modal = TransmitAndRec.getTr(self)        
        self.tableview.setModel(modal)       
        self.setCellSize(35, 20)
        '''    
    def slotGetHv1(self):
        import hvswitch
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
        import TransmitAndRec
        modal = TransmitAndRec.getRec(self)        
        self.tableview.setModel(modal)       
        self.setCellSize(35, 20)
        self.action_rec.setChecked(True)
        self.action_rec_gl.setChecked(False)
        self.action_rec_mov.setChecked(False)
        
    def slotGenRec_mov(self):
        import TransmitAndRec
        modal = TransmitAndRec.getRecMov(self)        
        self.tableview.setModel(modal)       
        self.setCellSize(35, 20)
        self.action_rec.setChecked(False)
        self.action_rec_gl.setChecked(False)
        self.action_rec_mov.setChecked(True)
        
    def slotGenRec_gl(self):
        import TransmitAndRec
        modal = TransmitAndRec.getRecGl(self)        
        self.tableview.setModel(modal)       
        self.setCellSize(35, 20)
        self.action_rec.setChecked(False)
        self.action_rec_gl.setChecked(True)
        self.action_rec_mov.setChecked(False)
        
    def slotAbout(self):
        QMessageBox.about(self, "About pyqtNormal", "this programe is build for us scan ")
        
    
if __name__=="__main__":
    app =  QtGui.QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    app.exec_()