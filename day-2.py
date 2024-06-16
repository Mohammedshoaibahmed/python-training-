'''arr=[4,0,5,0,1,9,0,0]
l=len(arr)
j=0
for i in range(0,l):
    if arr[i]!=0:
        arr[j]=arr[i]
        j=j+1
        
while(j<l):
    arr[j]=0
    j=j+1        
    
print(arr) '''   
#recurrsion
#factorial
'''n=5
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))'''
#fibbocaci
'''n=5
def fibb(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibb(n-1)+fibb(n-2)
for i in range(1,n+1):
    print(fibb(i))'''
                 
                 
'''def p(n,m):
    if m==0:
        return 1
    return n*p(n,m-1)

res=p(2,3)
print(res)                 
'''
#sum of digitsof numbers using recursion 9123
'''def sum(n):
    if n==0:
        return 0
    return ((n%10)+sum(n//10))

print(sum(9123))'''
    
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
# class calculations:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def add(self):
#         ar=self.a+self.b  
#         print("sum of a and b is",ar)

# class calculation1(calculations):
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def sub(self):
#         ar=self.a-self.b    
#         print("sub of a and b is",ar)
# obj1=calculations(2,3)
# obj1.add()
# obj2=calculation1(2,3)
# obj2.add()
# obj2.sub()  
# #multilevel      
# class calculations:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def add(self):
#         ar=self.a+self.b  
#         print("sum of a and b is",ar)

# class calculation1(calculations):
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def sub(self):
#         ar=self.a-self.b    
#         print("sub of a and b is",ar)
        
# class calculation2(calculation1):
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b 
#     def mul(self):
#         ar=self.a*self.b  
#         print("mul of a and b is",ar) 
     
# obj1=calculations(2,3)
# obj1.add()
# obj2=calculation1(2,3)
# obj2.add()
# obj2.sub()
# obj3=calculation2(2,3)                   
# obj3.add()
# obj3.sub()
# obj3.mul() 

# #multipleinheritance
# class calculations:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def add(self):
#         ar=self.a+self.b  
#         print("sum of a and b is",ar)

# class calculation1:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def sub(self):
#         ar=self.a-self.b    
#         print("sub of a and b is",ar)
        
# class calculation3(calculations,calculation1) :
#        def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b 
#        def mul(self):
#             ar=self.a*self.b  
#             print("mul of a and b is",ar) 
# obj1=calculations(2,3)
# obj2=calculation1(2,3)        
# obj4=calculation3(2,3)
# obj4.add() 
# obj4.sub() 
# obj4.mul()


# #hiearchical
# class calculations:
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def add(self):
#         ar=self.a+self.b  
#         print("sum of a and b is",ar)

# class calculation1(calculations):
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def sub(self):
#         ar=self.a-self.b    
#         print("sub of a and b is",ar)
# class calculation2(calculations) :
#        def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b 
#        def mul(self):
#             ar=self.a*self.b  
#             print("mul of a and b is",ar)        
# obj1=calculations(2,3)
# obj1.add()
# obj2=calculation1(2,3)
# obj2.add()
# obj2.sub() 
# obj3=calculation2(2,3)
# obj3.add()
# obj3.mul()
  
  
  
  
# #problem    [2,1,0,1,1,2,0,0]->[0,0,0,1,1,1,2,2]
# a=[2,1,0,1,1,2,0,0]
# l=0
# m=0
# n=0
# for i in range(len(a)):
#     if a[i]==0:
#         l+=1
#     if a[i]==1:
#         m+=1
#     if a[i]==2:
#         n+=1 
        
# j=0        
# while l>0:
#     a[j]=0
#     j=j+1 
#     l-=1              
# while m>0:
#     a[j]=1
#     j=j+1 
#     m-=1 
# while n>0:
#     a[j]=2
#     j=j+1 
#     n-=1     
# print(a)        
        
    
# In polymorphism there are two types
# 1>compile time->functionoverloading 
# in this there a`re 3 types
# function overloading -> which is not possible in python
# constructor overloading -> which is not possible in python    
# operator overloading-> this is only possible

# 2>runtime polymorphism i.e over ridding      



#project
# create a class car_show_room in which 
# 1. create a function named car_company() which will allow user to select a car company out of the displayed companies. if the user enters any random car company he/she should be asked to re-enter.
# 2. according to the car company selected the user should be redirected to selecting the models of that company out of the given list. if any thing other than list is given then re-enter.
# 3. after selecting the model the user should be redirected to selecting the variant.
# 4. according to the car company model and variant a price should be calculated to which sgst and cgst are added to make it the total price. 
# note:- sgst and cgst are common for all the cars.
class carshowroom:
    def select_model(self,sl):
        while True:
            if sl==1:
                print("u have selected MANUAL MODEL")
                print("select the variant")
                print("1>PETROL   2>DIESEL ")
                pl=int(input())
                obj.variant(pl)
                break
            elif sl==2:
                print("u have selected MANUAL MODEL")
                print("select the variant")
                print("1>PETROL   2>DIESEL ")
                pl=int(input())
                obj.variant(pl)
                break
            else:
                print("please re enter")    
                    
    def car_company(self,ch):
        while True:
            if ch==1:
                print("you have choosen WOLKSWAGEN ")
                print("select the model u need")
                print("1>MANUAL   2>FULL AUTOMATIC ")
                sl=int(input())
                obj.select_model(sl)
                break
            elif ch==2:
                print("you have choosen MERCEDES") 
                print("select the model u need")
                print("1>MANUAL   2>FULL AUTOMATIC ")
                sl=int(input())
                obj.select_model(sl)
                break
            else:
                print("please re enter") 
                
    def variant(self,pl):
        if pl==1:
            print("u have selected PETROL variant") 
            print("the total cost is 5000000")
            obj.billing(ql)
             

        elif pl==2:
            print("u have selected DIESEL variant") 
            print("the total cost is 1000000") 
            obj.billing(ql)
    def billing(self,ql):
        sgst=0.10
        cgst=0.10
        if ql==1:
            price=ql(ql*sgst*cgst)
            print(price)
        
                           
print("WELCOME TO CAR SHOWROOM")
print("choose the car company you want to buy")
ch=int(input("1. wolksvagen    2.Mercedes")) 
obj=carshowroom()
obj.car_company(ch)  