'''
Created on 2013-9-27

@author: Administrator
'''
import sqlite3
class dbActicleIMS(object):
    '''
    singe instance of database
    
    '''
    __instance = None        
    def __init__(self):
        "disable the __init__ method"
    
    @staticmethod
    def getInstance():
        if not dbActicleIMS.__instance:
            dbActicleIMS.__instance = object.__new__(dbActicleIMS)
            object.__init__(dbActicleIMS.__instance)
            dbActicleIMS.__instance.createDataBase()
        return dbActicleIMS.__instance
    
    def createDataBase(self):
        self.con = sqlite3.connect("f:\\ims_acticle.db3")
        #print self.con
        cusor =  self.con.execute('select * from tbActicle')
        #print cusor
        #print cusor.fetchall()
        #print cusor.count()
    def getConnection(self):
        return self.con
        
        
if __name__=="__main__":
    a = dbActicleIMS.getInstance()
    b = dbActicleIMS.getInstance()
    b.a = 3
    print b.a
    print a.a
    print id(a)
    print id(b)
    print a.getConnection()