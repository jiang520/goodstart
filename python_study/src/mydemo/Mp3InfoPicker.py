#coding=gbk
'''
Created on 2012-7-15

@author: jiang
'''
import struct

class Mp3InfoPicker:
    
    def __init__(self, path):
        self.path = path
        
        try:
            fp = open(path, 'rb')
        except:
            print 'invalid file path'
            return None
        if (fp==None): return
        fp.seek(-128, 2)      
        #tag  = struct.unpack('3s', f.read(3))
        #print tag
        strIdv31 = fp.read(93)
        print strIdv31
        (self.a,self.b, self.c,self.d)=struct.unpack('3s30s30s30s',strIdv31)
        print self.a, self.b, self.c, self.d,
        strlast3 = fp.read(35) 
        (self.e, self.f, self.g) = struct.unpack('4s30s1b', strlast3)
        
        print self.e, self.f,int(self.g)
        fp.close()   
        
        '''1-3 3 ��š�TAG���ַ�����ʾID3 V1.0��׼�����������Ǹ�����Ϣ�� 
        4-33 30 ���� 
        34-63 30 ���� 
        64-93 30 ר���� 
        94-97 4 ��� 
        98-127 30 ��ע 
        128 1 MP3������𣬹�147�֡�
        '''
    def GetTag(self):
        return self.a
    def GetName(self):
        return self.b
    def GetAuthor(self):
        return self.c
    def GetZj(self):
        return self.d
    def GetYear(self):
        return self.e
    def GetDetail(self):
        return self.f
    def GetType(self):
        return self.g

if __name__=='__main__':
    obj = Mp3InfoPicker('d:\\test.mp3')
    