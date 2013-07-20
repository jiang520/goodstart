'''
this module is used to delete blank line in File
'''
import re
import os
print os.getcwd()
strPath = "%s\\Teris.py"%os.getcwd()
filesrc = open(strPath, "r")
filedst = open(strPath+'.dst', "w")

if filesrc == None:
    print strPath, "is not exist !"
    exit()
if filedst == None:
    print "can't open the dst file"
    exit()

for line in filesrc.readlines():
    #print re.match('^(\s)*', line)
    if None == re.match('^(\s)*$', line):
        '''del line prefix'''
        line = re.sub('^\d{1,3} ', "", line, 1)
        filedst.write(line)
        '''#print line'''
    else:
        print line
filesrc.close()
filedst.close()
print 'blank line has been deleted!'
print os.system("notepad.exe  "+ strPath+".dst")
#print os.system("copy d:\\pic3 d:\\pic2")
