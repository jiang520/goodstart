#encoding=gb2312
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

    '''创建数据库'''
    def createDataBase(self):
        import sys
        import os
        self.__dbFilePath = os.getcwd()+"\\ims_acticle.db3"
        print '======open data base at path:%s'%self.__dbFilePath
        self.con = sqlite3.connect(self.__dbFilePath)
        sql_cr_tbtyp = ''' CREATE TABLE if not exists tbType
                        (
                        id integer primary key autoincrement,
                        name varchar(100),
                        parentid uint
                        );'''
        sql_cr_tbInOut = '''CREATE TABLE if not exists tbInOutRecord 
                        (
                        id integer primary key autoincrement,
                        articleid integer not null,
                        time datetime not null,                    
                        count float not null,
                        price float,
                        recordid uint not null,
                        clientid uint,
                        detail varchar(100)
                        );
                        '''
        sql_cr_tbclient = '''CREATE TABLE if not exists tbClient
                            (
                            id integer primary key autoincrement,
                            name varchar(100),
                            address varchar(200),
                            phone varchar(50),
                            mobile varchar(50),
                            boss varchar(50),
                            clienttype varchar(50),
                            detail varchar(100)
                            );'''
        sql_cr_tbArticle = '''CREATE TABLE if not exists tbArticle(
                            id integer primary key autoincrement,
                            typeid    uint,
                            model     varchar(50),
                            packaging varchar(100),
                            pingpai   varchar(100),
                            function  varchar(100),
                            detail    varchar(200)
                            );'''
        self.con.execute(sql_cr_tbArticle)
        self.con.execute(sql_cr_tbclient)
        self.con.execute(sql_cr_tbclient)
        self.con.execute(sql_cr_tbtyp)
        self.con.execute(sql_cr_tbInOut)
        
    '''获取数据库连接'''
    def getConnection(self):
        return self.con

    def getDatabaseFilePath(self):
        return  self.__dbFilePath
    
if __name__=="__main__":
    a = dbActicleIMS.getInstance()
    b = dbActicleIMS.getInstance()
    b.a = 3
    print b.a
    print a.a
    print id(a)
    print id(b)
    print a.getAllArticleRemainList()
    print a.getSpecArticleRemainList(4)