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
        self.usertype = u'reader'

    #�����޸�����
    def is_enable_write_all(self):
        if usertype == u'writer':
            return  True
        return  False
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
        strEncodePass = base64.encodestring(userinfo.password)
        strEncodePass = strEncodePass.strip()
        if len(strEncodePass) > 100: return False
        sql = ''' insert into tbSysUser (username, password)
                        values('%s','%s')'''%(userinfo.username, strEncodePass)
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
    def modifyUser(self, userinfo):
        try:
            strEncodePass = base64.encodestring(userinfo.password)
            strEncodePass = strEncodePass.strip()
            if len(userinfo.username > 50): return  False
            if len(strEncodePass > 100): return  False
            sql = ''' update tbSysUser set username='%s',
                                        password='%s'
                                        where id=%d '''%(userinfo.username,
                                                         strEncodePass,
                                                         userinfo.id)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
        except Exception, e:
            print e
            return  False


    def deleteUser(self, userid):
         try:
            sql = ''' delete from tbSysUser where id=%d '''%(userid)
            print sql
            con = dbActicleIMS.getInstance().getConnection()
            con.execute(sql)
            con.commit()
            return True
         except Exception, e:
            print e
            return  False

 #������
if __name__ == '__main__':
    user = SysUser()
    user.username = 'fuckoff3'
    user.password = 'fosei'

    db = dbSysUser()
    print db.addUser(user)

