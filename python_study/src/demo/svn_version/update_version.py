#!encoding=gb2312
'''
Created on 2013-3-20

@author: jiang
@summary:  this file is used to update version number of .rc file

'''
import os
import re
import pysvn
import shutil
import sys

def SetVersion(strSrcPath, a, b, c, d):
    strNewVer = "%d,%d,%d,%d"%(a,b,c,d)       
    if os.path.isfile(strSrcPath)==False:
        print '----file not exit! '
        exit()
    'copy src file to src.bak,the write the changed file to srcfile'
    shutil.copy(strSrcPath, strSrcPath+".bak")
    fileBak=open(strSrcPath+".bak","r")
    fileSrc=open(strSrcPath, "w")
    i = 0;
    print 'searching the file'
    for line in fileBak.readlines():
        i = i+1
        #if len(line) > 10:
        #    print line
        bMatch = False
        if re.match('^\s*FILEVERSION\s+(\d{1,5},){3}\d{1,5}\s*$',line):
            bMatch = True
        elif re.match('^\s*PRODUCTVERSION\s+(\d{1,5},){3}\d{1,5}\s*$',line):
            bMatch = True
        #print start   
        if bMatch:
            old = line
            new = re.sub('(\d{1,5},){3}\d{1,5}\s*$', str(strNewVer), old, 1)
            print old, '->', new 
            line = new+ '\n'
            print 'repleace line[%d]'%i, ':', line
        fileSrc.write(line)           
    fileSrc.close
'''
@deprecated: use svn command to get version number
'''    
def GetVersionNumber(strPath):
    if os.path.exists(strPath)==False:
        return None
    if os.path.isdir(strPath)==False:
        return None
    
    strcmd = "svn info %s "%strPath
    print strcmd
    file = os.popen(strcmd)
    #file = open('temp.txt', 'r')
    print file.readlines()
    
    
    for line in file.readlines():
        if re.match('\s*版本: \d*\s*', line):
            strVersion = line.lstrip()
            strVersion = strVersion.lstrip('版本: ')
            return strVersion

'''get version number use pysvn API'''
def GetVersionNumberByPySvn(strPath):
    if os.path.isdir(strPath)==False:
        return None
    try:
        client = pysvn.Client()
        entity = client.info(localdir)
    except:
        print 'try get svn info of ',strPath,'failed'
        return None    
    return entity.revision.number

'''
1.find file in dir
2.get svn number
3.change version info in *.rc file
'''
if __name__=='__main__':
    print __doc__
    #localdir = "d:\\redmine2.1-stable";
    #localdir="D:\\workspace\\tab"
    if len(sys.argv) > 1:
        localdir = sys.argv[1]
    else:
        while True:
            localdir = raw_input("please input dir path")
            if os.path.isdir(localdir):
                break
    if not os.path.isdir(localdir):
        print 'invalid directroy ! retry please !localdir = ', localdir
        sys.exit(0)
        
    svnnum = GetVersionNumberByPySvn(localdir)
    if(svnnum == None):
        print 'failed to get version number of ', localdir
        sys.exit(0)
    rcfiles=[]
    for filename in os.listdir(localdir):
        #print filename
        if os.path.isfile(os.path.join(localdir,filename)) and re.match('\w*.rc$',filename)!=None:
            #print filename
            rcfiles.append(os.path.join(localdir,filename))
    #print 'files=',rcfiles
    if len(rcfiles) != 1:
        print '*rc files not found in %s'%(localdir)
        sys.exit(0)
    a=1
    b=0
    c=0 
    print 'Ready to change version to %d,%d,%d,%d of %s'%(a,b,c,svnnum, rcfiles[0])   
    choose = raw_input('Are you sure to change?(y/n):')
    if choose != 'y' and choose != 'Y':
        print 'Thanks for use!Bye!'
        sys.exit(0)               
    SetVersion(rcfiles[0], a, b, c, svnnum)
    print 'version change finished !'
    if 'y'== raw_input('press y to edit rc file(y/n):'):
        os.system("notepad.exe "+rcfiles[0])
    print 'Thanks for use!Bye!'
    
    
