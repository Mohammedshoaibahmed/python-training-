n=5
def fibb(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibb(n-1)+fibb(n-2)
for i in range(1,n+1):
    print(fibb(i))