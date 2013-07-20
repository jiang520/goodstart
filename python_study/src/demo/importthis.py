'''
Created on 2012-9-22

@author: jiang
'''

#import this
print 'hello'
l= [1, 2]
l.append(l)
print l

import re
#a = re.match('n*', 'name3')
#print 'match', re.match('\d*','39242424')
print '\\'
print 'match', re.match("\d\d\d\d[\\-]\d?[\\-]\d?$", '1980\2\3')

#print a
print re.findall('[n]\w', 'sofonestring')
print re.sub('[n]a*', 'n2', 'strina3g5')
print re.subn('\d\w', '--', 'nal3eo25ife3')
print 'split \d-------', re.split('\d', 'sf9e8afskf8e9we')
print re.findall('[]','sofiefe\\e3\\32')
print '\d'

