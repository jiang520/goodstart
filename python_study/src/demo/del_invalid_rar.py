'''
this file is used to delete invalid rar package of ut500/ut1000
'''
import os
import re
''' find spec file name in the cmd output'''
def findSpecFileInRar(strRar, strPatten):
    print "input parm' type'=",type(strRar)
    if type(strRar) == type('str'):
        print "try to open file :" , strRar
        try:
            filetemp = open(strRar, "r")
        except:
            print '=========open file failed :', strRar
            return False
    elif str(type(strRar)) == "<type 'file'>":
        filetemp = strRar
    else:
        print 'Invalid param of strRar'
        raise TypeError
        return False
        #print strRar.readlines()
    if filetemp == None:
        print strRar,"does not exist !"
        return False
    bfind = False
    print filetemp.tell()
    filetemp.seek(0, 0)
    print filetemp.tell()
    for line in filetemp.readlines():
        #print line
        if re.match(strPatten, line):
            print 'find match with:', line
            bfind = True
    filetemp.close()
    return bfind

strDir = 'd:\\'
rarpath = "D:\\Program Files\\WinRAR\\rar.exe"
if False == os.path.exists(rarpath):
    print rarpath + "not exist !"
    exit()
if False == os.path.exists(strDir):
    print rarpath + "not exist !"
    exit()
for filename in os.listdir(strDir):
    #print "check in file:",strDir, file  
    if ".rar" == filename[-4:].lower():
        print "check in file:",strDir + filename
        #strcmd = "\"D:\\Program Files\\WinRAR\\rar.exe\" l  %s%s > temp.txt"%(strDir,file)
        strcmd = "\"D:\\Program Files\\WinRAR\\rar.exe\" l  %s%s "%(strDir,filename)
        print strcmd
        #str = os.system(strcmd)
        ppfile = os.popen(strcmd) 
        #print str.readlines()
        #print '--------write to temp.txt--------'  
        strPatten = "^.*.cc\s{1,}"  
        if findSpecFileInRar(ppfile, strPatten):#"temp.txt"
            print "now please don't del the rar file "
        else:
            print "nothing like [%s] found in %s%s "%( strPatten, strDir, filename)
        if os.path.exists("temp.txt"):
            os.remove("temp.txt")
        
