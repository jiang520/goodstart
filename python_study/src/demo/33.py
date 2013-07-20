'''
Created on 2013-5-14

@author: jiang
'''
for y in range(1, 10):
    for x in range(1, y+1):
        print '%d*%d=%-2d '%(x,y, x*y),
    print ''