'''
Created on 2012-7-15

@author: jiang
'''

import re
class FileBlankDeleter(object):
    '''
    classdocs
    '''


    def __init__(self,path):
        '''
        Constructor
        '''
        self.path = path
        pass
    
    def process(self):
        if(self.path == None or len(self.path) <= 0):
            return 'empty path'
        str = self.path        
        dotpos = str.rindex('.')
        if(dotpos < 0 ):
             dotpos = len(str)
        str = str[0:dotpos] + 'new' + str[dotpos:] 
        #print str
        
        try:
            filesrc = file(self.path,'r')
            filedst = file(str, "w")
        except:
            return 'file open failed'
        srccount = 0;
        dstcount = 0;
        for line in filesrc.readlines():
            # print line
            #print 'line strip ---',len(line.strip())
            srccount += 1
            
            print '134-foo'[0:3];
            if( re.match('\d\d\d[ ]',line[0:4])):
                line = line.lstrip(line[0:4]);
                print line
            if(len(line.strip()) > 0):
                filedst.write(line)
                dstcount += 1
            #if(a>10): break;
        filesrc.close()
        filedst.close()
        return self.path +'\nprocess successed!\n%s:%d,%s:%d'%('dstlincount:', dstcount,'srclinecount',srccount)