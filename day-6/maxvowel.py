# n=int(input (" enter the number of person"))
# d
# input_sentences=input("Enter name with colon and sentences")
def count_vowel(n):
    dict={'A':0,'a':0,'E':0,'e':0,'I':0,'i':0,'O':0,'o':0,'U':0,'u':0}
    for i in n:
        if i=='A' or i=='a':
            dict['A']+=1
        elif i=='E' or i=='e':
            dict['E']+=1
        elif i=='I' or i=='i':
            dict['I']+=1
        elif i=='O' or i=='o':
            dict['O']+=1           
        elif i=='U' or i=='u':
            dict['U']+=1
                
    x=max(dict.values()) 
    result=[]
 
    for i,j in dict.items():
        if j==x:
            result.append(i)
    return result 
i_p=[["man","dog is black in colour"],["god","its my creation"]]
       
res={}
for i in i_p:
    res[i[0]]=count_vowel(i[1])
    
print(res)            