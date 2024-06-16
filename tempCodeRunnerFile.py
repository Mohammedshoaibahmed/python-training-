list=[2,3,4,4,5,4,5] 
dict={}
l=len(list)  
vote=int(input("cast u r vote"))    
list.append(vote)
for i in list:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
maximum=0
key=0         
for i,j in dict.items():
    if j>maximum:       
        maximum=j
        key=i    
for i,j in dict.items():
    if j==maximum:
        print(i)    
