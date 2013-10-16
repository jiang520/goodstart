#encoding=gb2312
__author__ = 'jiang'

from dbActicleIMS import *
import base64
g_current_user = None
class SysUser:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.id = 0
        self.usertype = u'�ο�'

    #�����޸�����
    def is_enable_write_all(self):
        #print 'is admin',self.usertype == u'����Ա'
        return self.usertype == u'����Ա'

    def is_enable_read_all(self):
        return  True

class dbSysUser:
    """
    �û��ʻ����������,
    �ʺŵ������ַ�����д�����ݿ�ǰ����,�ʻ���������
    """
    def __init__(self):
        pass

    #У���û��ʻ�,����,������ܹ��̲�����,�Ƚ����ݿ��е�����
    def isValidUser(self, userinfo):
        print u'check invalid,%s,%s',userinfo.username, userinfo.password
        if len(userinfo.username) > 50:return  False
        if type(userinfo.password) != type(u'string'):
            print 'invalid userinfo.password type',type(userinfo.password)
            return
        strEncodePass = base64.encodestring(u'%s'%userinfo.password)
        strEncodePass = strEncodePass.strip()
        print "str Encode pass= '%s'"%strEncodePass, type(userinfo.password)
        if len(strEncodePass) > 100: return False
        sql = ''' select * from tbSysUser where username='%s'
                                and password='%s' '''%(userinfo.username, strEncodePass)
        try:
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            cursor = con.execute(sql)
            #У�����Ƿ�Ϊһ��
            bValid =  len(cursor.fetchall())==1
            return bValid
        except Exception, e:
            print e
            return  False

    #����û���Ϣ
    def addUser(self, userinfo):
        if len(userinfo.username) > 50:return  False
        if len(userinfo.usertype) <= 0: return  False
        strEncodePass = base64.encodestring(userinfo.password)
        strEncodePass = strEncodePass.strip()
        if len(strEncodePass) > 100: return False
        sql = ''' insert into tbSysUser (username, password,usertype)
                        values('%s','%s','%s')'''%(userinfo.username, strEncodePass, userinfo.usertype)
        print sql
        try:
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return  False

    def modifyUser(self, oldusername, userinfo):
        if len(oldusername) < 1: return  False
        if len(userinfo.username) > 50:return  False
        if len(userinfo.usertype) <= 0: return  False
        strEncodePass = base64.encodestring(userinfo.password)
        strEncodePass = strEncodePass.strip()
        if len(strEncodePass) > 100: return False
        sql = ''' update tbSysUser set username='%s',
                                       password='%s',
                                       usertype='%s'
                                       where username='%s' '''%(userinfo.username,
                                                        strEncodePass,
                                                        userinfo.usertype,
                                                        oldusername)
        print sql
        try:
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return  False

    #�޸��û���Ϣ
    def modifyPassword(self, username, password):
        password = password.strip()
        if len(password) < 4: return
        try:
            strEncodePass = base64.encodestring(password)
            strEncodePass = strEncodePass.strip()
            if len(username) > 50: return  False
            if len(strEncodePass)    > 100: return  False
            sql = ''' update tbSysUser set password='%s'
                                        where username='%s' '''%(strEncodePass, username)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return  False

    def deleteUser(self, username):
         try:
            sql = ''' delete from tbSysUser where username='%s' '''%(username)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
         except Exception, e:
            print e
            return  False


    def get_all_users(self):
        sql = ''' select id,username, usertype from tbSysUser '''
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        if cursor is None: return
        usrlist = []
        for item in cursor.fetchall():
            user = SysUser()
            user.id = int(item[0])
            user.username = item[1]
            user.usertype = item[2]
            usrlist.append(user)
        return  usrlist
    def get_user_by_username(self,username):
        sql = ''' select id,username, usertype from tbSysUser where username='%s' '''%username
        print sql
        con = dbActicleIMS.getInstance().getConnection()
        cursor = con.execute(sql)
        if cursor is None: return
        item = cursor.fetchone()
        if item == None: return
        user = SysUser()
        user.id = int(item[0])
        user.username = item[1]
        user.usertype = item[2]
        return  user



 #������
if __name__ == '__main__':
    user = SysUser()
    user.username = 'fuckoff3'
    user.password = 'fosei'

    db = dbSysUser()
    print db.addUser(user)

