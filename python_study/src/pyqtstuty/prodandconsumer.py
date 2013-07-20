'''
Created on 2013-6-8

@author: jiang
'''
import threading
import time
import random
from Queue import Queue
class Producer(threading.Thread):
    def __init__(self, threadname, queue):
        super(Producer, self).__init__(name=threadname)
        self.sharedata = queue
    
    def run(self):
        for i in range(20):
            print self.getName(), "adding", i, 'to queue'
            self.sharedata.put(i)
            time.sleep(random.randrange(10)/10.0)
        print self.getName(), 'is exiting ...'


#Consumer thead
class Consumer(threading.Thread):
    def __init__(self, theadname, queue):
        super(Consumer, self).__init__(name=theadname)
        self.sharedata = queue
        
    def run(self):
        for i in range(20):
            print self.getName(),"got a value:", self.sharedata.get()
            time.sleep(random.randrange(10)/10.0)
        print 'thead [%s] is exiting ...'%self.getName()

if __name__ == '__main__':
    queue = Queue()
    producer = Producer("prod1",queue)
    consumer = Consumer("csm1",queue)
    producer.start()
    consumer.start()
    
    time.sleep(40)
    print 'try to stop all thread...'
    producer.join(3)
    consumer.join(3)