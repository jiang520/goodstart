#encoding=gb2312
'''
Created on 2013-9-27

@author: Administrator
'''
import sys
import os
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

    '''创建数据库'''
    def createDataBase(self):

        self.__dbFilePath = u"%s\\ims_acticle.db3"%os.getcwdu()
        print self.__dbFilePath
        print '======open data base at path:%s'%self.__dbFilePath
        self.con = sqlite3.connect(self.__dbFilePath)
        sql_cr_tbtyp = ''' CREATE TABLE if not exists tbType  ( id integer primary key autoincrement,
                                                name varchar(100),
                                                parentid uint
                        );'''
        sql_cr_tbInOut = '''CREATE TABLE if not exists tbInOutRecord ( id integer primary key autoincrement,
                                                    articleid integer not null,
                                                    time datetime not null,
                                                    count float not null,
                                                    price float,
                                                    recordid uint not null,
                                                    clientid uint,
                                                    detail varchar(100)
                                                    );
                                                    '''
        sql_cr_tbclient = '''CREATE TABLE if not exists tbClient (
                            id integer primary key autoincrement,
                            name varchar(100),
                            address varchar(200),
                            phone varchar(50),
                            mobile varchar(50),
                            boss varchar(50),
                            clienttype varchar(50),
                            detail varchar(100)
                            );'''
        sql_cr_tbArticle = '''CREATE TABLE if not exists tbArticle( id integer primary key autoincrement,
                                                    typeid    uint,
                                                    model     varchar(50),
                                                    packaging varchar(100),
                                                    pingpai   varchar(100),
                                                    function  varchar(100),
                                                    detail    varchar(200),
                                                    unit varchar(20)
                                                     );'''
        sql_cr_tbSysUser = '''CREATE TABLE if not exists tbSysUser( id integer  primary key autoincrement,
                                                    username varchar(50) not null unique,
                                                    password varchar(100) not null,
                                                    usertype varchar(50) not null);'''
        import  base64
        passd = u'5950ut'
        pass_encoded = base64.encodestring(passd)
        pass_encoded = pass_encoded.strip()
        sql_insert_default_user = ''' insert into tbSysUser (username, password,usertype) values('%s',"%s",'admin') '''%('admin', pass_encoded)
        self.con.execute(sql_cr_tbArticle)
        self.con.execute(sql_cr_tbclient)
        self.con.execute(sql_cr_tbclient)
        self.con.execute(sql_cr_tbtyp)
        self.con.execute(sql_cr_tbInOut)
        self.con.execute(sql_cr_tbSysUser)
        try:
            self.con.execute(sql_insert_default_user)
        except Exception, e:
            print 'Create default sysuser failed:', e
        self.con.commit()

        
    '''获取数据库连接'''
    def getConnection(self):
        return self.con

    def getDatabaseFilePath(self):
        return  self.__dbFilePath
