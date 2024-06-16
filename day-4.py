'''list=[2,3,45,'shoaib']
for i in list:
    if i == 'shoaib':
        print(list.index(i))
        print(i)
        '''
'''class student:
    def __init__(self,nm,ag,gn) -> None:
        self.name=nm
        self.age=ag
        self.gender=gn       
        
        
st1=student('shoaib',23,'male')        
print(st1.name,st1.age,st1.gender)'''
# class A:
#     def __init__(self,a,b):
#         self.A=a
#         self.__B=b

#     def printB(self):
#         print(self.__B)
# ob1=A(1,3)
# print(type(ob1))
# print(ob1.A)
# ob1.printB()

##task 1
# class student:
#     def __init__(self):
#         self.name=input("Enter the name")
#         self.usn=input("Enter the usn")
#         self.marks=[]
#         for i in range(5):
#             self.marks.append(int(input("enter the marks")))
#         self.calculation(self.marks)
            
#     def calculation(self,marks):
#         self.cl=sum(marks)     
#         self.percentage=(self.cl/500)*100
#         if self.percentage>=90:
#             self.grade="a"
#         else:
#             self.grade="b"    
#             print(self.name,self.usn,self.cl,self.percentage,self.grade)   
# s=[0]*5
# for i in range(5):
#     s[i]=student()
    