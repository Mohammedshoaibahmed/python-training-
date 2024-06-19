# if i found a smaller element than pivot then incrwase j by 1 and swap it by i
# if i found bigger element than pivot i will do nothing


def partition(l,low,high):
    p=l[high] 
    pi=high
    j=low-1
    for i in range(low,high):
        if l[i]<=p:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi
def quick_sort(l,low,high):
    if low<high:
        pi=partition(l,low,high)        
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return    
if __name__=="__main__":
    l=list(map(int,input("enter the elements").split()))
    low=0
    high=len(l)-1
    print(low,high)
    quick_sort(l,low,high)
    
    print("Sorting array",l)