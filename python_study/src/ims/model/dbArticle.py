#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
from dbActicleIMS import *
class Article:
    def __init__(self):
        self.id         = 0#系统编号
        self.typeid     = 0#类型信息
        self.model      = u''#型号
        self.packaging  = u''#封装
        self.pingpai    = u''#品牌
        self.function   = u''#功能说明
        self.detail     = u''#详细信息
        self.unit       = u'个'#物品单位

class ArticleRemainInfo:
    def __init__(self):
        self.article     = None #物品信息
        self.remainCount = 0.0  #剩余数量信息
    
                
class dbArticle:
    """
    物品信息表查询类
    """

    '''根据物品id查找物品信息'''
    def getById(self, articleid):
        sql = '''SELECT id, typeid, model, packaging, pingpai, function, detail,unit FROM tbArticle where id=%d'''%articleid
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        item = cursor.fetchone()
        #print item
        if item == None: return None
        a = Article()
        a.id        = int(item[0])
        a.typeid    = item[1]
        a.model     = item[2]
        a.packaging = item[3]
        a.pingpai   = item[4]
        a.function  = item[5]
        a.detail    = item[6]
        a.unit      = item[7]
        return a


    '''根据物品类型和型号(字符串)查找物品信息'''
    def getByTypeAndModel(self, typeid, model):
        sql = '''SELECT "id", "typeid", "model", "packaging", 
            "pingpai", "function", "detail", unit FROM "tbArticle"  where typeid=%d and model='%s' '''%(typeid, model);
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        item = cursor.fetchone()
        if item == None:
            return None
        #print item
        a = Article()
        a.id        = int(item[0])
        a.typeid    = item[1]
        a.model     = item[2]
        a.packaging = item[3]
        a.pingpai   = item[4]
        a.function  = item[5]
        a.detail    = item[6]
        a.unit      = item[7]
        return a

    '''查找所有物品信息'''
    def getAll(self):
        sql = '''SELECT "id", "typeid", "model", "packaging", 
            "pingpai", "function", "detail","unit" FROM "tbArticle" ''';
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        list = []
        for item in  cusor.fetchall():
            a = Article()
            a.id        = int(item[0])
            a.typeid    = item[1]
            a.model     = item[2]
            a.packaging = item[3]
            a.pingpain  = item[4]
            a.fuction   = item[5]
            a.detail    = item[6]
            a.unit      = item[7]
            list.append(a)
        return list

    '''查找指定具体类型的物品列表数据'''
    def getArticlesByTypeId(self, typeid):
        sql = '''SELECT "id", "model", "packaging","pingpai", "function", "detail" ,"unit" FROM "tbArticle" where typeid=%d'''%typeid;
        con = dbActicleIMS.getInstance().getConnection()
        cusor = con.execute(sql)
        list = []
        for item in  cusor.fetchall():
            a = Article()            
            a.typeid    = typeid
            a.id        = int(item[0])
            a.model     = item[1]
            a.packaging = item[2]
            a.pingpain  = item[3]
            a.fuction   = item[4]
            a.detail    = item[5]
            a.unit      = itme[6]
            list.append(a)
        return list
        
    '''添加物品信息,id自动产生的,不需要有输入'''
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
                                            "detail",
                                            "unit")
                values(%d,'%s','%s','%s','%s','%s','%s')'''%(article.typeid,
                                                      article.model,
                                                      article.packaging,
                                                      article.pingpai,
                                                      article.function,
                                                      article.detail,
                                                      article.unit)
        print sql        
        try:
            con = dbActicleIMS.getInstance().getConnection()           
            con.execute(sql)   
            con.commit()     
            return True
        except:
            print 'sql failed :%s'%sql 
            return False

    '''修改物品信息,id号不变'''
    def modify(self, article):
        try:
            con = dbActicleIMS.getInstance().getConnection()
            sql = '''update tbArticle set   typeid=%d,
                                            model='%s', 
                                            packaging='%s',
                                            pingpai='%s', 
                                            function='%s',
                                            detail='%s'
                                             unit='%s' where id = %d '''%(
                                              article.typeid,
                                              article.model,
                                              article.packaging,
                                              article.pingpai,
                                              article.function,
                                              article.detail,
                                              article.unit,
                                              article.id)
            print sql
            con.execute(sql) 
            con.commit()
            return True
        except:
            return False       
        
    '''根据物品id移除物品信息'''
    def delete(self, id):
        try:
            sql = '''delete from tbArticle where id=%d'''%(id)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except:
            return False
        
    '''查找所有库存'''
    def getAllArticleRemainList(self):
        sql = '''select tbArticle.id, sum(tbInoutRecord.count)
                from tbArticle left join tbInoutRecord                
                on tbInoutRecord.articleid=tbArticle.id                 
                group by tbArticle.id''' 
        cursor = dbActicleIMS.getInstance().getConnection().execute(sql)
        reslist = []
        for item in  cursor.fetchall():    
            remainInfo = ArticleRemainInfo()
            remainInfo.article      = self.getById(int(item[0]))            
            remainInfo.remainCount  = item[1] != None and float(item[1]) or 0
            reslist.append(remainInfo)
        return reslist
    
    '''查找指定物品的库存'''        
    def getSpecArticleRemainList(self, articleid):
        sql = '''select tbArticle.id,sum(tbInoutRecord.count)
                 from tbInoutRecord,tbArticle
                  where tbInoutRecord.articleid=tbArticle.id and tbArticle.id=%d 
                  group by tbInoutRecord.articleid'''%articleid
        print sql
        cursor = dbActicleIMS.getInstance().getConnection().execute(sql)
        reslist = []
        for item in  cursor.fetchall():    
            remainInfo = ArticleRemainInfo()
            remainInfo.article      = self.getById(int(item[0]))            
            remainInfo.remainCount  = item[1] != None and float(item[1]) or 0
            reslist.append(remainInfo)
        return reslist
        
        
if __name__=="__main__":
    a = Article()
    a.type = 33
    a.model = '3402424'
    
    dba = dbArticle()
    print dba.getById(28)