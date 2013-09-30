'''
Created on 2013-9-29

@author: Administrator
'''
from dbActicleIMS import dbActicleIMS

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
        self.model = u''
    def __str__(self):
        return '<InOurRecord object(id=%d)>'%self.id
        
class dbInOutRecord:
    def getRecord(self, start=0,end=50):
        sql = '''SELECT "id", "articleid", "time", "count", "price", "recordid", "clientid", "detail" 
                    FROM "tbInOutRecord" limit %d,%d'''%(start,end)
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        listRes = []
        for item in  cursor.fetchall():
            record          = InOutRecord()
            record.id       = int(item[0])
            record.articleid=int(item[1])
            record.time     = item[2]
            record.count    = float(item[3])
            record.price    = float(item[4])
            record.number   = item[5]
            record.clientid = int(item[6])
            record.detail   = item[7]
            listRes.append(record)
        return listRes
    
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
        #print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        #print cursor
        #print cursor.fetchall() 
        con.commit()
                        
    def delete(self, inoutid):       
        sql = '''delete  from tbClient where id = %d'''%(inoutid)
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        print cursor.fetchall()              
        con.commit()
    
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
