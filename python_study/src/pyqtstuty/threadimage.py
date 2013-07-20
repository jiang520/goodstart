'''
Created on 2013-6-8

@author: jiang
'''
from threading import Thread 
import time
import threading

class ThreadImage(Thread):
    '''
    classdocs
    '''
    def __init__(self):
        super(ThreadImage, self).__init__(None)
        '''
        Constructor
        '''
        self.counter = 0
        self.bstop = False
    def run(self):
        self.counter = 0
        while( not self.bstop):
            print 'thread [%s] is running ...'%self.getName()
            self.counter += 1
            
            time.sleep(0.3)
        print 'thread [%s] is exiting..'%self.getName()
        
    def stop(self):
        self.bstop = True
        self.join(3)
            
if __name__=="__main__":
    a = ThreadImage()
    a.setName("set a name")
    a.start()
    b = ThreadImage()
    b.start()
    
    time.sleep(10)
    a.stop()
    b.stop()