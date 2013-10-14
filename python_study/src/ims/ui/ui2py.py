'''
Created on 2013-6-6

@author: jiang
'''
import os
import sys
def pyqt_ui_2_py():
    exepath = "C:\Python27\Lib\site-packages\PyQt4\pyuic4"
    print os.getcwd()
    os.chdir(os.getcwd())
    for file in os.listdir(os.curdir):
        #print type(file)
        #print 'ext =', file[-3:]
        if  len(file) > 3 and (file[-3: ] == '.ui'):
            filename = file.rstrip('.ui')
            cmd = "%s %s > ui%s.py"%(exepath, file, filename)
            print cmd
            os.system(cmd)

if __name__ == '__main__':
    pyqt_ui_2_py()
    pass