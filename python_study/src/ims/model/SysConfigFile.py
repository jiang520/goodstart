#encoding=gb2312
__author__ = 'Administrator'
import ConfigParser
class SysConfigFile:
    def __init__(self):
        self.__filepath = None
        self.__config=None

    def setFilePath(self, path):
        self.__filepath = path
        self.__config = ConfigParser.ConfigParser()
        print '==========init sys config with path:%s'%path
        self.__config.read(path)

    def save(self):
        self.__config.write(open(self.__filepath,'w'))

    #添加客户类型
    def addClientTypes(self, newtype):
        if type(newtype)==type(u''):
            str_newtype = newtype.encode('gb2312')
        else:
            str_newtype = newtype
        types  = set(self.getClientTypes())
        types.add(str_newtype)
        if not self.__config.has_section('client'):  self.__config.add_section('client')
        self.__config.set('client','types', ','.join(types))
        self.save()
        return True

    #获取客户类型,r
    def getClientTypes(self):
        try:
            str_types = self.__config.get('client','types')
            return  str_types.split(',')
        except:
            return  []
    def getClientTypesu(self):
        clients = self.getClientTypes()
        cu = []
        for i  in range(len(clients)):
            item = unicode(clients[i],'gb2312')
            cu.append(item)
        return  cu

    #获取帐户名
    def getUserList(self):
        try:
            str_users = self.__config.get('login','users')
            users = str_users.split(',')
            return  users
        except:
            return []

    def getUserListu(self):
        users = self.getUserList()
        for u in users:
            u = u.decode('gb2312')
        return  users

    def addUserName(self, newname):
        if len(newname)<= 0: return False
        #unicode转换成string
        if type(newname)==type(u''):
            str_newname = newname.encode('gb2312')
        else:
            str_newname = newname
        if ',' in newname: return False
        old_username_list = self.getUserList()
        #如果当前记录超过10个,移除最头的一个
        if len(old_username_list) > 10:
            old_username_list.pop(0)
        names  = set(old_username_list)
        names.add(str_newname)
        if not self.__config.has_section('login'):
            self.__config.add_section('login')
        self.__config.set('login','users',','.join(names))
        self.save()
        return  True

g_configfile = SysConfigFile()

if __name__=="__main__":
    sc = SysConfigFile()
    sc.setFilePath('D:\\a.ini')
    sc.addClientTypes('中国的')
    sc.addClientTypes('doifsuee')
    print 'client list ', sc.getClientTypes()
    print 'client list __u ', sc.getClientTypesu()
    for c in sc.getClientTypes():
        print unicode(c, 'gbk')

    print 'userlist ',  sc.getUserList()
    sc.addUserName('jiang')
    sc.addUserName('admin')
    print 'userlist ', sc.getUserList()

    a = [u'fuck',u'中国的',u'shi赤']
    a.pop(0)
    print a
    a.append('fodiodd')
    print u'--==-%s'%a

