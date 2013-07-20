'''
Created on 2013-7-20

@author: jiang
'''
from PyQt4.QtGui import *
def getTr(dlg):
    modal = QStandardItemModel(64,33, dlg)
       
    for y in range(64):
        n = y%2==0 and 14 or 15
        x = y/2
        for m in range(16):                
            item = QStandardItem("m%02d"%m)
            modal.setItem(y, x%32,item)
            x = x+1
        for n in range(n, -1, -1):
            item = QStandardItem("n%02d"%n)                
            modal.setItem(y, x%32,item)
            x = x+1
            #pass 
        modal.setItem(y, 32, QStandardItem("i=%d"%((y+30)%64)))  
    return modal