'''
Created on 2012-6-16

@author: jiang
'''
print 'hello'
from PyQt4.QtGui import *
import PyQt4

import PyQt4.QtGui as QtGui

if __name__ == "__main__":
    print 'heloo'
    import sys    
    app = QtGui.QApplication(sys.argv)
    frame = QtGui.QFrame()
    menubar = QtGui.QMenuBar(frame)
    qstr = PyQt4.QtCore.QString("title")
    type(qstr)
    action1 = QtGui.QAction(qstr, None)
    frame.addAction(action1)
    label = QtGui.QLabel("Hello PyQt!")
    menu = QtGui.QMenu(frame)
    frame.resize(300, 200);

    frame.addAction(QAction('enough',None))
      

    menu.addAction('fuck ')
    menu.addAction("edit")
    menu.addAction("cao")
  #  label.show()
    frame.show()
    sys.exit(app.exec_())
   