'''
Created on 2012-7-15

@author: jiang
'''
import struct 

def writeStruct():
    a = 3
    b = 'a'
    print 'fuck'
    f = open('d:\\test.bin','wb')
    astr = struct.pack('ldf', 4,3.0342424242223002, 2.03424233334)
    f.write(astr)
    f.close()

def readstruct():
    f = open('d:\\test.bin', 'rb')
    bstr = f.read(20)
    (a, b, c) = struct.unpack('ldf', bstr)
    
    print a
    print b
    print c
    
if __name__ == '__main__':
    writeStruct()
    readstruct()
    pass