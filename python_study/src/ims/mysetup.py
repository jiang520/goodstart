# -*- coding: gb2312 -*-
__author__ = 'Administrator'

# mysetup.py
from distutils.core import setup
import py2exe
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")


py2exe_options = {
        "includes":["sip",],
        "dll_excludes": ["MSVCP90.dll"]
        }

#生成安装包
setup(windows=[{"script":"__init__.py",
                "icon_resources":[(1,"images/stock.ico")]
               }],
      version     = u"0.4.0",
      description = u"UT库存管理系统",
      right       = u'版权归ericwill所有',
      name        = u"UT库存管理系统",
      zipfile     = None,
      options     = {'py2exe':py2exe_options},
      #data_files=[("images", ["images//*.png"])]
)


import shutil
import os
curdir = os.getcwdu()
print curdir
#复制文件
if curdir != '':
    print '========rmtree '+ curdir+'\\dist\\images'
    try:
        shutil.rmtree(curdir+'\\dist\\images')
    except:
        print '======rm dir failed'
    try:
        shutil.copytree('images', 'dist/images')
    except:
        print '======copy images failed'
    fileNeedCopys = ['ims_acticle.db3', 'SQLiteSpy.exe']
    for filename in fileNeedCopys:
        print '=========copy %s to dist/%s'%(filename,filename)
        shutil.copyfile(filename,  'dist/%s'%filename)
    shutil.move(curdir+u'\\dist\\__init__.exe', curdir+u'\\dist\\UT库存管理系统.exe')
    sys.exit(0)

    if not os.path.isdir(curdir+u'\\dist\\images'):
        os.mkdir(curdir+u'\\dist\\images')
    shutil.copytree(curdir+u'\\images', curdir+u'\\dist\\images')
    strSrc = u'%s\\dist'%curdir
    strDst = curdir+u'\\库存管理系统'
    print 'mvdir from [%s]->[%s]'%(strSrc, strDst)
    os.rmdir(unicode(strDst))
    os.rename(strSrc, strDst)
    os.system(u'rmdir /q /s '+strDst)
    os.system(u'mkdir '+strDst)
    cmd = u'xcopy /q /s %s %s'%(strSrc, strDst)
    print 'cmd ',cmd
    os.system(cmd)