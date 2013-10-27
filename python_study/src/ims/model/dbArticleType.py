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
    """
    物品类型管理信息
    """
    def getArticleTypeInfo(self, type_id):
        sql = '''select tbType.name, tbType2.name
                    from tbType left join tbType as tbType2 on tbType.parentid=tbType2.id
                    where tbType.id=%d'''%type_id
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        if cursor is None: return  None
        res = cursor.fetchone()
        if res is None: return  None
        return  res

    #根据类型名称查找类型信息
    def getArticleTypeInfoByTypeName(self, name):
        sql = '''select id,name,parentid from tbType where name='%s' '''%name
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        if cursor is None: return  None
        res = cursor.fetchone()
        if res is None: return  None
        typeinfo = ArticleType()
        typeinfo.id = int(res[0])
        typeinfo.text = res[1]
        typeinfo.parentid=int(res[2])
        return  typeinfo

    #'''查找所有大类信息列表'''
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

    #'''查找指定大类下的二级类型信息'''
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
    #'''修改类型名称'''
    def rename(self, typeid, newname):
        if newname==None or newname == '': return False
        con = dbActicleIMS.getInstance().getConnection()
        if not con:
            return False
        '''========执行更名操作'''
        sql = '''update tbType set name='%s' where id=%d '''%(newname,typeid);
        print sql
        try:
            con.execute(sql)
            con.commit()
        except:
            return False
        finally:
            return True

    '''新增类型信息'''
    def insert(self, articletype):
        con = dbActicleIMS.getInstance().getConnection()  
        if con == None: return False              
        if articletype.text == None or len(articletype.text) <1:
            return False
        if articletype.parentid < 0:
            print 'parent id cant be < 0' 
            return False
        '''====== 检查父类id是否存在'''
        if articletype.parentid != 0:
            sql = '''select * from tbType where id=%d'''%articletype.parentid
            cursor = con.execute(sql)
            if len(cursor.fetchall()) <= 0: 
                print 'invalid parent type id (un exist parent type'
                return False
        
        '''======检查是否存在同名,同级的id'''
        sql = '''select * from tbType where parentid=%d and name='%s' '''%(articletype.parentid,articletype.text)
        cursor = con.execute(sql)
        if len(cursor.fetchall()) > 0: 
            print 'invalid parent type id (un exist parent type'
            return False
        '''======执行添加操作'''
        sql = '''insert into tbType("name", "parentid") values('%s',%d)'''%(articletype.text, articletype.parentid);
        print sql
        try:
            con.execute(sql)
            con.commit()
        except:
            return False
        finally:
            return True

    '''移除类型信息'''
    def delete(self, typeid):
        sql = '''delete from tbType where id=%d'''%typeid;
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
                