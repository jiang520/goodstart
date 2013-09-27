'''
Created on 2013-9-27

@author: Administrator
'''
from dbActicleIMS import *
class Article:
    def __init__(self):
        self.id = 0
        self.type=u''
        self.model=u''
        self.packaging=u''
        self.pingpai = u''
        self.function=u''
        self.detail = u''
        
        
class ArticleDatabase:
    
    def getAll(self):
        sql = '''SELECT "id", "typeid", "model", "packaging", 
            "pingpai", "function", "detail" FROM "tbActicle" ''';
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        list = []
        for item in  cusor.fetchall():
            a = Article()
            a.id = int(item[0])
            a.type = item[1]
            a.model = item[2]
            a.packaging = item[3]
            a.pingpain = item[4]
            a.fuction = item[5]
            a.detail = item[6]            
            list.append(a)
        return list
        
    def add(self, article):
        con = dbActicleIMS.getInstance().getConnection()
        sql = '''insert into tbActicle("typeid", 
                                        "model", 
                                        "packaging",
                                        "pingpai", 
                                        "function", 
                                        "detail") 
            values(%d,'%s','%s','%s','%s','%s')'''%(article.type, 
                                          article.model,
                                          article.packaging,
                                          article.pingpai,
                                          article.function,
                                          article.detail)
        print sql
        con.execute(sql)        
    
    def modify(self, article):
        con = dbActicleIMS.getInstance().getConnection()
        sql = '''update tbActicle set   "model=%s", 
                                        "packaging=%s",
                                        "pingpai=%s", 
                                        "function=%s", 
                                        "detail=%s" where typeid = %d '''%(
                                          article.model,
                                          article.packaging,
                                          article.pingpai,
                                          article.function,
                                          article.detail,
                                          article.type)
        print sql
        con.execute(sql) 
        con.commit()       
    
    def delete(self, id):
        con = dbActicleIMS.getInstance().getConnection()
        con.execute('''delete from tbActicle where id=%d'''%(id))
        
    
if __name__=="__main__":
    a = Article()
    a.type = 33
    a.model = '3402424'
    
    dba = ArticleDatabase()
    dba.add(a)
    #for a in  dba.getAll():
    #    print a