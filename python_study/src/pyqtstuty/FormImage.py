'''
Created on 2013-6-6

@author: jiang
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import uiFormImage
class FormImage(QWidget):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        super(FormImage, self).__init__(parent)
        self.ui = uiFormImage.Ui_FormImage()
        self.ui.setupUi(self)
        self.img  = None
        self.resize(200, 500)
        self.setimagepath("d:\\pic\\steve_nash.jpg")
        
        
    def setimagepath(self, path):
        import os
        if not os.path.isfile(path):
            return None
        #print 'load file at path:',path
        self.img = QImage(QString.fromUtf8(unicode(path)))
        if self.img == None or self.img.width()==0 or self.img.height() == 0:
            print 'load image failed:',path
            return
        self.repaint()
        
    '''
    draw image on the dialog,with the same x/y rate
    '''
    def paintEvent(self, *args, **kwargs):
        #print 'on paintevent'
        painter = QPainter(self)
        
        painter.fillRect(self.rect(), QBrush(QColor(33, 33,33)) )
        painter.drawText(QPoint(33, 44), "QString")
        
        if self.img != None and self.img.width()!=0 and self.img.height() != 0:
            #print self.img.width(),'X',self.img.height()
            #zoom rate
            fzoom = min(self.width()*1.0/self.img.width(),self.height()*1.0/self.img.height())
            print fzoom
            w = self.img.width()*fzoom
            h = self.img.height()*fzoom
            rect2 = QRectF()
            #print help(rect2.setRect)
            rect2.setRect(self.width()/2.0-w/2, self.height()/2.0-h/2, w, h)
            painter.drawImage(rect2, self.img)
        return QWidget.paintEvent(self, *args, **kwargs)
    
if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    window = FormImage()
    window.show()
    app.exec_()

    