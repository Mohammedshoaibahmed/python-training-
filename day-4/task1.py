#list operation
'''list=[2,3,45,'shoaib']
for i in list:
    if i == 'shoaib':
        print(list.index(i))
        print(i)
        '''
#simple class,constructor and object
'''class student:
    def __init__(self,nm,ag,gn) -> None:
        self.name=nm
        self.age=ag
        self.gender=gn       
        
        
st1=student('shoaib',23,'male')        
print(st1.name,st1.age,st1.gender)'''

#class and method
'''class A:
    def __init__(self,a,b):
        self.A=a
        self.__B=b

    def printB(self):
        print(self.__B)
ob1=A(1,3)
print(type(ob1))
print(ob1.A)
ob1.printB()'''