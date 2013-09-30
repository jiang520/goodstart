#encoding=gb2312
'''
Created on 2013-9-29

@author: Administrator
'''
from dbActicleIMS import dbActicleIMS
class ArticleType:
    def __init__(self):
        self.id = 0
        self.parentid = 0
        self.text = u''
    
    def __str__(self):
        return "[%d,%s,%d]"%(self.id, self.text, self.parentid)   
      
class dbArticleType:
    def getType1(self):
        sql = '''SELECT "id", "name", "parentid" from tbType where parentid=0''';
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        liType = []
        for item in  cusor.fetchall():
            a = ArticleType()
            a.id    = item[0]
            a.text  = item[1]
            a.parentid = item[2]           
            liType.append(a)
        return liType
    
    def getType2(self, parentid):
        sql = '''SELECT "id", "name", "parentid" from tbType where parentid=%d'''%parentid
        #print sql    
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        liType = []
        for item in  cusor.fetchall():
            a = ArticleType()
            a.id    = item[0]
            a.text  = item[1]
            a.parentid = item[2]
            #print a.text
            liType.append(a)
        return liType
        
    def insert(self, articletype):        
        if articletype.text == None or len(articletype.text) <1:
            return False
        sql = '''insert into tbType("name", "parentid") values('%s',%d)'''%(articletype.text, articletype.parentid);
        print sql
        try:
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
        except:
            return False
        finally:
            return True
    
def gettype1():
    for a in dbArticleType().getType1():
        print a
        for b in dbArticleType().getType2( a.id):
            print '-',b
        
if __name__ == '__main__':
    gettype1()
                