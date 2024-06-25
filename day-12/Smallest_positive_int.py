def small(l):
    res=999
    for i in l:
        if i>0 and i<res:
            res=i
    print(res)
        
            
l=[-3,6,-4,2,-5,-3,7]
small(l)