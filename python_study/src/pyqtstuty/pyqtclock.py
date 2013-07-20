'''
Created on 2013-7-5

@author: jiang
'''
import PyQt4
import PyQt4.QtCore
import PyQt4.QtGui
from  PyQt4.QtGui import *
from  PyQt4.Qt import *
import sys
from PyQt4.uic.Compiler.qtproxies import QtCore
from cocos.rect import Rect
import time
import math

class QWidgetClock(QWidget):
    def __init__(self):
        super(QWidgetClock, self).__init__()
        self.resize(300, 200)
        layoutmain = QVBoxLayout()
       # layoutmain.addWidget(QPushButton("sel colro"))
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layoutmain.addItem(spacerItem)
        self.setLayout(layoutmain)
        self.startTimer(1000)
        
    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        clrbk = QColor.red
        painter.fillRect(self.rect(), Qt.black)
        elWidth = min(self.rect().width(), self.rect().height())
        penline = QPen(Qt.blue)
        painter.setPen(penline)
        ptCenter = QPoint(self.rect().width()/2, self.rect().height()/2)
        
        painter.drawEllipse(ptCenter, elWidth/2, elWidth/2)
        painter.drawEllipse(ptCenter, 2, 2)
        nR = elWidth/2
        tm = time.localtime()
        angleHour = 3.14159*2*tm.tm_hour/12.0
        angleMin  = 3.14159*2*tm.tm_min/60.0
        angleSec  = 3.14159*2*tm.tm_sec/60.0
        ptHour = QPoint(ptCenter.x()+elWidth/2*0.6*math.sin(angleHour), ptCenter.y()-elWidth/2*0.6*math.cos(angleHour))
        ptMin = QPoint(ptCenter.x()+elWidth/2*0.8*math.sin(angleMin), ptCenter.y()-elWidth/2*0.8*math.cos(angleMin))
        ptSec = QPoint(ptCenter.x()+elWidth/2*1.0*math.sin(angleSec), ptCenter.y()-elWidth/2*1.0*math.cos(angleSec))
        
        str = "%d:%2d:%2d"%(tm.tm_hour, tm.tm_min,tm.tm_sec)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(10, 10, str)
        
        #painter.translate(self.rect().width()/2, self.rect().height()/2)
        #painter.rotate(30)
        penHour = QPen(QColor(255, 44, 0))
        penHour.setWidth(3);
        
        penMin = QPen(QColor(255, 88, 0))
        penMin.setWidth(2);      
        
        penSec = QPen(QColor(255, 255, 0))
        penSec.setWidth(1);
        painter.setPen(penHour)        
        painter.drawLine(ptCenter, ptHour)        
        painter.setPen(penMin)
        painter.drawLine(ptCenter, ptMin)        
        painter.setPen(penSec)
        painter.drawLine(ptCenter, ptSec)
        
    def timerEvent(self, *args, **kwargs):
        print 'timer event'
        self.repaint()
        return QWidget.timerEvent(self, *args, **kwargs)
        
        #print 'paint event'        
        
if __name__=="__main__" :
    app = QApplication(sys.argv)
    window = QWidgetClock()
    window.show()
    app.exec_()