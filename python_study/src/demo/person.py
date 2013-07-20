'''
Created on 2012-6-2
moduld person
@author: jiang
'''
#from file import  
class person(object):
    name = ''
    age = 0
    def __str__(self):
        return "\n[%8s,%3d]"%(self.name,self.age)
    def __init__(self,name, age):
        self.name = name
        self.age = age
        


def addperson(personlist):
    print 'please input name age:'
    name,age = raw_input(),raw_input()
    print 'you input is name = ',name, 'age = ', age
    list.append(person(name, age))

def removeperson(personlist):
    displayall(list)
    print 'please input the person whos name you want to remove '
    name = raw_input()
    for person in list:
        if person.name == name:
            list.remove(person)
            print 'remove person',person
 
def displayall(personlist):
    for person in personlist:
        print person,"name=",person.name, "age = ",person.age
        
def initpersonlist(personlist):
    personlist.append(person('john', 33))
    personlist.append(person('tom', 8))
    personlist.append(person('le', 15))       
if __name__=="__main__":
    personlist = []
    initpersonlist(personlist)
    while(True):
        print "1.add person"
        print "2.remove person"
        print "3.display all"
        
        sel = raw_input()
        print "you select :",sel        
        result = {
             '1':addperson,
             '2':removeperson,
             '3':displayall,
             }
        type(result)
        try:
            result[sel].__call__((personlist))
        except:
            print 
            print 'input errro'
print "%s%d"%('ddd',88)
    