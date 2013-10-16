#encoding=gb2312
'''
Created on 2013-9-29

@author: Administrator
'''
from dbActicleIMS import dbActicleIMS
from ims.model.dbClient import *
from ims.model.dbArticle import dbArticle


class InOutRecord:
    def __init__(self):
        self.id = 0
        self.detail = u''
        self.price = 0
        self.count = 1
        self.time = ''
        self.count = 1
        self.price = 1.0
        self.number = 0
        self.clientid = 0
        self.articleid = 0
        self.__articleInfo = None
        self.__clientInfo  = None
    #延迟查询
    def getArticleInfo(self):
        if self.__articleInfo is None:
            self.__articleInfo = dbArticle().getById(self.articleid)
        return  self.__articleInfo
    #延迟查询
    def getClientInfo(self):
        if self.__clientInfo is None:
            self.__clientInfo = dbClient().getById(self.clientid)
        return  self.__clientInfo

    def __str__(self):
        return '<InOurRecord object(id=%d)>'%self.id
        
class dbInOutRecord:
    def getRecord(self, strNumber=None,
                  strArticleModel=None,
                  strClientName=None,
                  dateInterval=None,
                  articleid = None,
                  indexInterval=(0,100)):
        if indexInterval == None: return
        strFilterList = []
        if None != strNumber:
            strFilterList.append(''' and recordid like '%%%s%%' '''%strNumber)
        if None != dateInterval and dateInterval[0] != '' and dateInterval[1] != '':
            strFilterList.append(''' and time >= '%s' and time <= '%s' '''%(dateInterval[0], dateInterval[1]))
        if None != strArticleModel:
            strFilterList.append( ''' and model like '%%%s%%' '''%strArticleModel )
        if None != strClientName:
            strFilterList.append( '''and tbClient.name like '%%%s%%' '''%strClientName)
        if None != articleid:
            strFilterList.append('''and articleid=%d'''%articleid)
        sql = '''SELECT tbInOutRecord.id, "articleid", "time", "count", "price", "recordid", tbInOutRecord.detail, "clientid"
                    FROM tbInOutRecord left join tbArticle on tbInOutRecord.articleid=tbArticle.id,
                                                 tbClient on tbClient.id = tbInOutRecord.clientid
                    where 1=1 %s
                    limit %d,%d'''%(' '.join(strFilterList), indexInterval[0], indexInterval[1])
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        listRes = []
        for item in  cursor.fetchall():
            record          = InOutRecord()
            record.id       = int(item[0])
            record.articleid= int(item[1])
            record.time     = item[2]
            record.count    = float(item[3])
            record.price    = float(item[4])
            record.number   = item[5]
            record.detail   = item[6]
            record.clientid = item[7]
            listRes.append(record)
        return listRes

    #获取物品的所有
    def getSpecArticlePriceList(self,article_id):
        sql = '''SELECT distinct price FROM tbInOutRecord where articleid=%d order by time desc '''%article_id
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        priceList = []
        for item in  cursor.fetchall():
            priceList.append(item[0])
        return  priceList

    #获取物品最近单价
    def getLastUnitPrice(self, article_id):
        sql = '''SELECT price From tbInoutRecord where articleid=%d order by time desc limit 1,1'''%article_id
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        if cursor is None: return  None
        item = cursor.fetchone()
        if item is None: return  None
        return  item[0]

    def getById(self, recordid):
        sql = '''SELECT id, articleid, time, count, price, recordid, clientid, detail  FROM tbInOutRecord where id=%d '''%recordid
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        item = cursor.fetchone()
        record          = InOutRecord()
        record.id       = int(item[0])
        record.articleid=int(item[1])
        record.time     = item[2]
        record.count    = float(item[3])
        record.price    = float(item[4])
        record.number   = item[5]
        record.clientid = int(item[6])
        record.detail   = item[7]
        return record
        
    def addRecords(self, recordlist):
        for record in recordlist:
            sql = '''insert into tbInOutRecord (
                        articleid,
                        time,
                        count,
                        price,
                        recordid,
                        clientid,
                        detail) values(
                        %d,'%s',%f,%f,'%s',%d,'%s')'''%(
                          record.articleid,
                          record.time,
                        record.count, 
                        record.price,
                        record.number,
                        record.clientid,
                        record.detail);
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
        con.commit()
        return True
    
    def add(self, record):
        sql = '''insert into tbInOutRecord (
                        articleid,
                        time,
                        count,
                        price,
                        recordid,
                        clientid,
                        detail) values(
                        %d,'%s',%f,%f,'%s',%d,'%s')'''%(
                          record.articleid,
                          record.time,
                        record.count, 
                        record.price,
                        record.number,
                        record.clientid,
                        record.detail);
        #print sql
        con = dbActicleIMS.getInstance().getConnection()
        con.execute(sql)
        con.commit()                
        
    def modify(self,record):
        sql = '''update tbInOutRecord set 
                        articleid=%d,
                        time='%s',
                        count=%d,
                        price=%f,
                        recordid='%s',
                        clientid=%d,
                        detail='%s' where  id=%d''' % (
                        record.articleid,
                        record.time,
                        record.count,
                        record.price,
                        record.number,
                        record.clientid,
                        record.detail,
                        record.id);
        print sql
        try:
            con = dbActicleIMS.getInstance().getConnection()
            cursor = con.execute(sql)
            #print cursor
            #print cursor.fetchall()
            con.commit()
            return True
        except Exception, e:
            print e
            return  False
                        
    def delete(self, inoutid):       
        try:
            sql = '''delete  from tbInoutRecord where id = %d'''%(inoutid)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)          
            con.commit()
            return  True
        except Exception,e:
            print e
            return False
    
if __name__ == '__main__':
    record = InOutRecord()
    record.articleid = 3
    record.price = 1.0
    record.count = 1
    record.detail= 'detai33l3'
    record.time = '20120304'
    record.id = 1
    print dbInOutRecord().add(record)
    #print dbInOutRecord().modify(record)
    print dbInOutRecord().getRecord()
