'''
Created on 2013-9-27

@author: Administrator
'''
from dbActicleIMS import *
class Client:
    id = 0
    name = ''
    address = ''
    phone = ''
    mobile = ''
    boss = ''
    type = ''
    detail = ''

class dbClient():
    def getAll(self):
        sql = '''SELECT "id", "name", "address", "phone", "mobile", "boss", "clienttype", "detail" FROM "tbClient"'''
        con = dbActicleIMS.getInstance().getConnection()
        cursor  = con.execute(sql)
        if cursor == None:
            return []
        list = []
        for item in cursor.fetchall():
            a = Client()
            a.id        = item[0]
            a.name      = item[1]
            a.address   = item[2]
            a.phone     = item[3]
            a.mobile    = item[4]
            a.boss      = item[5]
            a.type      = item[6]
            a.detail    = item[7]
            list.append(a)
        return list
        
    def getById(self, clientid):
        sql = '''SELECT "id", "name", "address", "phone", "mobile", "boss", "clienttype", "detail"
                FROM "tbClient" where id = %d'''%clientid
        con = dbActicleIMS.getInstance().getConnection()
        cursor  = con.execute(sql)
        if cursor == None:  return None
        item = cursor.fetchone()
        if item == None: return None
        a = Client()
        a.id        = item[0]
        a.name      = item[1]
        a.address   = item[2]
        a.phone     = item[3]
        a.mobile    = item[4]
        a.boss      = item[5]
        a.type      = item[6]
        a.detail    = item[7]
        return a
        
    def insert(self, client):
        sql = '''insert into tbClient("name", "address", "phone", "mobile", "boss", "clienttype", "detail")
                values('%s','%s','%s','%s','%s','%s','%s')'''%(                                                 
                                                 client.name,
                                                 client.address,
                                                 client.phone,
                                                 client.mobile,
                                                 client.boss,
                                                 client.type,
                                                 client.detail)
        print sql
        try:
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return False
        
    ''' modify client data by id and new client data'''
    def modify(self, id, client):
        sql = '''update  tbClient set name='%s', 
                                        address='%s', 
                                        phone='%s', 
                                        mobile='%s', 
                                        boss='%s', 
                                        clienttype='%s', 
                                        detail='%s'
                                        where id = %d'''%(
                                                 client.name,
                                                 client.address,
                                                 client.phone,
                                                 client.mobile,
                                                 client.boss,
                                                 client.type,
                                                 client.detail,
                                                 id,
                                                 )
        print sql
        try:
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return False
        
    def delete(self, clientid):
        sql = ''' delete from tbClient where id = %d'''%clientid
        print sql
        try:
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return False

if __name__=="__main__":
    dbc = dbClient()
    c = Client()
    c.id = 33
    c.address = 'addr3'
    c.boss = 'fosoe'
    c.name = 'company'
    c.detail = 'dooifidetail'
    
    print 'before insert len = ',len(dbc.getAll())        
    dbc.insert(c)
    print 'after insert len = ', len(dbc.getAll())