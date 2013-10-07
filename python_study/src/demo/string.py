'''
Created on 2012-6-16

@author: jiang
'''
print 'hello'
from PyQt4.QtGui import *
import PyQt4

import PyQt4.QtGui as QtGui

class FrameDemo(QFrame):
    def __init__(self):
        super(FrameDemo, self).__init__(None)
        
        qstr = PyQt4.QtCore.QString("title")
        type(qstr)
        action1 = QtGui.QAction(qstr, None)
        self.addAction(action1)
        label = QtGui.QLabel("Hello PyQt!")
        menu = QtGui.QMenu(self)
        self.resize(300, 200);
        self.addAction(QAction('enough',None)) 
    
        menu.addAction('fuck ')
        menu.addAction("edit")
        menu.addAction("cao")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('fuck',self))
        layout.addWidget(QLineEdit("fuckofff", self))
        self.setLayout(layout)

if __name__ == "__main__":
    print 'heloo'
    import sys    
    app = QtGui.QApplication(sys.argv)
    frame = FrameDemo()   
  #  label.show()
    frame.show()
    sys.exit(app.exec_())
   