
import os.path
print 'this module walk in the dir'

def visitdir(arg, dirname, names):
    print 'dir name=', dirname
    print names     
    for filepath in names:
       print os.path.join(dirname, filepath)
       #print arg
  	   
if __name__=='__main__':
    path = 'd:\pic'
    os.path.walk(path, visitdir, (3,))
    for root, dirs, files in os.walk(path):
        print '--------root=', root
        print '--------dirs=', dirs
        for file in files:
            print file