#encoding=gb2312
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
        }

#生成安装包
setup(windows=["__init__.py"],
      options={'py2exe':py2exe_options},
      #data_files=[("images", ["images//*.png"])]
)


import shutil
import os
curdir = os.getcwd()
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