objectCount = 2
class Person(object):
    objectCount=0   
    def __init__(self,name):
        self.name=name      
        self.objectCount=0 
        objectCount += 1
   
    def pick(self) :
        self.objectCount += 1
        Person.objectCount += 1     #self.__class__.count_beans += 1
        print objectCount,self.name, self.objectCount, Person.objectCount
p = Person('leo')
Person.objectCount += 1
p.pick()
