# listofequipment={}

# class sports:
#     def crud(self):
#         print("Select the operations u wnat to perform")
#         while True:
#             a=int(input("1. CREATE  2.ADD  3.REMOVE  4.UPDATE"))
#             if a==1:
#                 ep=int(input("enter the equipment id"))
#                 eq=int(input("enter the equipment name"))
#                 listofequipment[ep]=eq
#                 print(listofequipment)
#             elif a==2:
#                 ep=int(input("enter the equipment id"))
#                 eq=int(input("enter the equipment name"))
#                 listofequipment[ep]=eq
#                 print(listofequipment)
#             elif a==3:
#                 eq=int(input("enter the equipment id"))
#                 listofequipment.popitem(eq)
#             else:
#                 print("no such choice")    
                


# obj=sports()
# obj.crud() 
  
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

  