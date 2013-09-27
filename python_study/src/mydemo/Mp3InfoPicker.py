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
        
        '''1-3 3 存放“TAG”字符，表示ID3 V1.0标准，紧接其后的是歌曲信息。 
        4-33 30 歌名 
        34-63 30 作者 
        64-93 30 专辑名 
        94-97 4 年份 
        98-127 30 附注 
        128 1 MP3音乐类别，共147种。
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
    