'''
Created on 2013-7-20

@author: jiang
'''
from PyQt4.QtGui import *
class TableGetter:
    def __init__(self, probecell, subcell,channel):
            self.probecell = probecell
            self.subcell = subcell
            self.channel = channel
            
    def getRecGl(self, dlg):
        model = QStandardItemModel(64, 33, dlg)
        for y in range(64):
            n = y%2==0 and 15 or 16
            center = y/2+15        
            for i in range(16):
                x=center-i
                if(x < 0 or x >= 64):
                    continue
                item = QStandardItem("m%02d"%(15-i))
                model.setItem(y, x%32,item)
            for i in range(n):#0~14 or 0~15
                x = center+1+i
                if x < 0 or x >=64:
                    continue
                item = QStandardItem("n%02d"%(n-1-i))
                model.setItem(y, x%32,item)
        return model
    
    def getRecMov(self, dlg):
        model = QStandardItemModel(64, 65, dlg)
        for y in range(64):
            n = y%2==0 and 15 or 16
            center = y/2+15        
            for i in range(16):
                x=center-i
                if(x < 0 or x >= 64):
                    continue
                item = QStandardItem("m%02d"%(15-i))
                model.setItem(y, x,item)
            for i in range(n):#0~14 or 0~15
                x = center+1+i
                if x < 0 or x >=64:
                    continue
                item = QStandardItem("n%02d"%(n-1-i))
                model.setItem(y, x,item)
        return model
    
    def getRec(self, dlg):
        model = QStandardItemModel(64, 65, dlg)
        for y in range(64):
            n = y%2==0 and 15 or 16
            center = y/2        
            for i in range(16):
                x=center-i
                if(x < 0 or x >= 64):
                    continue
                item = QStandardItem("m%02d"%(15-i))
                model.setItem(y, x,item)
            for i in range(n):#0~14 or 0~15
                x = center+1+i
                if x < 0 or x >=64:
                    continue
                item = QStandardItem("n%02d"%(n-1-i))
                model.setItem(y, x,item)
        return model