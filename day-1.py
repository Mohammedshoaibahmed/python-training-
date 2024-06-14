#calculate the sum of a number where each digit is powered to number of digit(armstrong)
'''x=1634
y=x
p=x
length=0
while(y>0):
    length+=1
    y=y//10
print(length) 
sum=0
while(x>0):
    rem=x%10
    sum+=rem**length
    x=x//10
print(sum) 
if sum==p:
    print("arm")
else:
    print("no arm")  
    '''
    
#2
'''x=153
y=x
p=x
length=0
while(y>0):
    length+=1
    y=y//10
print(length) 
sum=0
while(p>0):
    rem=p%10
    sum+=rem**length
    length=length-1
    p=p//10
print(sum) '''
#3(patterns)
'''n=4
for i in range(i=0):
    for i in range(i=n-1):
        print('*')'''
#chessboard
'''
e_r="1357"
o_r="2468"
e_c="bdfh"
o_c="aceg"
s="a7"
if s[0] in e_c:
    if s[1] in e_r:
        print("white")
    else:
        print("black")   
else:
    if s[1] in e_r:
        print("black")
    else:
        print("white")    
            '''
#prisoners        
'''pri=6
cho=10
s=4
p=(s+cho-1)%pri
if p==0:
    p=pri
    print(p)
else:
    print(p) '''

#write a program to built a login system using function        
#first it should ask the user to enter the details for registration 
# out of all this details only username and passed to be stored
#now this function should ask ue=ser to enter username and passwd 
# if these mathc with regesterd details in not repeat the login process to enter again    
dict={}
def register(): 
    print("Welcome to registration")     
    print("enter the user name and password")
    usr=input()
    passwd=input()
    name=input("enter ur name")
    dict[usr]=passwd
    print(dict)
    while True:
        print("Welcome login")
        usr=input("enter the user name")
        passwd=input("enter the passwd")
        if usr in dict:
            if dict[usr]==passwd: 
                print("Login Succesful")
                break
                
            else:
                print("password is wrong")
        else:
            print("user not found")
            break

register()    


    
       