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

    #可以修改内容
    def is_enable_write_all(self):
        if usertype == u'writer':
            return  True
        return  False
    def is_enable_read_all(self):
        return  True

class dbSysUser:
    """
    用户帐户密码管理类,
    帐号的密码字符串在写入数据库前加密,帐户名不加密
    """
    def __init__(self):
        pass

    #校样用户帐户,密码,密码加密过程不可逆,比较数据库中的密码
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
            #校验结果是否为一条
            bValid =  len(cursor.fetchall())==1
            return bValid
        except Exception, e:
            print e
            return  False

    #添加用户信息
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

    #修改用户信息
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

 #主函数
if __name__ == '__main__':
    user = SysUser()
    user.username = 'fuckoff3'
    user.password = 'fosei'

    db = dbSysUser()
    print db.addUser(user)

