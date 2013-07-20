'''
Created on 2013-4-2

@author: jiang
'''
from symbol import arglist
import sys
import os
if __name__=='__main__':
    print sys.argv
    print len(sys.argv)
    
    if os.path.isdir(sys.argv[1]):
        print 'you input a directory'
    else:
        print 'error input  !'