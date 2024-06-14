# #problem    [2,1,0,1,1,2,0,0]->[0,0,0,1,1,1,2,2]
a=[2,1,0,1,1,2,0,0]
l=0
m=0
n=0
for i in range(len(a)):
    if a[i]==0:
        l+=1
    if a[i]==1:
        m+=1
    if a[i]==2:
        n+=1 
        
j=0        
while l>0:
    a[j]=0
    j=j+1 
    l-=1              
while m>0:
    a[j]=1
    j=j+1 
    m-=1 
while n>0:
    a[j]=2
    j=j+1 
    n-=1     
print(a) 