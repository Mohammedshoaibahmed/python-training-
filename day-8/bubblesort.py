# bubble sort is defined as it works step by step it takes an element  at index 0
# and check with another elements  
'''list=[23,45,67,8,89]
for i in range(0,len(list)):
    for j in range(0,len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print(list)'''

#find minimum
'''list=[23,45,67,8,79]
min=23
for i in range(1,len(list)):
    if min>list[i]:
        min=list[i]
        j=i   
print("minimum value",min,"index value",j) 
'''
#find maximum                   
list=[23,45,67,8,79]
max=23
for i in range(1,len(list)):
    if max<list[i]:
        max=list[i]
        j=i   
print("maximum value",max,"index value",j)