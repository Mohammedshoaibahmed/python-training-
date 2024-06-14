#oops    
#class-> it is the collection of datamembers(variables) and member function(methods)
#object-> it is defined as by which we can access all the data members and member function of a class
#constructor->it is called automatically when the object is created
'''class calculations:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        ar=self.a+self.b  
        print("sum of a and b is",ar)
    def sub(self):
        ar=self.a-self.b  
        print("sub of a and b is",ar)
    def mul(self):
        ar=self.a*self.b  
        print("mul of a and b is",ar)        

obj=calculations(3,2) 
obj.add()  
obj.sub()
obj.mul()    
'''
#inheritance
#singleinheritance
'''class calculations:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        ar=self.a+self.b  
        print("sum of a and b is",ar)

class calculation1(calculations):
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def sub(self):
        ar=self.a-self.b    
        print("sub of a and b is",ar)
obj1=calculations(2,3)
obj1.add()
obj2=calculation1(2,3)
obj2.add()
obj2.sub()'''  
# #multilevel      
'''class calculations:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        ar=self.a+self.b  
        print("sum of a and b is",ar)

class calculation1(calculations):
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def sub(self):
        ar=self.a-self.b    
        print("sub of a and b is",ar)
        
class calculation2(calculation1):
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b 
    def mul(self):
        ar=self.a*self.b  
        print("mul of a and b is",ar) 
     
obj1=calculations(2,3)
obj1.add()
obj2=calculation1(2,3)
obj2.add()
obj2.sub()
obj3=calculation2(2,3)                   
obj3.add()
obj3.sub()
obj3.mul() 
'''
# #multipleinheritance
'''class calculations:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        ar=self.a+self.b  
        print("sum of a and b is",ar)

class calculation1:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def sub(self):
        ar=self.a-self.b    
        print("sub of a and b is",ar)
        
class calculation3(calculations,calculation1) :
       def __init__(self,a,b) -> None:
        self.a=a
        self.b=b 
       def mul(self):
            ar=self.a*self.b  
            print("mul of a and b is",ar) 
obj1=calculations(2,3)
obj2=calculation1(2,3)        
obj4=calculation3(2,3)
obj4.add() 
obj4.sub() 
obj4.mul()


#hiearchical
class calculations:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        ar=self.a+self.b  
        print("sum of a and b is",ar)

class calculation1(calculations):
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def sub(self):
        ar=self.a-self.b    
        print("sub of a and b is",ar)
class calculation2(calculations) :
       def __init__(self,a,b) -> None:
        self.a=a
        self.b=b 
       def mul(self):
            ar=self.a*self.b  
            print("mul of a and b is",ar)        
obj1=calculations(2,3)
obj1.add()
obj2=calculation1(2,3)
obj2.add()
obj2.sub() 
obj3=calculation2(2,3)
obj3.add()
obj3.mul()'''
# In polymorphism there are two types
# 1>compile time->functionoverloading 
# in this there a`re 3 types
# function overloading -> which is not possible in python
# constructor overloading -> which is not possible in python    
# operator overloading-> this is only possible

# 2>runtime polymorphism i.e over ridding      
