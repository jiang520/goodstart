'''
Created on 2013-6-6

@author: jiang
'''
import os
import sys
if __name__ == '__main__':
    exepath = "C:\Python27\Lib\site-packages\PyQt4\pyuic4"
    os.chdir(os.curdir)
    for file in os.listdir(os.curdir):
        print type(file)
        print 'ext =', file[-3:]
        if  len(file) > 3 and (file[-3: ] == '.ui'):
            filename = file.rstrip('.ui')            
            cmd = "%s %s > ui%s.py"%(exepath, file, filename)
            print cmd
            os.system(cmd)
            
        
    pass