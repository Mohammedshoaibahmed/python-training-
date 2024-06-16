# # printing reverse of list
'''list=[2,3,4,5,6,7]
li = list[-1::-1]
print(li)'''

#prime number
'''m=int(input("Enter the number"))
flag=0
list=[]
if m<=0:
    flag=1
elif m==1:
    flag=0
else:        
    for i in range(2,(m//2)+1):
        if(m%i==0):
            flag=1
            break
if flag==0:
    print("it is a prime")
else:  
    print("it is not a prime") ''' 
    
#fibannoci series
n=int(input("enter the number of terms"))
def fibb(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
for i in range(1,n+1):
    print(fibb(i))    
    
      