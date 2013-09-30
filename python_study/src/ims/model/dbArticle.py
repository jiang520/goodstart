#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from dbActicleIMS import *
class Article:
    def __init__(self):
        self.id = 0
        self.typeid=u''
        self.model=u''
        self.packaging=u''
        self.pingpai = u''
        self.function=u''
        self.detail = u''

                
class dbArticle:
    
    def getAll(self):
        sql = '''SELECT "id", "typeid", "model", "packaging", 
            "pingpai", "function", "detail" FROM "tbArticle" ''';
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        list = []
        for item in  cusor.fetchall():
            a = Article()
            a.id = int(item[0])
            a.typeid = item[1]
            a.model = item[2]
            a.packaging = item[3]
            a.pingpain = item[4]
            a.fuction = item[5]
            a.detail = item[6]            
            list.append(a)
        return list
    def getArticlesByTypeId(self, typeid):
        sql = '''SELECT "id", "model", "packaging","pingpai", "function", "detail" FROM "tbArticle" where typeid=%d'''%typeid;
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        list = []
        for item in  cusor.fetchall():
            a = Article()            
            a.typeid = typeid
            a.id = int(item[0])
            a.model = item[1]
            a.packaging = item[2]
            a.pingpain = item[3]
            a.fuction = item[4]
            a.detail = item[5]            
            list.append(a)
        return list
        
        
    def add(self, article):
        if article.typeid <= 0:
            return False
        if article.model == '':
            return False
        #print article.detail
        sql = '''insert into tbArticle("typeid", 
                                            "model", 
                                            "packaging",
                                            "pingpai", 
                                            "function", 
                                            "detail") 
                values(%d,'%s','%s','%s','%s','%s')'''%(article.typeid, 
                                                      article.model,
                                                      article.packaging,
                                                      article.pingpai,
                                                      article.function,
                                                      article.detail)
        print sql        
        try:
            con = dbActicleIMS.getInstance().getConnection()           
            con.execute(sql)   
            con.commit()     
            return True
        except:
            print 'sql failed :%s'%sql 
            return False
        
    def modify(self, article):
        con = dbActicleIMS.getInstance().getConnection()
        sql = '''update tbArticle set   "model=%s", 
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
        try:
            con = dbActicleIMS.getInstance().getConnection()
            con.execute('''delete from tbActicle where id=%d'''%(id))
            con.commit
            return True
        except:
            return False
        
    '''查找所有库存'''
    def getAllArticleRemainList(self):
        sql = '''select tbArticle.id,tbArticle.model, sum(tbInoutRecord.count),
                tbArticle.packaging,tbArticle.pingpai,tbArticle.detail
                 from tbArticle left join tbInoutRecord                
                 on tbInoutRecord.articleid=tbArticle.id                 
                  group by tbArticle.id''' 
        cursor = dbActicleIMS.getInstance().getConnection().execute(sql)
        return cursor.fetchall()
    '''查找指定物品的库存'''        
    def getSpecArticleRemainList(self, articleid):
        sql = '''select tbArticle.id,tbArticle.model,sum(tbInoutRecord.count),
                tbArticle.packaging,tbArticle.pingpai,tbArticle.detail
                 from tbInoutRecord,tbArticle
                  where tbInoutRecord.articleid=tbArticle.id and tbArticle.id=%d 
                  group by tbInoutRecord.articleid'''%articleid
        #print sql 
        cursor = dbActicleIMS.getInstance().getConnection().execute(sql)
        return cursor.fetchall()    
if __name__=="__main__":
    a = Article()
    a.type = 33
    a.model = '3402424'
    
    dba = dbArticle()
    dba.add(a)
    #for a in  dba.getAll():
    #    print a