'''
Created on 2013-7-20

@author: jiang
'''

from PyQt4.QtGui import *
def gethv1(w, h, dlg):
    model = QStandardItemModel(w,h,dlg)
    for y in range(h):
        for x in range(32):
            item = QStandardItem("%d"%1)
            model.setItem(y, y+x, item)
            
    return model            