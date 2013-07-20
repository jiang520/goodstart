'''
Created on 2012-6-2

@author: jiang
'''
import sys
import os
class student:
    _name  = 'nameJOhn'
    __age = 33
    id = 4
    __sex_='male'
    
a= student()
print 'a._name=',a._name;
print 'a.id=', a.id
#print 'a.__sex=', a.__sex_
#print 'a.__age__=',a.__ag

print a.id
a.id = 525
b = student()
student.id  = student.id + 20
print 'b._name=', b._name
print 'b.id=', b.id
print 'a.id=', a.id
print 'student.id = ', student.id

class Fruit:
    print 'ehllo world this is a good ideal fuck you are ha'
    price = 0
    def __init__(self):
        self.color = 'red'
        zone = 'china'
        
if __name__ == "__main__":
    print Fruit.price
    apple = Fruit();
    print apple.color
    Fruit.price = Fruit.price + 10
    print "apple'price = ", str(apple.price)
banana = Fruit()
print 'banala\'s price = ', banana.price