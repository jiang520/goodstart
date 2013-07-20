#encoding=gb2312
'''
Created on 2013-7-17

@author: jiang
'''

import urllib2
import urllib
import re

def getimg(url):
    
    rep = urllib2.urlopen(url)
    print rep
    print dir(rep)
    lines = rep.readlines()
    i = 0
    urls = []
    for line in lines:
        if i % 10 == 0:
            print 'process line:%%d',i*100/len(lines)
        i=i+1
        if line.find('.png')  > 0:
            print line
        #print re.findall('<img \w*>$', line)
        res =  re.findall('http://[^\'\"]*.jpg', line)        
        if res != None and len(res) > 0:
            print res
            urls.extend(res)
    return urls
            
def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per,
def save(url):
    local = "d:\\pic\\test\\%s.jpg"%url.__hash__() 
    urllib.urlretrieve(url, local, cbk)
    
if __name__ == '__main__':   
    url = 'http://sports.qq.com/nba/?pgv_ref=aio2012&ptlang=2052'
    '''获取网页的url'''
    imgurls = getimg(url)
    print 'imgurls -= ', imgurls
    print 'start to get images....'
    i=0

    for url in imgurls:
        if i>30:
            break;
        i=i+1
        print '---[%d]'%i,url
        save(url)
        print '--end'
        
    print 'image get finished..............'
  
  
    